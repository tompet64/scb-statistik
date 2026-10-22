# SCB Företagens ekonomi workflow

Use this guide for annual statistics on the structure and financial results of Swedish non-financial businesses: enterprise counts, employees, turnover, production, value added, costs, profitability, assets, liabilities and investments. The product is `Företagens ekonomi` (FEK, `NV0109`). It is a different product from Företagens demografi (`NV1001`), whose statistical responsibility lies with Tillväxtanalys; route the latter to the planned Tillväxtanalys skill when appropriate.

## Start with the statistical unit

Since reference year 2022, FEK uses three statistical units. They answer different questions:

| Unit | Use when the question concerns | Interpretation |
| --- | --- | --- |
| Företagsenhet (FE) | Enterprise structure and financial position | A profiled enterprise, generally built from the Swedish part of a group; it may encompass multiple legal units. |
| Verksamhetsenhet (VE) | An enterprise's activity by industry | A unit created to separate different activities in an enterprise for functional industry statistics. |
| Lokal verksamhetsenhet (LVE) | Activities and results by local operating unit | A VE split across places; the standard regional FEK table reports counties and uses local units. |

An enterprise unit is not automatically one registered legal entity, one worksite or one municipality. SCB uses FE to describe institutional structure and financial statements; VE and LVE are used for functional analysis by industry and region. The observed units approximate their statistical target concepts and have a documented model error.

## Coverage and measures

FEK is an annual total survey based on multiple administrative and collected sources. Its institutional and functional populations cover Swedish non-financial businesses in the in-scope industries; check the current quality declaration for exact NACE/SNI exclusions and any table-specific coverage. Do not describe it as all Swedish organizations or as including financial enterprises.

Common measures include:

- number of enterprises or activity units;
- average employees, sometimes stated as full-time equivalents;
- net turnover, production value, consumption/input value and value added;
- operating surplus, labor costs and profitability ratios;
- gross/net investment, assets, equity and liabilities.

The concept and unit can differ between tables. In FEK, value added is related to production value less the cost of purchased goods and services used as inputs; it is not the same as turnover or profit. Employee counts may be annual averages or full-time equivalents. Read the exact variable label, unit and definition in the table metadata and current quality declaration.

## Find current tables and interpret periods

Search the live table list with short Swedish phrases such as `företag basfakta bransch`, `förädlingsvärde näringsgren`, `regionala basfakta verksamhetsenhet` or `investeringar företagens ekonomi`. Current discovery families include:

- enterprise-unit basic facts by SNI and size class;
- activity-unit basic facts and key ratios by SNI;
- local activity-unit regional basic facts by county and SNI;
- result and balance-sheet accounts by activity or enterprise unit.

Recent FEK final tables cover reference years 2022–2024. Check the publication calendar for newer preliminary or final releases before answering. Use SNI edition and detailed industry level shown by the table, not a code remembered from an older series. For example, current recent tables include SNI 2007; classification changes and revisions can affect newer releases.

From 2022 the new statistical units affect comparability with the earlier enterprise/legal-unit presentation. Large headquarters can be classified to SNI 70.100 from 2022 under new decision rules; revisions to those rules from 2023 may cause industry changes between years. Do not interpret a change around these breaks as purely economic growth without checking the current table's notes.

Report the price basis. Many financial totals are in million SEK at current prices, while certain production/value-added series also have fixed-price variants. A nominal increase is not real growth. Do not silently deflate a series using an unrelated price index or combine fixed-price and current-price measures.

Standard FEK regional results by LVE are available at county level in the current regional table; do not promise municipal values from that table. A county's LVE result describes activities at local units in that county, not all head-office financial accounts of enterprises headquartered there. Avoid summing enterprise-level data across counties or treating VE/LVE rows as distinct independent companies.

## Distinguish adjacent statistics and evaluation claims

Use FEK for annual economic structure and accounting outcomes. Use Företagens demografi for births, deaths and active enterprise population; it is a separate product under Tillväxtanalys's statistical responsibility. Use shorter-period products such as Ekonomisk statistik på kvartal for more current business-cycle changes, while checking their populations and units before comparing them with FEK.

FEK describes outcomes and structure; an industry or region aggregate does not identify a policy effect. For an evaluation, define the intervention, eligible units, comparison group, exposure and time window separately. Do not infer that a change in value added or firm counts was caused by a specific support measure from FEK alone.

## PxWebApi retrieval

1. Parse the request into unit (FE, VE or LVE), measure, reference year, industry classification/detail, size class, geography and price basis.
2. Search current metadata with several short phrases; compare table title, description, variables, periods, unit, update date and notes. Treat table identifiers and CSV labels as discovery clues, not stable identifiers.
3. Inspect detailed metadata only for the leading candidate. Verify exact SNI codes, statistical unit, variable definitions, units, fixed/current-price options, regional level, coverage, revision notes and default selections.
4. Submit the smallest valid PxWebApi v2 selection. Estimate the cell count, retrieve observations, and confirm the response's labels, category codes, units and reference years.
5. Report product/table, statistical unit, industry and geography, period, price basis and material coverage or comparability limits. Label calculated ratios and changes; do not imply causal effects.

## Primary SCB references

- [Företagens ekonomi (FEK, NV0109)](https://www.scb.se/nv0109) — current tables, releases and product documentation.
- [Description of Företagens ekonomi](https://www.scb.se/hitta-statistik/statistik-efter-amne/naringsverksamhet-och-utrikeshandel/foretagens-produktion-forsaljning-och-ekonomi/foretagens-ekonomi/produktrelaterat/Fordjupad-information/beskrivning-av-foretagens-ekonomi/) — purpose, source base and population.
- [Quality declaration, final 2024](https://www.scb.se/contentassets/9dd20ce462644cc19f6f04eb2edbbe28/nv0109_kd_slut2024_20260513.pdf) — population, statistical units, definitions, methods and quality.
- [SCB publication calendar for NV0109](https://www.scb.se/hitta-statistik/publiceringskalendern/?period=Forward1Year&prodKod=NV0109) — latest and planned reference periods.
