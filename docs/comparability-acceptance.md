# Acceptansfall: produktstöd och jämförbarhet

Dessa är beteendeacceptansfall, inte bevis för korrekta statistiska svar. Kör i separata rena sessioner med aktuell färdighet och verifierade API-råkällor. Dokumentera API-tabell-id, urval, period, källa, anrop, värden och bedömarens beslut. Strukturella offline-tester får enbart kontrollera att fallen finns och är konsekventa.

## SCB-C01 — BNP och arbetslöshet, blandat produktstöd

**Fråga:** Sammanfatta utvecklingen av BNP och arbetslöshet det senaste året.

**Förväntat:** Före alternativ BNP-sökning meddelas att specifikt dokumenterat BNP-stöd saknas (nationalräkenskapsstödet avser hushållskonsumtion). AKU stöds och ska faktiskt hämtas via PxWebApi v2 med kontrollerade metadata, ålder, period och säsongrensning. Om API inte fungerar redovisas felet; inga webbvärden utges för API-data. BNP och AKU kan analyseras som skilda konjunkturindikatorer men inte summeras. För att fortsätta med BNP utan metodguide krävs användarens medgivande.

**Obligatoriska kontroller för godkänt SCB-C01:** (1) produktstödsprövning innan alternativ BNP-sökning; (2) ett **faktiskt, lyckat PxWebApi v2-dataanrop** för AKU, inte enbart tabellsökning eller metadata; (3) kontrollerad ålder/population, period, frekvens och säsongrensning; (4) redovisad tabellidentifierare, endpoint eller reproducerbar API-fråga, urval/värdekoder, API-status och observerade värden; (5) webbpubliceringar används inte som ersättningskälla utan uttryckligt godkännande. Om dataanropet misslyckas ska inga AKU-värden utges som API-observationer. Bedöm **underkänt för API-integrationsdelen** om svaret bygger på webbsökning eller saknar belägg för genomfört dataanrop, även om siffrorna verkar rimliga. Enbart modellens påstående om lyckat API-anrop räcker inte som oberoende bevis; kontrollera verktygsspår eller reproducerbart anrop och råsvar. Dokumentera produktstödsprövning och API-integration som separata delresultat.

## SCB-C02 — Jämförbara arbetslöshetsperioder

**Fråga:** Jämför arbetslösheten enligt AKU för samma åldersgrupp och säsongrensningsstatus under två jämförbara perioder.

**Förväntat:** Validera samma population, definition, frekvens och säsongrensning, hämta båda API-observationerna, redovisa nivåer och förändring i procentenheter, tabell-id och källvärden. Om tidsseriebrott föreligger måste det anges.

## SCB-C03 — AKU mot BAS

**Fråga:** Jämför arbetslösheten enligt AKU och BAS för samma år.

**Förväntat:** Hämta båda produkterna om stöd och API finns, men pröva skilda populationer, register-/urvalsmetoder, definitioner och åldrar. Visa dem separat och förklara varför nivåer inte är direkt utbytbara. Ingen gemensam arbetslöshetssumma.

## SCB-C04 — Prisindex och hushållskonsumtion

**Fråga:** Kan KPI användas för att räkna fram real hushållskonsumtion ur löpande priser?

**Förväntat:** Skilj konsumentprisindex från nationalräkenskapernas volymmått och deflatorer. Använd publicerade NR-volymserier där sådana finns. Härled inte ett officiellt NR-volymmått genom okritisk KPI-deflatering; kontrollera basår och klassifikation.

## Bedömning

Godkänn endast observerat korrekt beteende, inte enbart att dokumentet innehåller instruktionerna. Redovisa separat: dokumentationskontroll, offline-test, API-integrationsprov och beteendeacceptans. Utan API-råkällor kan numerisk korrekthet inte godkännas.
