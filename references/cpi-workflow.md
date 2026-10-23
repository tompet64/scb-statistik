# SCB Konsumentprisindex workflow

Use this guide for consumer price change, inflation and indexation questions. The product is Konsumentprisindex (KPI, `PR0101`). KPI measures average price development for private domestic consumption at the prices consumers pay. It is commonly used for inflation and compensation/indexation, but the requested purpose determines the right measure.

## Choose the measure and comparison

- **KPI** is the common Swedish measure of consumer price inflation and includes changes in mortgage interest rates in owner-occupied housing costs.
- **KPIF** holds household mortgage interest rates constant. SCB identifies it as the Riksbank's inflation target measure.
- **KPIF-XE** excludes energy products from KPIF and is often used as an underlying-inflation measure.
- **HIKP** is the harmonised EU measure. Its coverage and methods differ from KPI; do not substitute it when the request explicitly concerns Swedish KPI.

Resolve whether the user asks for an index level, month-on-month change, year-on-year inflation rate, annual average or a COICOP-group contribution. State the period and calculation basis. The monthly change compares with the previous month; inflation rate normally compares with the same month a year earlier. An index level such as 125.94 is not an inflation rate of 125.94 percent.

## Shadow index and finalized KPI values

Do not treat **KPI, skuggindex** and **KPI, fastställda tal** as synonyms or as different inflation measures like KPI and KPIF. The finalized total KPI index value is formally fixed after publication for the month and is not reconsidered later; SCB says those finalized values are the ones to use when laws, regulations or contracts refer to KPI. The current month's value can appear in the table before that formal fixing has taken place.

SCB adjusts the shadow index to address certain shortcomings in the price data or calculation methods underlying the finalized values, so that the series is consistent with similarly adjusted main and subgroup indices. It differs from the finalized total index in some months. SCB calculates monthly and 12-month changes from shadow-index levels expressed to two decimals; check the published precision of the change rates separately. Therefore a percentage change may not be exactly reproduced by taking the ratio of the two-decimal finalized total indices. Compare the actual shadow and finalized levels before attributing a specific difference to shadow-index adjustments: rounding alone can explain it. This is not by itself evidence of an error or a different inflation concept.

## Find current tables and preserve classification

Search current PxWeb metadata for short phrases such as `KPI totalt månad 2020=100`, `KPI COICOP månad`, `KPIF månad` or the requested measure plus product group. Current KPI table families include total index, COICOP groups, detailed COICOP, special aggregates, finalized annual/monthly values, KPIF and HIKP. Resolve the live table ID, units, period coverage, category codes and notes; remembered IDs are discovery clues only.

From January 2026, KPI and KPIF use 2020=100 instead of the earlier 1980=100 (KPI) and 1987=100 (KPIF), and the published classification changes from COICOP 1999 to COICOP 2018. Legacy COICOP 1999 and Riksbank tables are no longer updated after December 2025. SCB supplies backcast COICOP 2018 series for 1980–2025 to support transition, but some earlier categories are model-estimated. Some inflation rates from the new backcast series can differ by 0.1 percentage point from the inflation rate officially published at the time because of rounding. For pre-2026 historical official inflation, use the series that was published for that period; for a consistent COICOP 2018 analysis, label the backcast series and its caveat.

## Indexation, income and deflators

For a contract or payment that specifies KPI indexation, use the matching total KPI index series, reference months and finalized index numbers. Confirm the contract's exact formula, reference month and rounding rule. Do not substitute KPIF, HIKP, an annual inflation rate or a preliminary index level. A generic indexation calculation is the indexed amount multiplied by the ratio of the new to the reference index; label any calculation and keep the source index values visible.

For comparisons across January 2026, distinguish originally finalized values from rebased finalized values. KPI was finalized on the 1980=100 scale through December 2025 and on the 2020=100 scale from January 2026. Use SCB's rebased finalized series to put both months on the same base; do not divide index levels with different bases. SCB specifies the conversion factor 3.3592: divide old-base finalized values by this factor to obtain the 2020 scale, or multiply new-base values to obtain the 1980 scale. Prefer SCB's published rebased values, which are rounded to two decimals, and follow the contract's specified series and rounding.

Discovery clues verified on 2026-10-23: in `TAB6596`, `ContentsCode=00000808` (finalized KPI, 2020=100) is missing for September 2025 but equals 125.94 for September 2026. In `TAB6792`, `ContentsCode=000007T9` (finalized 1980-base KPI rebased to 2020) equals 124.51 for September 2025. The ratio gives 1.148502... percent, or 1.1 percent at the published inflation rate's one-decimal precision. The shadow levels for these months are also 124.51 and 125.94, so this example demonstrates rounding, not a shadow-index adjustment. Resolve live metadata and codes again when using these tables.

When converting nominal household disposable income to a consumer-purchasing-power measure, confirm the income table's definition and price basis and use a matching time period. Prefer an officially published constant-price income series when it answers the question; if you calculate a KPI-adjusted series, state the formula and that it is your calculation. KPI does not measure household income inequality or each household's individual cost-of-living experience.

For national-accounts household-consumption volume or price analysis, use the relevant national-accounts series/deflator (such as the HUKO deflator) rather than assuming KPI is equivalent. KPI and the HUKO deflator differ in purpose, weights and treatment/coverage, particularly for housing costs. For enterprise output, turnover or value-added volume, use the appropriate industry-specific deflator or official fixed-price series, not consumer KPI by default.

## PxWebApi retrieval

1. Parse the request into measure (index/change/contribution), KPI-related measure, product group/classification, comparison period, and intended use.
2. Search the live table list with concise Swedish terms and inspect the current table descriptions, dimensions, periods, units and publication/update notes.
3. Fetch detailed metadata for the leading candidate. Verify base year, COICOP version, historical series status, group codes, finalized/preliminary status and definitions of published changes.
4. Select only the required periods and categories. Check the number of cells, retrieve values and verify the returned codes, labels and units.
5. Report whether each result is an index level, percentage change or contribution; identify the measure and period, and state any classification/backcast or price-basis caveat relevant to the request.

## Primary SCB references

- [Konsumentprisindex (KPI), PR0101](https://www.scb.se/PR0101) — tables, releases and product documentation.
- [KPI changes in classification and base year](https://www.scb.se/hitta-statistik/statistik-efter-amne/priser-och-ekonomiska-tendenser/priser/konsumentprisindex-kpi/produktrelaterat/aktuellt/kpi-byter-klassificering-och-basar/) — COICOP 2018, base-year change and backcast-series caveats.
- [2020: new base year for KPI](https://www.scb.se/contentassets/a1e257bb3a574420b9d3f2ff59851c0a/2020-nytt-basar-for-konsumentprisindex.pdf) — finalized versus rebased values, conversion factor 3.3592 and two-decimal publication of rebased series.
- [KPI and KPIF: two different inflation measures](https://www.scb.se/hitta-statistik/artiklar/2017/kpi-och-kpif-tva-olika-inflationsmatt/) — mortgage-interest treatment.
- [KPI and the HUKO deflator](https://www.scb.se/hitta-statistik/temaomraden/sveriges-ekonomi/fordjupningsartiklar_Sveriges_ekonomi/kpi-och-huko-deflatorn-ar-tva-sidor-av-samma-mynt/) — differences from national-accounts consumption deflation.
- [KPI September 2026 release](https://www.scb.se/hitta-statistik/statistik-efter-amne/priser-och-ekonomiska-tendenser/priser/konsumentprisindex-kpi/pong/statistiknyhet/konsumentprisindex-kpi-september-2026) — example of monthly versus annual changes and KPI/KPIF/KPIF-XE.
