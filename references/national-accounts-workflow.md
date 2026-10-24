# SCB nationalräkenskaper workflow

Use this guide for national household final consumption expenditure by COICOP purpose within `NR0103` (Nationalräkenskaper, kvartals- och årsberäkningar). This first scope covers consumption, not a complete GDP or sector-accounts workflow. Live table discovery, metadata and small data extracts were checked on 2026-10-24; the three current tables below were updated on 2026-08-28. Resolve IDs, codes, coverage and notes again for each request.

## Select the source and frequency

| Need | Current discovery clue | Metadata checked on 2026-10-24 |
| --- | --- | --- |
| Annual expenditure, detailed purposes, prices or volumes | `TAB6332`, legacy `NR0103ENS2010T03NAN` | 1950–2024 overall coverage; 154 categories; `AndamalCOICOP`, `ContentsCode`, `Tid`; fixed-price reference year 2020. Check missing values for the particular category/year. |
| Actual quarterly expenditure or year-on-year volume change | `TAB6330` | 1980K1–2026K2; 19 categories; `Andamal`, `ContentsCode`, `Tid`; fixed-price reference year 2025. |
| Quarter-on-quarter consumption development | `TAB6331`, legacy `NR0103ENS2010T14KvN` | 1981K1–2026K2; 19 categories; seasonal adjustment `SesOnly`, not calendar adjustment; fixed-price reference year 2025. |

Search short Swedish phrases such as `hushållens konsumtionsutgifter ändamål` and screen the subject path for `NR0103`. Archived `NR0101` results include ENS95 and COICOP 1999 series. Do not choose them solely for longer history or similar titles. The annual table currently ends earlier than the quarterly tables: if a full year is needed from quarterly data, retrieve all four actual quarters and label the result as a quarterly-derived annual total with its revision status; do not call it a published annual-table observation. Never annualise a partial year silently.

## Resolve population, purpose and denominator

These are national accounting aggregates of expenditure flows during a year or quarter. They are not counts of households, household medians or survey estimates for income deciles. The checked tables have no regional or household-type dimension. Route regional household income to the regional-accounts guide and distributional income to the income guide.

- Distinguish households `S14`, household non-profit institutions `S15` (HIO), and their combined `S14S15` total. A category labelled “total konsumtion” includes HIO here; do not silently use it as the household-only denominator.
- The purpose groups describe consumption in Sweden before the separately unallocated cross-border adjustments. `CP15` adds households' consumption abroad; `CP16` removes foreign visitors' consumption in Sweden and is already negative in the checked current-price extracts. Preserve the published sign; do not subtract a negative value a second time.
- Quarterly tables publish `CP01TCP13` (summa ändamålsfördelat). The annual table lacks that aggregate in the checked metadata. If needed, sum only the 13 mutually exclusive top-level groups `CP01`–`CP13` in current prices, verify completeness, and cross-check against `S14 - CP15 - CP16`. Never sum every category: parents and children overlap.
- For transport, start with `CP07` and inspect its children. COICOP 2018 includes `CP071` vehicle purchases, `CP072` operating costs, `CP073` passenger services and `CP074` transport services for goods. Do not equate this group with public transport, transport-industry turnover or government transport spending.
- For a purpose-composition share, use `100 * CP07 / CP01TCP13` or the verified annual main-group sum in current prices. For an explicitly requested ratio to household total `S14`, calculate and label that different ratio; explain that the numerator excludes the unallocated cross-border adjustments. It is not an exact resident-household transport budget share. `CP07 / S14S15` additionally changes the sector boundary.

## Keep expenditure, prices and volumes separate

Use current-price mnkr for monetary amounts and expenditure composition. Use the published fixed-price series or volume-change measure for consumption growth; increased nominal spending alone does not establish increased volume. Consumption volume also reflects composition and quality, not simply passenger journeys or vehicle kilometres. Do not substitute KPI deflation for the official national-accounts volume series.

Read the measure's label, unit, reference year, adjustment and change interval together:

