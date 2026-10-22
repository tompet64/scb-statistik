# SCB housing workflow

Use this guide for questions about where and how households live, the dwelling stock, housing space, housing expenditure and overcrowding. These are related but distinct statistical products. Search current SCB metadata before selecting a table; IDs below are discovery clues, not stable contracts.

## Route the question

| User's measure | First source to check | Statistical unit and main limit |
| --- | --- | --- |
| Household or person by housing form; household size; area per person | Hushållens boende (`HE0111`) | Annual register-based statistics on registered residents/households; housing form is classified using building type and household's arrangement for the dwelling. |
| Number and structure of dwellings, by type, construction period, ownership, tenure or floor area | Bostadsbestånd (`BO0104`) | Dwelling stock at 31 December, not the number of occupied households or residents. Standard regional levels are national, county and municipality; finer regions may require a commissioned extract. |
| Housing costs, housing-cost share, disposable income or consumption space | Hushållens boendeutgifter (`HE0202`) | Survey estimates for selected common tenure arrangements, not all households; geography and years differ by table. |
| Overcrowding | Current table in the relevant product, often the norm-2 table sourced from HE0111 | A specific definition and population, not a synonym for low area per person. Confirm building type, age, year and classification before reporting. |

Do not infer the household's actual occupancy arrangement from BO0104's dwelling-stock tenure alone. SCB notes that this tenure variable represents the ownership relationship of the dwelling rather than how residents actually use or occupy it. Conversely, HE0111's household housing form is designed to describe the household's living arrangement.

## Hushållens boende (HE0111)

Use HE0111 for the distribution of households or persons by housing form, household type, household size, housing area and related living-space measures. The household concept is a dwelling household: people registered at the same property and apartment. It differs somewhat from the household types used in register-based household statistics. Resolve the exact definition and coverage in the quality declaration for the reference year.

Useful live searches include `hushåll boendeform region`, `bostadsarea per person region`, `hushållets storlek boendeform`, and `personer boendeform ålder kön`. Current discovery candidates include tables for:

- numbers and shares of households by region, housing form and housing area (excluding special dwellings);
- average housing area per person by region, household type and housing form;
- numbers and shares of households by region, housing form and household size;
- numbers and shares of persons by region, housing form, sex, age and year.

These tables have different units and category dimensions. Select a household table for household counts or shares; do not report a person table as household distribution. The housing-area-per-person measure is an average in square metres per person, not a median, room count or overcrowding classification. Special dwellings may be excluded from a table; check its title and notes.

For housing-form categories, inspect the current metadata and documentation. Categories can combine small houses and multi-dwelling buildings with tenure, plus special dwellings and an “other” group. Missing tenure information may be included in “other.” A label such as `hyresrätt` in the housing-form data should not automatically be interpreted as first-hand rental; check the year's definition and classification notes.

Use the 31 December reference date where applicable. Review the quality declaration for missing dwelling links, coverage and any changes in definitions. In particular, SCB reports a coverage change between 2015 and 2016 when apartment records without floor-area information were added to the apartment register. Do not interpret a difference across that break as purely a change in household behavior.

From reference year 2025, SCB states that a small controlled random uncertainty has been introduced in all published HE0111 values. Treat published values as protected estimates and avoid requiring small categories to add exactly to their published total. Read the table's current footnotes for its disclosure treatment.

## Bostadsbestånd (BO0104)

Use BO0104 for the number and structure of dwellings, commonly by building type, construction period, ownership category, tenure, dwelling size and region. The reference date is normally 31 December. A dwelling includes a unit intended wholly or substantially for residential use, including dwellings in single-family houses.

Search short variants such as `antal lägenheter region upplåtelseform`, `bostadsbestånd byggnadsperiod kommun` and `lägenheter bostadsarea`. A current portal table such as `Antal lägenheter efter region, hustyp och upplåtelseform` is a candidate; resolve its current API ID, variables, years and notes. Standard regional levels are national, county and municipality. Do not promise a DeSO/RegSO or other finer breakdown from the standard table; check whether SCB requires an assignment.

