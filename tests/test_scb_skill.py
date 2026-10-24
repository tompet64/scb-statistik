"""Offline checks for the skill's document structure, not statistical correctness.

Run: python -m pytest -q tests/test_scb_skill.py
Requires pytest and PyYAML only; does not import pxstatspy or call SCB.
"""

from pathlib import Path
import re
import socket
from urllib.parse import unquote, urlsplit

import pytest
import yaml


SKILL = Path(__file__).resolve().parents[1]


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def blocked(*args, **kwargs):
        pytest.fail("Skill file checks must not use the network")

    monkeypatch.setattr(socket.socket, "connect", blocked)
    monkeypatch.setattr(socket.socket, "connect_ex", blocked)
    monkeypatch.setattr(socket, "getaddrinfo", blocked)


class UniqueKeyLoader(yaml.SafeLoader):
    """Reject duplicate keys instead of silently retaining the last value."""


def unique_mapping(loader, node):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node)
        if key in result:
            raise ValueError("Duplicate YAML key: {}".format(key))
        result[key] = loader.construct_object(value_node)
    return result


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping
)


def frontmatter(text):
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
    assert match, "SKILL.md must start with delimited YAML frontmatter"
    metadata = yaml.load(match[1], Loader=UniqueKeyLoader)
    assert isinstance(metadata, dict), "Frontmatter must be a mapping"
    for field in ("name", "description"):
        assert isinstance(metadata.get(field), str) and metadata[field].strip(), (
            "Missing or invalid {}".format(field)
        )
    assert len(metadata["description"]) <= 1024, "Description exceeds installation limit"
    assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", metadata["name"])
    assert len(metadata["name"]) < 64
    return metadata


def local_targets(document, root):
    """Support inline code paths, inline Markdown links and link definitions.

    references/... and SKILL.md in code spans are skill-root-relative, as
    already used by these guides. Other code file paths are document-relative.
    Markdown links are always document-relative. Remote URLs are not checked.
    """
    text = document.read_text(encoding="utf-8")
    for value in re.findall(r"`([^`\n]+)`", text):
        if re.fullmatch(r"[\w./-]+\.(?:md|ya?ml|txt)", value):
            base = root if value.startswith("references/") or value == "SKILL.md" else document.parent
            yield base / value
    links = re.findall(r"\]\(<?([^\s)>]+)>?(?:\s+[^)]*)?\)", text)
    links += re.findall(r"^\s*\[[^]\n]+\]:\s*<?([^\s>]+)>?", text, re.M)
    for value in links:
        url = urlsplit(value)
        if not url.scheme and not url.netloc and url.path:
            yield document.parent / unquote(url.path)


def validate_references(root):
    documents = sorted(root.rglob("*.md"))
    assert documents, "No skill Markdown files found"
    for document in documents:
        for target in local_targets(document, root):
            assert target.resolve().is_relative_to(root.resolve()), (
                "Reference escapes skill: {} -> {}".format(document, target)
            )
            assert target.is_file(), "Missing reference: {} -> {}".format(document, target)
    # Every bundled reference must also remain discoverable from SKILL.md.
    linked = {p.resolve() for p in local_targets(root / "SKILL.md", root)}
    for reference in (root / "references").iterdir():
        if reference.is_file():
            assert reference.resolve() in linked, "Unlisted reference: {}".format(reference)


def documented_topics(root, text):
    topics = set(re.findall(r"^## (.+?) starter method\s*$", text, re.M))
    topics.update(re.findall(r"^## Grundmetod: (.+?)\s*$", text, re.M))
    for guide in (root / "references").glob("*-workflow.md"):
        if guide.name == "semantic-workflow.md":
            continue  # General search method, not a statistical subject.
        heading = guide.read_text(encoding="utf-8").splitlines()[0]
        match = re.fullmatch(r"# SCB (.+) workflow", heading)
        assert match, "Use '# SCB <topic> workflow' in {}".format(guide)
        topics.add(match[1])
    return {topic.casefold() for topic in topics}