- Annual `TAB6332`: `000007EJ` current-price mnkr; `000007EI` fixed-price mnkr, reference 2020; `000007EK` price change percent; `000007EL` volume change percent.
- Actual quarterly `TAB6330`: `0000079J` current-price mnkr; `0000079H` fixed-price mnkr, reference 2025; `0000079K` volume change against the same quarter a year earlier.
- Seasonally adjusted `TAB6331`: `0000079L` fixed-price mnkr, reference 2025; `0000079M` volume change against the previous quarter. `0000079O` is labelled current-price mnkr but its metadata unit says `procent`. Flag this inconsistency and verify against SCB's table description or obtain clarification; do not silently present the levels as percentages. Prefer the unambiguous actual table for expenditure levels.

National accounts use chain-linked volume series. Components are generally not additive; use the published aggregate for volume analysis, and current-price values for composition shares. Do not force component sums to match, calculate ordinary expenditure shares from chain-linked levels, or splice annual 2020-reference levels directly to quarterly 2025-reference levels. A reference-year difference is distinct from a classification change.

## Comparability, uncertainty and interpretation

National accounts introduced COICOP 2018 in the publication on 2024-05-30; KPI introduced it in January 2026. Do not transfer KPI's transition date to NR or assume identical category codes and coverage across products. Prefer a current internally consistent series; inspect correspondence tables and backcasting notes before combining vintages or classifications.

The 2026-08-28 correction affects the purpose/durability distribution for quarterly 2022–2024 and annual 2024, but not total household expenditure. Re-fetch revised data before interpreting differences from older reports. Annual and quarterly published change rates may differ slightly through calculation rounding. Record the data vintage and any preliminary/final status; table coverage alone does not prove finality. The checked metadata do not provide confidence intervals; do not invent them or interpret their absence as absence of estimation uncertainty. Treat suppression/missing values as missing, not zero.

Aggregate consumption does not measure low-income households' affordability, essential transport needs or unmet demand. Do not infer that all groups are better off from rising consumption or falling expenditure shares. Refer distributional questions to suitable household-budget and income sources and check their reference years and coverage. Distinguish NR expenditure from actual individual consumption, which also includes relevant publicly financed individual services, and from the separate short-term household consumption indicator; do not splice those products automatically.

## Report and verify

State table ID/title, extraction/update date, reference period, codes/labels, sector/geographic coverage, units, price reference year, adjustment and denominator. Identify calculated shares and growth separately from published measures. Before claiming a successful answer, verify the response dimensions and missing/status values, check the accounting identity in current prices where applicable, and separate live API checks from offline structural checks and independent model tests. Use the NR acceptance cases for dated numerical checks; revalidate revised observations rather than treating them automatically as regressions.

## SCB sources

- [NR0103 product and current table list](https://www.scb.se/hitta-statistik/statistik-efter-amne/nationalrakenskaper/nationalrakenskaper/nationalrakenskaper-kvartals-och-arsberakningar/)
- [Annual metadata, TAB6332](https://statistikdatabasen.scb.se/api/v2/tables/TAB6332/metadata?lang=sv)
- [Actual quarterly metadata, TAB6330](https://statistikdatabasen.scb.se/api/v2/tables/TAB6330/metadata?lang=sv)
- [Seasonally adjusted metadata, TAB6331](https://statistikdatabasen.scb.se/api/v2/tables/TAB6331/metadata?lang=sv)
- [National-accounts concepts, including reference-year prices and actual consumption](https://www.scb.se/hitta-statistik/statistik-efter-amne/nationalrakenskaper/nationalrakenskaper/nationalrakenskaper-kvartals-och-arsberakningar/produktrelaterat/Fordjupad-information/begreppsforklaringar-inom-nationalrakenskaperna/)
- [COICOP transition notice](https://www.scb.se/contentassets/66e9dae3a5d94bf8b4c299ce25294348/extrainsatt-publicering-av-nationalrakenskaperna-16-maj-2024.pdf)
- [Separate household-budget product, HUT](https://www.scb.se/hitta-statistik/statistik-efter-amne/hushallens-ekonomi/hushallens-utgifter/hushallens-utgifter-hut/)
