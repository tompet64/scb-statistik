# Statistical acceptance cases for scb-statistik

Use these cases alongside the existing offline document checks, not as a replacement for them. Numeric reference values in the household, commuting and migration cases were retrieved from SCB PxWebApi v2 on **2026-10-22**. Regional-accounts case R1 instead uses the values in SCB's published 2024 release, cited in that case. References are dated published values, including disclosure protection where applicable; revisions must be reviewed rather than treated automatically as regressions. BAS case B1 is a source-selection and interpretation check without a frozen numeric value; record the live API response during its acceptance run.

## Run and assess

Run the question in a fresh conversation with the skill under review and access to SCB. Give the answering assistant the question and the skill, not the reference answer. Record the skill commit, model, date, API selections, source responses and final answer. Assess the answer only after execution against the reference below and current metadata. Repeat important cases with different wording before claiming stable behavior.

Require the correct statistical unit/population, measure, geography/direction, reference period, units and interpretation. A correct number with a materially wrong meaning fails. Mark blocked source access as unverified, not passed. Separate structural checks, live API behavior and model-answer quality in the result.

## Household questions

### H1 — Household count, population and coverage

**Question:** Hur många hushåll fanns i Malmö vid utgången av 2025? Omfattar hushållsuppgifterna alla Malmöbor, och hur stora är hushållen i genomsnitt?

**Reference:** `TAB4374`, `Region=1280`, `Tid=2025`; `ContentsCode=000000M4` 174 327 households; `000000MH` 367 924 residents; `000000MG` 366 317 residents with household information; `000000M3` published coverage 99.6 percent; `000000M5` published mean 2.10 persons per household. Reference date: 31 December. Explain incomplete coverage. Use the published mean based on people with household information, not all residents divided by households. Treat the 2025 values as CKM-protected.

### H2 — Household types and non-additivity

**Question:** Redovisa Malmös hushållstyper 2025 och kontrollera att de summerar till totalen.

**Reference:** `TAB6568`, `Region=1280`, `Tid=2025`, `ContentsCode=000007Y1`:

| Type code | Published households |
| --- | ---: |
| SBMB | 35 340 |
| SBUB | 34 402 |
| ESMB | 13 829 |
| ESUB | 77 363 |
| OVRIGA | 13 392 |
| TOTALT | 174 327 |

The five components sum to 174 326. Retain the directly published total and explain that non-additivity is consistent with CKM. Do not invent a with-/without-children subdivision of OVRIGA or call this discrepancy proof of an API error.

### H3 — Children and geographic comparability

**Questions:** Kan hushåll med barn i TAB6568 tolkas som hushåll med barn under 18 år? Kan ett DeSO jämföras direkt mellan 2023 och 2025?

**Reference:** The table's child definition has no general age limit; an under-18 question requires an appropriate age breakdown in another table. DeSO 2025/RegSO 2025 applies from reference year 2024; check boundaries and correspondence before comparing individual areas. No numeric under-18 answer or area-specific time series has been validated by this case. Earlier years in TAB6568 also have CTA disclosure treatment.

## Commuting questions

### C1 — In-/out-commuting and direction

**Question:** Hur många pendlade in och ut ur Malmö, Lund och Helsingborg 2024, och vad var pendlingsnettot?

**Reference:** `TAB1828`, `Kon=1+2`, `Tid=2024`; `000000QI` in, `000000QJ` out, `000000QK` resident/workplace in the same municipality:

| Municipality | In | Out | Same municipality | Calculated in minus out |
| --- | ---: | ---: | ---: | ---: |
| Malmö (1280) | 82 903 | 51 969 | 127 748 | +30 934 |
| Lund (1281) | 43 571 | 24 986 | 35 807 | +18 585 |
| Helsingborg (1283) | 28 426 | 22 970 | 49 485 | +5 456 |

Report employed people aged 15–74, not trips. Label the net as calculated from published values. Do not require exact additivity under disclosure protection.

### C2 — Workplace direction versus actual journeys