def validate_topics(root, text):
    description = frontmatter(text)["description"].casefold()
    topics = documented_topics(root, text)
    assert topics, "No documented statistical subjects found"
    for topic in topics:
        # Reference guides may stay English while SKILL.md is Swedish.
        aliases = {
            "population": ("befolkning",),
            "household": ("hushållsstatistik",),
            "household statistics": ("hushållsstatistik",),
            "income": ("hushållens inkomster",),
            "household income": ("hushållens inkomster",),
            "education": ("utbildning och studiedeltagande",),
            "education and study participation": ("utbildning och studiedeltagande",),
            "housing": ("boende och bostadsförhållanden",),
            "commuting": ("pendling",),
            "geodata": ("geografi", "geography"),
        }
        terms = (topic,) + aliases.get(topic, ())
        assert any(re.search(r"\b" + re.escape(term) + r"\b", description) for term in terms), (
            "Description does not mention documented topic: {}".format(topic)
        )


def validate_steps(text):
    match = re.search(r"^## (?:Arbetsgång|Workflow)\s*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    assert match, "Missing Arbetsgång/Workflow section"
    numbers = [int(n) for n in re.findall(r"^(\d+)\. ", match[1], re.M)]
    assert numbers and numbers == list(range(1, len(numbers) + 1)), (
        "Workflow steps must be sequential from 1: {}".format(numbers)
    )


def test_skill_frontmatter():
    metadata = frontmatter((SKILL / "SKILL.md").read_text(encoding="utf-8"))
    assert metadata["name"] == SKILL.name


def test_bundled_yaml_syntax():
    for path in sorted(SKILL.rglob("*")):
        if path.suffix in (".yaml", ".yml"):
            data = yaml.load(path.read_text(encoding="utf-8"), Loader=UniqueKeyLoader)
            assert isinstance(data, dict), "Expected YAML mapping in {}".format(path)


def test_skill_references():
    validate_references(SKILL)


def test_skill_description_covers_documented_topics():
    validate_topics(SKILL, (SKILL / "SKILL.md").read_text(encoding="utf-8"))


def test_skill_workflow_numbering():
    validate_steps((SKILL / "SKILL.md").read_text(encoding="utf-8"))


def test_education_acceptance_cases_are_registered():
    acceptance = (SKILL / "docs" / "scb-statistik-acceptance.md").read_text(encoding="utf-8")
    assert "### E1 — Highest recorded education" in acceptance
    assert "### E2 — Participation in studies during a term" in acceptance
    assert "TAB3981" in acceptance
    assert "TAB3732" in acceptance


def test_regional_accounts_acceptance_cases_are_registered():
    acceptance = (SKILL / "docs" / "scb-statistik-acceptance.md").read_text(encoding="utf-8")
    assert "### R1 — Regional production versus resident household income" in acceptance
    assert "### R2 — Municipal coverage, units and revisions" in acceptance
    assert "NR0105ENS2010T01A" in acceptance
    assert "NR0105ENS2010T02B" in acceptance


def test_housing_acceptance_cases_are_registered():
    acceptance = (SKILL / "docs" / "scb-statistik-acceptance.md").read_text(encoding="utf-8")
    assert "### HOU1 — Household housing form versus dwelling stock" in acceptance
    assert "### HOU2 — Housing area versus overcrowding" in acceptance
    assert "### HOU3 — Housing costs and coverage" in acceptance
    assert all(code in acceptance for code in ("HE0111", "BO0104", "HE0202"))


def test_aku_acceptance_cases_are_registered():
    acceptance = (SKILL / "docs" / "scb-statistik-acceptance.md").read_text(encoding="utf-8")
    assert "### AKU1 — Annual labor-market indicators and denominators" in acceptance
    assert "### AKU2 — Education-dimension quality flag" in acceptance
    assert "### AKU3 — AKU versus BAS and geographic detail" in acceptance
    assert "5,263,000" in acceptance
    assert "retroactively to 2012" in acceptance


def test_enterprise_economy_acceptance_cases_are_registered():
    acceptance = (SKILL / "docs" / "scb-statistik-acceptance.md").read_text(encoding="utf-8")
    assert "### FEK1 — Enterprise unit, industry and accounting measures" in acceptance
    assert "### FEK2 — County activity versus enterprise headquarters" in acceptance
    assert "### FEK3 — Statistical-unit and product boundary" in acceptance
    assert "NV0109" in acceptance
    assert "NV1001" in acceptance


def test_kpi_acceptance_cases_are_registered():
    acceptance = (SKILL / "docs" / "scb-statistik-acceptance.md").read_text(encoding="utf-8")
    assert "### KPI1 — Monthly change, inflation and related measures" in acceptance
    assert "### KPI2 — Contract indexation" in acceptance
    assert "### KPI3 — Classification break and historical series" in acceptance
    assert "### KPI4 — KPI versus national-accounts consumption deflator" in acceptance
    assert "### KPI5 — Shadow index versus finalized index" in acceptance
    assert "PR0101" in acceptance
    assert "125.94" in acceptance
    assert "shadow index" in acceptance


@pytest.mark.parametrize("text", [
    "name: example\ndescription: text",  # No delimiters.
    "---\nname: [\ndescription: text\n---\n",  # Invalid YAML.
    "---\n- name\n- description\n---\n",  # Not a mapping.
    "---\nname: example\n---\n",  # Missing description.
    "---\nname: example\ndescription: 42\n---\n",  # Wrong type.
    "---\nname: example\ndescription: ' '\n---\n",  # Empty description.
    "---\nname: Bad_Name\ndescription: text\n---\n",
    "---\nname: example\nname: other\ndescription: text\n---\n",
    "---\nname: example\ndescription: " + "x" * 1025 + "\n---\n",
])
def test_rejects_invalid_frontmatter(text):
    with pytest.raises((AssertionError, ValueError, yaml.YAMLError)):
        frontmatter(text)


@pytest.mark.parametrize("reference", [
    "`references/missing.md`",
    "[guide](references/missing.md#details)",
    "[guide][method]\n\n[method]: references/missing.md",
])
def test_rejects_missing_references(tmp_path, reference):
    (tmp_path / "SKILL.md").write_text(reference, encoding="utf-8")
    with pytest.raises(AssertionError, match="Missing reference"):
        validate_references(tmp_path)


def test_ignores_remote_links_and_accepts_existing_local_links(tmp_path):
    (tmp_path / "references").mkdir()
    (tmp_path / "references" / "guide.md").write_text("[root](../SKILL.md)", encoding="utf-8")
    (tmp_path / "SKILL.md").write_text(
        "`references/guide.md` [guide](references/guide.md#details) "
        "[SCB](https://www.scb.se/anything)", encoding="utf-8"
    )
    validate_references(tmp_path)


def test_rejects_missing_migration_in_description():
    text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    # Remove only the frontmatter keyword, leaving the method guide intact.
    metadata_end = text.index("\n---", 4)
    broken = text[:metadata_end].replace("migration", "other") + text[metadata_end:]
    with pytest.raises(AssertionError, match="migration"):
        validate_topics(SKILL, broken)


def test_rejects_duplicate_workflow_step():
    with pytest.raises(AssertionError, match="sequential"):
        validate_steps("## Workflow\n\n1. First\n2. Second\n2. Duplicate\n")


def test_rejects_reference_outside_skill(tmp_path):
    (tmp_path / "SKILL.md").write_text("[outside](../outside.md)", encoding="utf-8")
    with pytest.raises(AssertionError, match="escapes skill"):
        validate_references(tmp_path)


def test_rejects_unlisted_reference(tmp_path):
    (tmp_path / "references").mkdir()
    (tmp_path / "references" / "forgotten.md").write_text("Guide", encoding="utf-8")
    (tmp_path / "SKILL.md").write_text("No references", encoding="utf-8")
    with pytest.raises(AssertionError, match="Unlisted reference"):
        validate_references(tmp_path)


def test_new_subject_guide_requires_description_update(tmp_path):
    (tmp_path / "references").mkdir()
    (tmp_path / "references" / "education-workflow.md").write_text(
        "# SCB education workflow\n", encoding="utf-8"
    )
    with pytest.raises(AssertionError, match="education"):
        validate_topics(tmp_path, "---\nname: example\ndescription: population\n---\n")
