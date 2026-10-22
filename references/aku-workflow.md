# SCB AKU workflow

Use this guide for SCB's Labor Force Surveys (Arbetskraftsundersökningarna, AKU): labor-force participation, employment, unemployment, hours, underemployment and related labor-market measures. AKU is a sample survey and follows ILO concepts. It answers different questions from administrative-register products such as BAS.

## Choose the right measure

AKU classifies people into employment, unemployment or outside the labor force using a hierarchical classification. A person who meets the employment definition is not classified as unemployed, even if also looking for another job. Unemployment follows the current ILO-based definition; check the latest SCB definitions and table notes for the exact conditions and age coverage.

Keep each measure and denominator explicit:

- **Unemployed persons**: an estimated number of people classified as unemployed.
- **Unemployment rate**: unemployed people as a share of the labor force, not the whole population.
- **Employed persons**: an estimated count under the survey's employment definition.
- **Employment rate**: employed people as a share of the population in the stated age group.
- **Labor-force participation rate**: people in the labor force as a share of the population in the stated age group.
- **Underemployment or unused labor supply**: separate measures with their own definitions; do not add counts unless the categories are documented as mutually exclusive.

Check whether the request concerns persons, rates, hours, job tenure, occupation or industry. For estimates by age, sex, country of birth, education, occupation or industry, use only dimensions that are present and reliable in the current table.

## Period, age and geography

AKU is conducted monthly. SCB publishes monthly, quarterly and annual estimates; the reference unit can be a reference week, month, quarter or annual average depending on the table. Do not substitute an annual average for a specific month. Distinguish unadjusted data from seasonally adjusted and trend-adjusted series. Use one series type consistently when comparing changes; seasonally adjusted values need not equal the raw monthly values.

Most headline statistics concern ages 15–74; some tables include people aged 75–89. Confirm the actual population and age total in the chosen table rather than applying 15–74 to every table. AKU is designed for population-level estimates, and geographic detail is constrained by sample size. Check the table's region dimension and quality notes before promising county or municipality estimates; do not derive municipal AKU counts by distributing national estimates.

## Sample uncertainty and current quality notes

All AKU estimates have sampling uncertainty. Report confidence intervals or uncertainty measures when the table provides them, and do not over-interpret small period-to-period movements. A suppressed estimate is unavailable, not zero; honor the current table's suppression thresholds and footnotes.

SCB identifies a current quality problem for education-level and field breakdowns: as of 22 April 2026, count estimates for these dimensions are dotted from 2026 Q1 retroactively to 2012. Relative estimates are not dotted under the stated method because numerator and denominator are affected similarly. Check the live table and quality note before using these dimensions; do not attempt to reconstruct or infer the suppressed counts.

AKU changed under the EU social-statistics framework from 1 January 2021, creating a series break. SCB has published linked series to support comparison across the break, but the availability and treatment are table-specific. Check the current break note and linked data for the exact measure. Do not join old and new series solely because their labels match.

## Distinguish AKU from BAS and registered unemployment

Use AKU when the question concerns the ILO-based official unemployment rate, international comparisons, or labor-market measures collected in a survey (including hours, job-seeking behavior and underemployment). Use BAS for more detailed administrative-register descriptions of registered residents and smaller geographic or demographic groups, when the BAS definition matches the question. Arbetsförmedlingen's registered jobseekers are another administrative measure.

Do not compare raw counts or rates from AKU, BAS and Arbetsförmedlingen as if they measured the same population or concept. Align age, period, denominator and geography, explain the source, and state that differences can reflect both definitions/data collection and actual labor-market conditions. A precise municipality-level count can be available in BAS even when AKU does not support that geography; this is not a reason to label BAS as an AKU estimate.

## PxWebApi retrieval

1. Search the live SCB table list with several short phrases such as `arbetslösa AKU månad`, `sysselsatta 15-74 kvartal`, `arbetskraftstal år`, or the requested measure plus a breakdown.
2. Compare table title, description, dimensions, period, frequency, season-adjustment status and notes. Table identifiers such as `TAB2892` are clues only; resolve the current ID and codes on each task.
3. Fetch detailed metadata for the leading candidate. Confirm measure, age group, sex, period, geographic dimension, units, uncertainty information, suppression and series-break notes.
4. Build the smallest valid PxWebApi v2 selection. Estimate the number of cells, retrieve data, and validate the returned codes, labels, unit and reference periods.
5. Report the table and source, unit, population/age group, period and adjustment type. Label calculated rates or changes, state the correct denominator, and describe the relevant sampling or comparability limitations.

## Primary SCB references

- [Arbetskraftsundersökningarna (AKU), AM0401](https://www.scb.se/AM0401) — product, results, tables and documentation.
- [Befolkningens arbetsmarknadsstatus (BAS), AM0210](https://www.scb.se/AM0210) — register-based labor-market statistics and links to AKU comparisons.
- [Changes in AKU](https://www.scb.se/hitta-statistik/statistik-efter-amne/arbetsmarknad/utbud-av-arbetskraft/arbetskraftsundersokningarna-aku/produktrelaterat/Fordjupad-information/forandringar-i-aku/) — series break and linked series.
- [AKU concepts and definitions](https://www.scb.se/contentassets/c12fd0d28d604529b2b4ffc2eb742fbe/begrepp-och-definitioner-i-aku.pdf) — survey concepts; confirm against current documentation.