**Questions:** Hur många bor i Malmö och arbetar i Lund, och hur många bor i Lund och arbetar i Malmö 2024? Hur många arbetsresor per dag motsvarar detta?

**Reference:** `TAB1830`, `Kon=1+2`, `ContentsCode=000000QT`, `Tid=2024`; residence 1280/workplace 1281 gives 13 493; residence 1281/workplace 1280 gives 12 898. Daily journeys cannot be determined from these employed-person counts. Do not multiply by two or by working days without explicitly requested and supported modelling assumptions.

### C3 — Denominator and method break

**Questions:** Hur stor är utpendlingsandelen? Kan förändringen 2023–2024 tolkas som en ren förändring i pendlingen?

**Reference:** Require employed resident population with the same year, ages and coverage; check treatment of people working abroad. The entire municipal population and workplace population are wrong denominators. An out/(out+same municipality) calculation is conditional on those categories covering the intended population; the complete denominator and cross-border coverage are not certified by this case. Flag the 2024 change in classification of entrepreneurs and assignment of people without a linked workplace to their residence municipality. Do not attribute a measured change entirely to real travel behavior.

## Migration questions

### M1 — Table transition, direction and international shares

**Question:** Hur förändrades Malmös in- och utflyttningar mellan 2024 och 2025? Hur stor andel kom från respektive gick till utlandet?

**Reference:** `Region=1280` in both tables:

| Measure | TAB1212 code / 2024 value | TAB6640 code / 2025 value |
| --- | --- | --- |
| Inflyttningar | BE0101AU / 23 981 | 0000086B / 22 434 |
| Utflyttningar | BE0101AV / 22 327 | 0000086F / 22 101 |
| Invandringar | BE0101AX / 6 956 | 00000869 / 5 866 |
| Utvandringar | BE0101AY / 6 281 | 00000867 / 5 627 |
| Flyttningsöverskott | BE0101AZ / +1 654 | 00000868 / +333 |

For the older table, `Alder=tot` with `Kon` omitted returned an all-sex aggregate (verify the response). For the newer table, the explicit total selection was `Alder=TOT1`, `Kon=TotSa`. Resolve live codes rather than copying these indefinitely. Avoid adding overlapping age classifications or totals.

Calculated incoming international share: approximately 29.0 percent in 2024 and 26.1 percent in 2025; outgoing international share: 28.1 and 25.5 percent. Use all in-/out-movements as denominators; these already include international movements. Label derived shares and the introduction of CKM in 2025. Do not claim they are separately published exact rates.

### M2 — Protected totals

**Question:** Stämmer summan av inrikes och utrikes flyttningar med Malmös totaler 2025?

**Reference:** `TAB6640` with the same explicit totals as M1: inrikes in (`0000086D`) 16 571 plus immigration 5 866 gives 22 437 versus published in 22 434. Inrikes out (`0000086E`) 16 470 plus emigration 5 627 gives 22 097 versus published out 22 101. Inrikes net (`0000086C`) 101 plus international net (`0000086A`) 239 gives 340 versus published total net 333. Explain CKM; retain directly published totals. Do not impose an invented universal tolerance or require these same differences in future releases.

### M3 — Combined geographical boundary

**Question:** Kan jag summera Malmös och Lunds inflyttningar för att få inflyttningen till deras gemensamma område?

**Reference:** No. Moves between member municipalities are internal to their combined area but included in municipal gross flows. Use a directly published region or suitable origin-destination data excluding internal moves. The problem exists independently of CKM; municipal marginal totals alone cannot identify the required external inflow.

## API controls and future automation

Observed on 2026-10-22:

- Omitting Hushallstyp in a filtered TAB6568 request for Malmö, 2025, household count yielded one observation, 174 327.
- Omitting both Alder and Kon in a filtered TAB6640 request for Malmö, 2025, inflyttningar yielded one observation, 22 434, equal to the explicit total selection.
- TAB1212 with Tid=2025, TAB6640 with ContentsCode=BE0101AU, and TAB1212 with Kon=1+2 each returned HTTP 400, Non-existent value. Do not apply a code from another subject or release silently.
- Search `Flyttningar efter region` returned zero candidates; `flyttningar region` found TAB1212 and TAB6640 among 14 candidates. Search `antal hushåll region` returned 156 candidates on two pages. Simplify empty searches and follow pagination.

Keep `tests/test_scb_skill.py` and its network block intact. Reuse fixtures and checks in `tests/test_pxapi.py` for client request/error handling, cell estimates and JSON-stat conversion when extending actual executable code. Future live checks should be separately opt-in and distinguish source unavailability, changed metadata and revised observations. A fixture test of client code does not establish that an assistant chooses or explains the statistic correctly; retain independent model acceptance for that claim.

## BAS questions

### B1 — Administrative labor-market status versus AKU

**Question:** Hur många arbetslösa personer fanns i Malmö kommun i december 2025, och kan siffran jämföras direkt med AKU:s arbetslöshetstal?

**Reference:** Resolve the current preliminary monthly BAS table and its live metadata. Select Malmö municipality, reference month 2025M12, the table's total-age category matching its population (generally registered residents aged 15–74), and the BAS status `arbetslös`. Report a count in persons, identify the value as preliminary BAS, and explain that it is not directly comparable with AKU's ILO unemployment measure or Arbetsförmedlingen's registered-unemployed count. Check the latest revision notice for the selected observation. This case tests source, population and measure selection; record the API response, current table ID and returned value when performing a live acceptance run rather than freezing a value in this document.

## Education questions

### E1 — Highest recorded education

**Question:** Hur många personer i Uppsala län i åldern 16–74 år hade eftergymnasial utbildning om minst tre år 2025, uppdelat efter kön?

**Reference:** Resolve the current UREG table and live category codes. `Utbildning` / `TAB3981` / matrix `UF0506A1` is a current candidate with region, age, education level, sex and year. Select Uppsala län, the table's 16–74 total if present, the matching SUN level, women and men, and 2025. Return counts in persons and identify the 31 December reference date. If the exact age total is absent, use only a documented, non-overlapping aggregation or explain that the requested cut is unavailable. Record the actual API table ID, codes and response when running this case; no frozen count has been independently verified here. The answer must not imply every foreign, private, company-internal or older qualification is necessarily observed.

### E2 — Participation in studies during a term

**Question:** Hur många personer i Västra Götalands län i åldern 16–64 år deltog i högskoleutbildning under höstterminen 2024, uppdelat efter kön?

**Reference:** Resolve the current RPU table and live category codes. `StudiedeltagandeK` / `TAB3732` / matrix `UF0507B2` is a current candidate with region, sex, age, study-participation type and year. Select Västra Götalands län, the 16–64 total if present, the category for higher education and 2024. Return people, not registrations or course instances, and identify the observation as autumn-term participation with reference date 31 December. Record the actual API table ID, selected codes and response when running this case; no frozen count has been independently verified here. If a person can be assigned to only one study type, do not sum the categories as separate enrollments.

## Regional accounts questions

### R1 — Regional production versus resident household income

**Question:** Jämför Stockholms och Hallands län 2024 med avseende på BRP per invånare, BRP per sysselsatt och hushållens disponibla inkomst per invånare. Vilket mått beskriver bäst invånarnas inkomster?

