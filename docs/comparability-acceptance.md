# Acceptansfall: produktstöd och jämförbarhet

Dessa är beteendeacceptansfall, inte bevis för korrekta statistiska svar. Kör i separata rena sessioner med aktuell färdighet och verifierade API-råkällor. Dokumentera API-tabell-id, urval, period, källa, anrop, värden och bedömarens beslut. Strukturella offline-tester får enbart kontrollera att fallen finns och är konsekventa.

## SCB-C01 — BNP och arbetslöshet, blandat produktstöd

**Fråga:** Sammanfatta utvecklingen av BNP och arbetslöshet det senaste året.

**Förväntat:** Före alternativ BNP-sökning meddelas att specifikt dokumenterat BNP-stöd saknas (nationalräkenskapsstödet avser hushållskonsumtion). AKU stöds och ska faktiskt hämtas via PxWebApi v2 med kontrollerade metadata, ålder, period och säsongrensning. Om API inte fungerar redovisas felet; inga webbvärden utges för API-data. BNP och AKU kan analyseras som skilda konjunkturindikatorer men inte summeras. För att fortsätta med BNP utan metodguide krävs användarens medgivande.

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