BO0104 describes dwellings, not whether they are occupied, how many households occupy them, household size or residents' actual tenure. Its tenure classification is based on ownership relations. Use HE0111 for households' housing arrangements and the living population.

## Hushållens boendeutgifter (HE0202)

Use HE0202 to compare housing expenditure between selected tenure groups, expenditure as a share of household disposable income, or consumption space after housing costs. Distinguish:

- housing expenditure per household (amount and price basis as published);
- housing-cost percentage, a ratio relative to household income;
- consumption space, which depends on the product's definitions;
- disposable income per household versus disposable income per consumption unit.

The survey's main comparison population covers owner-occupied single-family houses, tenant-owned apartments and first-hand rented housing. SCB says it does not cover all households: some arrangements and contracts are excluded so the included tenure forms can be compared. State this limitation, and do not apply an HE0202 estimate to all households without support in the relevant table.

Search the current HE0202 tables for the requested statistic and cross-classifications. National tables include household expenditure and count by tenure and household type, and housing-cost percentage, disposable income and consumption space by tenure and household type or dwelling type. A regional table exists for selected years, but its period and precision differ; verify the current table and quality notes before making regional comparisons. Do not treat the older regional table ending in 2017 as a current series, and do not infer that every currently published indicator has municipal detail.

The figures are survey estimates. Report whether the table gives means or medians, the monetary unit and price basis, and the reference year. Review the quality declaration for sampling precision and any corrected years. HE0202 is related to, but not interchangeable with, household disposable-income statistics in other products: check population, household definition and income concept before joining or comparing them.

## Overcrowding and space

First ask whether the user means small floor area per person, an overcrowding norm, or the dwelling stock's average size. These are not equivalent measures. Area per person is available in HE0111, while SCB also has a norm-2 overcrowding table in the living-conditions subject area that cites HE0111 as its source. That table concerns people in multi-dwelling buildings and has its own age, geography, year and other dimensions. Check its live metadata; do not generalize its result to every person or dwelling type.

Do not use historical HEK norm-3 overcrowding tables (with reference years ending in 2013) as a current measure. If no current table matches the requested population, dwelling types and norm, state the gap instead of silently substituting a different norm or a square-metres-per-person average.

## Retrieval and answer checks

1. Parse the request into unit (dwelling, household or person), measure, housing-form or dwelling-type concept, geography, reference date/year, and breakdowns.
2. Search the live SCB table list with several short Swedish phrases. Compare table title, description, variables, period, update date, subject path and notes. A zero-result keyword search is not evidence that SCB has no relevant product.
3. Fetch detailed metadata only for the leading table or tables. Confirm category codes, units, denominators, population coverage, geographic levels, reference date, disclosure notes and default selection.
4. Choose the source that directly measures the requested concept. Do not derive household counts from dwelling stock, infer actual occupancy from ownership status, or derive overcrowding from mean area per person.
5. Estimate cells and submit the smallest valid PxWebApi v2 selection. Verify returned dimensions, codes, labels, units and period before summarizing.
6. Report the SCB product/table, statistical unit, reference period, selected geography and categories, unit and material coverage or comparability limits. Label calculated shares or cost ratios and show the numerator and denominator.

## Primary SCB references

- [Hushållens boende (HE0111)](https://www.scb.se/he0111) — product page, current documentation and tables.
- [Bostadsbestånd (BO0104)](https://www.scb.se/hitta-statistik/statistik-efter-amne/boende-bebyggelse-och-mark/bostader-och-boende/bostadsbestand/) — product scope and regional levels.
- [Hushållens boendeutgifter (HE0202)](https://www.scb.se/hitta-statistik/statistik-efter-amne/hushallens-ekonomi/hushallens-utgifter/hushallens-boendeutgifter/) — product scope and relation to income.
- [SCB's sources and definitions for housing statistics](https://www.scb.se/hitta-statistik/sverige-i-siffror/manniskorna-i-sverige/boende-i-sverige/kallor-och-definitioner/) — definitions including tenure.
