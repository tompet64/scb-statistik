# SCB regionalräkenskaper workflow

Use this guide for regional economic output, household income, wages, employment and investment. The table names, years and identifiers below were checked in SCB's live PxWeb pages on 2026-10-22. Resolve current metadata and notes on every request; treat IDs as discovery clues.

## Choose the measure and geographic level

Regionalräkenskaper are the regional counterpart of the national accounts and follow ENS2010. They include gross regional product (BRP), average employment, wages, fixed gross capital formation and household disposable income. Use the measure that matches the question:

| User's question | Measure and starting table | Main interpretation |
| --- | --- | --- |
| Economic output/growth by county or NUTS region | `NR0105ENS2010T01A`, CSV `TAB3138`, matrix `NR0105AH` | BRP, employment and wages by county/riksområde, years 2000–2024. |
| BRP by municipality | `NR0105ENS2010T06A`, CSV `TAB3143`, matrix `NR0105AW` | BRP and per-capita/per-employed measures by municipality, years 2012–2024. |
| Household disposable income by county/riksområde | `NR0105ENS2010T02A`, CSV `TAB3139`, matrix `NR0105AN` | ENS2010 household-sector transactions by region, years 2000–2024. |
| Household disposable income by municipality | `NR0105ENS2010T02B`, CSV `TAB3463`, matrix `000001ZT` | Same concepts at municipality level, years 2000–2024. |
| BRP by sector | Search the current regional-accounts tables for the requested SNI breakdown and geography; available sector detail differs by table. | County and municipal tables do not necessarily provide the same industry detail. |
| Fixed gross capital formation | Current table for riksområden by SNI. | This product is not available at municipality level in the current annual table listing. |

SCB's latest published year as of 2026-10-22 is 2024; preliminary 2025 regional accounts are scheduled for 2026-12-17. Do not describe 2024 as final unless the live metadata or release says so. Current PxWeb pages identify the principal tables above as official statistics and use calendar year as reference period. The county BRP table has BRP in current-price mnkr, volume change in percent, BRP per resident and per employed person in current-price tkr, average employed persons in thousands, and total wages in current-price mnkr. It also marks seasonal and calendar adjustment as unavailable.

## Keep production, income and distribution separate

- **BRP** allocates value added to where production occurs. It is the regional counterpart to GDP, not the income of residents living in the region.
- **BRP per resident** divides production assigned to a region by its population. Commuting can make this ratio high in regions with many inbound workers or low in regions with outbound workers. It is not a household-income or welfare measure.
- **BRP per employed person** also relates regional production to jobs located there. Treat it as a broad ratio, not a clean measure of worker productivity; hours worked, industry mix and the employment denominator matter.
- **Household disposable income in regional accounts** is an aggregate for the household sector allocated to residents of the region. The tables show current-price totals in mnkr and current-price tkr per resident, split into national-accounts transaction posts. It is not a mean/median for individual households, equivalised income, an income distribution, or the same product as SCB's register-based household-income tables. Use the household-income guide when the user asks about household types, median, economic standard, income classes, or distribution.
- Per-capita income is not adjusted for age, household composition, prices across regions or differences in local living costs. The regional accounts tables are nominal/current-price series; do not describe their growth as real income growth without a suitable deflator and explicit method.

## Select tables and interpret change

Search short terms separately, such as `regionalräkenskaper BRP region`, `BRP kommun`, `hushållens disponibla inkomster region`, `lönesummor region`, or `fasta bruttoinvesteringar region`. Screen subject path, measure, geography, years, unit, price basis and notes. A title match alone is not enough; the regional-accounts tables may be confused with register-based income tables, municipal accounts, or other employment statistics.

For BRP:

- Use the volume-change series in fixed prices for real growth. The levels for BRP and BRP-per-person ratios are in current prices; do not infer a volume change by subtracting nominal levels.
- Use contribution to national GDP growth only when the table or release publishes it. It is a percentage-point contribution, not the region's own growth rate.
- SCB states that the sum of regional BRP equals national GDP by definition. When reconstructing totals from downloads, check that units, regions and years match and account for rounding before flagging a discrepancy.

For household disposable income:

- Use the directly published per-resident measure for regional average comparisons; do not derive it from a separately retrieved household total and a population table unless the reference population and calculation are documented.
- The transaction dimension contains components such as operating surplus and mixed income, compensation of employees, received/paid property income, primary-income balance, social benefits, current taxes/social contributions, other transfers, and net disposable income. Component sums may not match the published net total exactly after revisions/rounding; retain the direct total.
- These regional-account totals do not show how income is distributed across residents or households. They cannot answer poverty, median-income or inequality questions.

## Comparability and revisions

- Do not splice ENS95 historical tables to ENS2010 current tables as if the level series were seamless. Confirm a documented bridge or present the series separately. A classification/system change or rebasing can alter both levels and historical values.
- The 2026 release adds 2024 and reports the annual county BRP table from 2000 and municipal BRP from 2012. Older tables labelled ENS95 are archived products, not automatic extensions of the current series.
- The current BRP table has a note that the national accounts mini-review released in May 2025 changed GDP and component levels and therefore affected regional accounts. It also notes revisions to much of the source data for regional value added in 2022. Check release and table footnotes before interpreting changes around or since 2022.
- The household disposable income tables were corrected on 2026-06-26 for 2022–2024. Re-fetch current observations; do not preserve values from an earlier extract as current truth.
- Treat annual regional-accounts observations as revisable. Record publication/update date and preliminary/final status when making comparisons. If two values differ from a prior report, check revision notes before attributing the change to economic activity.

## Report

State the table title and current matrix/table ID, region and geographic classification, measure, period, current/constant-price basis, unit, and release/update status. Explain whether the value describes production at workplaces or income accruing to resident households. Flag per-capita denominators, commuting effects, revisions, system breaks, and limits on interpreting the measure as welfare or productivity.

### SCB sources

- [Regionalräkenskaper (NR0105)](https://www.scb.se/nr0105/)
- [BRP, sysselsatta och löner by län/riksområde (NR0105ENS2010T01A)](https://www.statistikdatabasen.scb.se/pxweb/sv/ssd/START__NR__NR0105__NR0105A/NR0105ENS2010T01A/)
- [BRP by municipality (NR0105ENS2010T06A)](https://www.statistikdatabasen.scb.se/pxweb/sv/ssd/START__NR__NR0105__NR0105A/NR0105ENS2010T06A/)
- [Household disposable income by län/riksområde (NR0105ENS2010T02A)](https://www.statistikdatabasen.scb.se/pxweb/sv/ssd/START__NR__NR0105__NR0105A/NR0105ENS2010T02A/)
- [Household disposable income by municipality (NR0105ENS2010T02B)](https://www.statistikdatabasen.scb.se/pxweb/sv/ssd/START__NR__NR0105__NR0105A/NR0105ENS2010T02B/)
- [SCB's 2024 release](https://www.scb.se/hitta-statistik/statistik-efter-amne/nationalrakenskaper/nationalrakenskaper/regionalrakenskaper/pong/statistiknyhet/regionalrakenskaper-2024/)
- [Quality declaration and documentation](https://www.scb.se/nr0105/#Dokumentation)