**Reference:** Resolve the current ENS2010 tables and confirm region, measure, year and price basis. `NR0105ENS2010T01A` / CSV `TAB3138` / matrix `NR0105AH` is the county/riksområde BRP table; `NR0105ENS2010T02A` / CSV `TAB3139` / matrix `NR0105AN` is the household-income table. For 2024, [SCB's official release](https://www.scb.se/hitta-statistik/statistik-efter-amne/nationalrakenskaper/nationalrakenskaper/regionalrakenskaper/pong/statistiknyhet/regionalrakenskaper-2024/) publishes (current-price tkr):

| Measure | Stockholm | Halland |
| --- | ---: | ---: |
| BRP per resident | 858 | 460 |
| BRP per employed person | 1 506 | 999 |
| Household disposable income per resident | 332 | 292 |

BRP is production located in the region; per-resident BRP is influenced by commuting and is not resident income. Household disposable income per resident is the closest of these three to average resident household-sector income, but it is not a median, distribution, equivalised standard or direct measure of every household's income. Values are in current prices. The 2024 release is published 2026-06-24; check the live table and note revisions before using values in a later rerun.

### R2 — Municipal coverage, units and revisions

**Question:** Vilken SCB-tabell kan visa BRP respektive hushållens disponibla inkomster för Växjö kommun 2024, och kan jag jämföra inkomstökningen 2022–2024 i fasta priser?

**Reference:** The current municipal BRP candidate is `NR0105ENS2010T06A` / CSV `TAB3143` / matrix `NR0105AW` (2012–2024). The municipal household-income candidate is `NR0105ENS2010T02B` / CSV `TAB3463` / matrix `000001ZT` (2000–2024). Both include current-price totals and current-price tkr per resident; do not report these as constant-price series. The household-income table notes that 2022–2024 were corrected on 2026-06-26, so values must be retrieved from current metadata. If a real income change is requested, explain that the current regional-accounts table does not supply a fixed-price household-income series; do not call nominal growth real growth or silently substitute BRP volume change.

## Housing and dwelling questions

### HOU1 — Household housing form versus dwelling stock

**Question:** Hur många hushåll i Uppsala kommun bodde i småhus respektive flerbostadshus 2025, och hur många bostadslägenheter av respektive hustyp fanns där?

**Reference:** Resolve a current HE0111 household table and a BO0104 dwelling-stock table from live metadata. Return households from HE0111 and dwellings from BO0104, each for Uppsala municipality and reference year 2025, with the exact requested building-type categories and published units. These counts are different statistical units and must not be equated. State that HE0111 describes households' housing form, while BO0104 counts dwellings in the stock; BO0104's tenure classification is based on ownership relations, not actual household occupancy arrangements. Record live table IDs, category codes and values during the run; no frozen count has been independently validated here.

### HOU2 — Housing area versus overcrowding

**Question:** Vilken genomsnittlig bostadsarea per person hade hushåll i Malmö 2025, och hur många personer var trångbodda enligt norm 2 samma år?

**Reference:** Resolve the current HE0111 table for average housing area per person and the current norm-2 overcrowding table from live metadata. Report square metres per person as an average, and the overcrowding measure in persons using its published definition. Confirm whether the norm-2 table includes only residents of multi-dwelling buildings and verify its age and geography dimensions. Do not infer the number of overcrowded persons from average floor area, substitute an old HEK norm-3 series, or generalize a multi-dwelling-building measure to all housing. Record current table IDs, selections and values; no frozen value is certified here.

### HOU3 — Housing costs and coverage

**Question:** Hur stor andel av den disponibla inkomsten gick till boendeutgifter för ensamstående med barn 2024, och kan värdet beskriva alla hushåll i Sverige?

**Reference:** Resolve the current HE0202 table and category for single-adult households with children, using the table's published housing-cost percentage and reference year 2024. Identify whether the table reports a mean or median, state the denominator as household disposable income, and include any price/reference basis specified by the table. Explain that HE0202 covers selected common arrangements (owner-occupied single-family homes, tenant-owned apartments and first-hand rentals), not all households or housing contracts. Do not substitute the household's income or an individual-level income measure. Record table ID, categories and value from the live response; no frozen value is certified here.

## AKU questions

### AKU1 — Annual labor-market indicators and denominators

**Question:** Hur många sysselsatta och arbetslösa fanns i Sverige 2025 enligt AKU, och vad var sysselsättningsgraden respektive arbetslöshetstalet?

**Reference:** Resolve the current annual AKU tables and verify the population and age group. SCB's [published 2025 annual release](https://www.scb.se/hitta-statistik/statistik-efter-amne/arbetsmarknad/utbud-av-arbetskraft/arbetskraftsundersokningarna-aku/pong/statistiknyhet/arbetskraftsundersokningarna-aku-2025/) reports 5,263,000 employed people, an employment rate of 69.0 percent, 510,000 unemployed people and an unemployment rate of 8.8 percent. Identify these as annual estimates, normally ages 15–74 in this release. State that the unemployment rate denominator is the labor force, while the employment-rate denominator is the population in the stated age group. Recheck current table values, revision notes and units during a live run; do not assume the published release and current database extract cannot differ after revisions.

### AKU2 — Education-dimension quality flag

**Question:** Kan jag ta fram antal arbetslösa i AKU efter utbildningsnivå för 2025 och jämföra grupperna?

**Reference:** Inspect the current table notes and AKU quality documentation. SCB states that count estimates by education level and education field are dotted from 2026 Q1 retroactively to 2012 because of quality problems; relative estimates are not dotted under the stated method. Do not invent, interpolate or reconstruct unavailable count estimates. Explain that other dimensions or relative measures may remain usable only if the current table and documentation support them. Record the live table and note used.

### AKU3 — AKU versus BAS and geographic detail

**Question:** Kan jag jämföra AKU:s arbetslöshetstal för Malmö kommun med BAS och AF:s inskrivna arbetslösa?

**Reference:** Resolve the current AKU geography and age dimensions and explain any unsupported municipal breakdown; do not generate a municipal AKU estimate if the table does not publish it. Distinguish AKU's ILO-based sample-survey measure from BAS's administrative-register classification and Arbetsförmedlingen's registered jobseekers. Compare only after aligning period, age, geography and denominator, and label the sources and concepts separately. A BAS municipality value cannot be presented as an AKU figure. No numeric cross-source comparison has been validated by this case.

## Företagens ekonomi questions

### FEK1 — Enterprise unit, industry and accounting measures

**Question:** Hur många företag inom transport och magasinering (SNI 49–53) fanns 2024, och vad var deras nettoomsättning, förädlingsvärde och antal anställda?

**Reference:** Resolve a current FEK table for företagsenhet and SNI 2007 from live metadata. Select the correct SNI categories covering 49–53 without double-counting totals, and the requested reference year 2024. Report the unit exactly as published (for example, average employees/full-time equivalents if indicated), financial units and current- or fixed-price basis. Explain that since reference year 2022 FEK's företagsenhet may consist of multiple legal units and is not necessarily a single registered legal company. Record live table ID, category codes and observations; no frozen values are certified here.

### FEK2 — County activity versus enterprise headquarters

**Question:** I vilket län var förädlingsvärdet störst inom transport och magasinering 2024, och visar det var företagens huvudkontor ligger?

**Reference:** Use the current regional FEK table for local verksamhetsenheter (LVE), county and the matching SNI categories. Report the table's value-added unit and price basis. Explain that this is a regional distribution of local activity, not a distribution of enterprise-level accounts by head-office location. Do not claim municipal detail from a county table or sum local-unit values to reconstruct the enterprise-unit total. Record current table, selections and values; no frozen county ranking has been independently validated here.

### FEK3 — Statistical-unit and product boundary

**Question:** Kan jag tolka förändringen i antal företag och förädlingsvärde mellan 2021 och 2022 som en direkt jämförbar utveckling, och använder Företagens ekonomi samma definition av nya och nedlagda företag som Företagens demografi?

**Reference:** Flag the 2022 change to FE, VE and LVE and check whether the exact measure has a documented comparable or linked series. State that 2022 onward enterprise units may differ from the earlier legal-unit presentation; do not assume a direct like-for-like comparison. Explain that FEK measures annual economic structure and accounting results, while enterprise births/deaths and active-firm demography belong to the separate NV1001 product with statistical responsibility assigned to Tillväxtanalys. Do not interpret aggregate FEK change as a causal policy effect.
