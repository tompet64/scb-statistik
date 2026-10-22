# SCB education and study participation workflow

Use this guide for population education level or field, and for participation in studies. Resolve current table IDs, category codes, age groups and notes from live PxWebApi v2 metadata on every request; the table names and IDs below are discovery clues observed on 2026-10-22.

## Choose the statistical product

- **Befolkningens utbildning (UF0506 / UREG)** describes the highest education recorded for people in the registered population. It is suitable for questions about educational attainment, level and field.
- **Befolkningens studiedeltagande (UF0507 / RPU)** describes participation in education during a specified term, mainly in the regular education system. It can also classify participants by education level, employment and student-aid use.
- Do not treat UREG attainment as current study participation, or RPU participation as a completed qualification. Neither product alone measures learning outcomes, program effectiveness or causal effects of an education or labor-market intervention; those require a separate evaluation design and suitable data.

## UREG: educational attainment

SCB describes UREG as an annual register of the registered population at 31 December, with each person's highest attained education through the spring term of that year. Statistics are counts of people. Start with these current table candidates and verify their metadata:

| Discovery clue | Scope | Notes |
| --- | --- | --- |
| `Utbildning` / CSV name `TAB3981` / matrix `UF0506A1` | Population aged 16–74 by region, education level, age and sex; years 1985–2025 | Official statistics; unit count; reference date 31 December. Updated 2026-04-27. |
| `UtbSUNBefN` / CSV name `TAB655` / matrix `000000XG` | Population aged 16–74 by sex, age, national background, education level and field SUN 2020; years 2019–2025 | Field of education uses SUN 2020. This table is not marked official statistics on its PxWeb page. |
| `UtbBefRegionR` / CSV name `TAB4320` / matrix `000000I2` | Population aged 16–95+ by region, education level, age and sex; years 2008–2025 | The current PxWeb page does not mark this table as official statistics. Check that its wider age coverage is needed and explain the status. |

For counts or shares, use the same reference year, region and age group in numerator and denominator. Confirm how the table handles missing/unknown education before deriving a percentage. Prefer a published share when it matches the question. Keep unknown education in the denominator only when the intended population and table definition require it; do not silently drop it.

Education level is classified under the Swedish Educational Nomenclature (SUN). SCB notes that a level may include education completed with or without a degree; doctoral education is an exception where only graduates are included. A course must cover at least one full-time term to be level-classified. The register may lack information on some foreign, private, company-internal or older education for a small number of people. A reported level is therefore the highest recorded level, not proof that every qualification is observed.

For field of education, keep the classification version in the label. SUN 2020 was introduced in UREG in 2019, replacing SUN 2000. SCB reports that the level classification remained unchanged, but some fields moved between categories. Do not join field series across versions as if the categories were identical.

Check breaks before comparing years. SCB identifies quality improvements in 1990 and 2000; comparisons across 2000 need particular caution because both SUN 2000 and new source data affected measured levels. For published series using ages 25–64 through 2022 and 25–65 from 2023, do not describe the change as a like-for-like trend unless you align the age range from the underlying table.

## RPU: study participation

RPU records participation in studies, mainly in regular education. Its register population is people registered on 31 December, ages 15–74, but published tables use different age ranges. Select the age range from the exact table, not from the product-wide description. RPU data are published for spring and autumn terms; as of 2026-10-22 the latest tables covered autumn 2024, with the next release scheduled for 2026-12-11.

Current table candidates include:

| Discovery clue | Scope | Notes |
| --- | --- | --- |
| `StudiedeltagandeK` / CSV name `TAB3732` / matrix `UF0507B2` | Population aged 16–64 by region, sex, age and study-participation type during autumn term; years 1993–2024 | Official statistics; counts; reference date 31 December. Updated 2025-12-10. |
| `StudiedeltagandeR` / CSV name `TAB3733` / matrix `UF0507B1` | Population aged 16–64 by sex, age, participation type, education level and student-aid use during autumn term; years 1993–2024 | Official statistics; counts; reference date 31 December. Updated 2025-12-10. |
| `StudiedeltagandeF` / CSV name `TAB3730` | Population aged 16–74 by sex, age, participation type, parental education and national background during autumn term; years 1999–2024 | Verify the current matrix, status and dimensions in live metadata. |

SCB classifies a person who participated in more than one study form only in the form with the highest priority. Therefore, do not sum study-form categories as if they were independent registrations. Distinguish the number of people from the number of courses, registrations, credits or full-time equivalents. If deriving a participation rate, use a denominator with the same reference year, age group, geography and population coverage, and explain any calculation.

Review the table notes for changes that affect time series or scope. Current notes include:

- For folkhögskola, the register covers long courses; 1997–1999 includes only students in Kunskapslyftet.
- Higher-education distance students' study municipality was assigned differently from 2018 after changes to institutional reporting.
- Commissioned higher education is excluded from the relevant category from 2021.
- From 2022, the Yrkeshögskola count reflects actual students after accounting for interruptions and study leave; SCB reports an approximate decrease of 5,000 due to the definition change.
- From 2024, the category “Övriga med CSN-stöd” also includes certain study-start and transition-study support recipients who are not classified in another student group.
- The treatment of doctoral students changed in 2000 and 2005; check the table note before interpreting long series.

## Search and validation

Search short Swedish phrases separately, for example `utbildningsnivå region`, `utbildningsinriktning SUN`, `studiedeltagande region`, and `studerande utbildningsnivå`. Inspect candidate titles, reference year, age range, region definition, update date and table notes. The current tables are based on registers and describe people or their recorded education/study status; do not infer attendance intensity, completed credentials, learning outcomes or intervention effects unless the selected measure directly supports that claim.

### SCB sources

- [Befolkningens utbildning (UF0506)](https://www.scb.se/uf0506)
- [Befolkningens studiedeltagande (UF0507)](https://www.scb.se/uf0507)
- [Data från Utbildningsregistret (UREG)](https://www.scb.se/vara-tjanster/bestall-data-och-statistik/register/registret-over-befolkningens-utbildning/)
- [Data från Studiedeltagande (RPU)](https://www.scb.se/vara-tjanster/bestall-data-och-statistik/register/registret-over-befolkningens-studiedeltagande/)
- [Befolkningens utbildning in Statistikdatabasen](https://www.statistikdatabasen.scb.se/pxweb/sv/ssd/START__UF__UF0506/)
- [Befolkningens studiedeltagande in Statistikdatabasen](https://www.statistikdatabasen.scb.se/pxweb/sv/ssd/START__UF__UF0507/)
