---
name: scb-statistik
description: Hitta, tolka, validera och hämta SCB-statistik via PxWebApi v2 och geodata. Använd för frågor om befolkning; hushållsstatistik; hushållens inkomster och ekonomiska standard; boende och bostadsförhållanden; konsumentprisindex (KPI), KPIF, HIKP, inflation och indexuppräkning; utbildning och studiedeltagande; regionalräkenskaper (BRP); nationalräkenskaper, hushållens konsumtionsutgifter, COICOP och konsumtionsvolymer; Företagens ekonomi; arbetsmarknadsstatistik från AKU och BAS; pendling; migration och flyttningar; geografi; SCB-tabeller, metadata, kategorivärden och datauttag.
---

# SCB-statistik

Använd färdigheten för att omsätta en statistikfråga på svenska till en spårbar SCB-tabell och ett giltigt urval i PxWebApi v2. Tolka frågans innebörd själv; SCB:s parameter `query` söker efter nyckelord och är inte en semantisk sökmotor.


## Kontroll av produktstöd före uttag

Identifiera samtliga efterfrågade statistikprodukter och kontrollera först om de omfattas av dokumenterat produktstöd och relevant metodguide. Om stöd saknas för en produkt, meddela användaren detta **innan** alternativ tabellsökning, webbsökning eller datahämtning för den produkten. Skilj bristande färdighetsstöd från avsaknad av statistik hos SCB. Fråga om användaren vill gå vidare utan dokumenterat metodstöd; ersätt aldrig tyst med webbuppgifter. Vid delvis stöd: redovisa gränsen, men fullfölj API-uttag för de produkter som stöds. En identifierad AKU-tabell ska således följas av ett faktiskt API-uttag och validering, inte enbart en hänvisning till statistiknyheter. Misslyckade API-anrop redovisas öppet.

## Syfte: jämförbara statistikprodukter

Färdigheten ska snabbt hitta rätt produkt, variabel, mätvärde och urval, besvara enkla frågor och möjliggöra tabeller och diagram. Den ska dessutom kunna hämta flera statistikprodukter och jämföra eller kombinera dem **endast när deras definitioner är förenliga**. Kontrollera statistisk enhet, population, geografisk täckning, referensperiod och frekvens, mätstorhet och enhet, prisbas, säsongrensning, klassifikation, metodförändringar och preliminär/slutlig status. Harmonisering genom dokumenterad omräkning eller aggregering är tillåten när den är metodologiskt försvarbar; redovisa transformation och källvärden. Kedjade volymmått, överlappande populationer och olika arbetslöshetsdefinitioner får inte summeras som om de vore jämförbara. Vid oförenlighet: visa serierna separat, förklara konkret varför direkt jämförelse eller sammanläggning är missvisande och erbjud en alternativ analys. Skilj alltid observerade värden från beräknade härledningar. Diagram får inte antyda jämförbarhet som saknas.

## Arbetsgång

1. Identifiera mått eller begrepp, population eller statistisk enhet, geografi, tidsperiod, frekvens, redovisningsgrupper och önskad enhet. Bevara användarens avsikt: exempelvis är `folkmängd` ett bestånd vid en tidpunkt, medan `folkökning` är en förändring eller ett flöde.
2. Sök i SCB:s tabellförteckning med flera korta svenska begreppsfraser, en i taget. Börja med måttet och en trolig dimension, exempelvis `folkmängd region`, och pröva sedan varianter som `befolkning kommun`, `invånare region` och `antal folkbokförda`. Parametern `query` filtrerar på nyckelord; en hel fråga på naturligt språk kan ge noll träffar. Det bevisar inte att statistiken saknas: förenkla sökningen och pröva synonymer.
3. Välj rätt källa för geografiska frågor. Sök i PxWebApi v2 efter vanliga administrativa områden och statistik i tabellform. Vid frågor om rutnät, rasterceller, hög geografisk upplösning, nedladdningsbara GIS-data eller områden som saknas i tabellmetadata, kontrollera även SCB:s öppna geodata och sidor om geografiska indelningar. Geodata kan ligga utanför PxWebApi; en tabellsökning utan träff visar inte att uppgifterna saknas. Följ `references/geodata-workflow.md`. Om lämpliga uppgifter kräver betalning, beställning eller särskild behörighet, eller annars inte kan hämtas öppet via API, förklara begränsningen och hänvisa till officiell leverantör eller beställningssida. Försök inte kringgå begränsningen eller antyda att uppgifterna är öppet tillgängliga.
4. Granska tabellförteckningens kompakta poster innan detaljerade metadata hämtas. Jämför titel, beskrivning, `variableNames`, tidsomfattning, uppdateringsdatum och ämneshierarki. Hämta fler resultatsidor när svaret anger att sådana finns. Välj inte tabell enbart utifrån liknande titel eller senaste uppdatering.
5. Ange den bästa tabellkandidaten och varför den passar. Ställ en kort följdfråga om en oklarhet skulle ändra måttet eller tabellvalet, exempelvis årsslutsbefolkning jämfört med månadsbefolkning. Fortsätt annars med ett uttryckligt antagande.
6. Hämta detaljerade metadata bara för de främsta kandidaterna. Vissa tabeller har mycket stora värdemängder, exempelvis kommuner tillsammans med DeSO- och RegSO-områden. Skriv inte ut alla kategorinamn i samtalet. Bearbeta metadata lokalt eller granska endast relevanta koder och benämningar. Om det inte är praktiskt möjligt, pröva en mer avgränsad tabell med samma mått, geografi och tidsperiod.
7. Bygg det minsta giltiga urval som besvarar frågan. För en total, granska tabellens standardurval och pröva om valfria dimensioner kan utelämnas. PxAPI v2 kan då ge ett enda aggregat utan kategorifilter. Välj och summera inte valfria kategorier i onödan. Kontrollera svarets dimensioner och värde innan beteendet används. Om svaret fortfarande innehåller en uppdelning, välj en uttrycklig totalkategori om sådan finns. Summera annars endast ömsesidigt uteslutande kategorier och först efter kontroll av noter och röjandeskyddets påverkan.
8. Kontrollera uppskattat cellantal, API-gränser, tidsomfattning, geografisk jämförbarhet och eventuella tidsseriebrott. Hämta data först när urvalet är giltigt.
9. Redovisa tabelltitel och tabell-id, referensperiod, tillgängligt uppdateringsdatum, valda kategorier och enhet. Länka till SCB-tabellen eller API-uttaget när det går. Skilj statistikuppgifter från din tolkning av användarens avsikt.

## Grundmetod: Befolkning

Avgör först om en fråga om befolkning eller invånare avser:

- folkmängd vid en tidpunkt, vanligen vid årets slut;
- aktuell folkmängd eller månadsbefolkning, om den senaste uppgiften efterfrågas;
- folkökning, födda, döda, flyttningar eller andra flöden.

För årlig kommun- eller länsbefolkning, sök aktuella API-tabeller med exempelvis `folkmängd efter region år` och kontrollera metadata och regiondimension. Den välkända tabellen `Folkmängden efter region, civilstånd, ålder och kön` är en sökledtråd, inte ett garanterat stabilt tabell-id. Välj rätt tidsomfattning och detaljnivå och kontrollera ändrade kommungränser och regionkoder. Om användaren frågar efter det senaste, jämför referensperiod och uppdateringsdatum och överväg en månadstabell. Ersätt inte årlig årsslutsbefolkning med månadsdata utan att ange det.

Pröva separata sökningar med `befolkning`, `invånare`, `folkmängd` och `antal folkbokförda`, tillsammans med efterfrågad geografi och år. Förvänta dig inte att en enda sökning förstår hela frågan.

## Grundmetod: Hushållsstatistik

Skilj hushåll från personer, familjer och hushållsmedlemmar samt från hushållstyp, hushållsstorlek och boendeform. Använd `references/household-workflow.md` för SCB:s hushållsdefinition, årliga uppgifter vid årets slut, täckning, geografiska tidsseriebrott och röjandeskydd. För disponibel inkomst och ekonomisk standard, använd `references/income-workflow.md` och skilj hushållets totalinkomst från personers ekonomiska standard per konsumtionsenhet.

## Grundmetod: Hushållens inkomster

Avgör om frågan gäller hushållets disponibla inkomst, en persons disponibla inkomst eller ekonomisk standard per konsumtionsenhet. Använd `references/income-workflow.md` för aktuellt tabellval, prisnivå, hushållspopulation, inkomstdefinition och tidsseriebrott. Behandla inte preliminära månadsuppgifter om individinkomster som hushållsinkomster.

## Grundmetod: Utbildning och studiedeltagande

Skilj befolkningens högsta uppnådda utbildning enligt Utbildningsregistret (UREG, `UF0506`) från studiedeltagande under en termin enligt Registret över personer i utbildning (RPU, `UF0507`). De mäter olika saker och använder tabellspecifika åldersgrupper och referenstidpunkter. Använd `references/education-workflow.md` för tabellval, SUN-indelningar, kohorter och nämnare, studieformer och jämförbarhetsbrott. Likställ inte studenter eller studiedeltagande med kursregistreringar, avslutade examina eller utbildningseffekter.

## Grundmetod: Regionalräkenskaper

Använd `references/regional-accounts-workflow.md` för regional produktion, hushållsinkomster, löner, sysselsättning och investeringar. Välj mått och geografi först: BRP mäter produktion i regionen, medan regional disponibel hushållsinkomst avser inkomster för regionens hushållssektor. Tolka inte BRP per invånare som invånarnas inkomst eller disponibel hushållsinkomst per invånare som ett fördelningsmått. Kontrollera aktuella tabellnamn, id:n och noter i API-metadata.

## Grundmetod: Nationalräkenskaper

Använd `references/national-accounts-workflow.md` för hushållens konsumtionsutgifter på nationell nivå, utgiftsandelar och konsumtionsvolym. Det första stödet för NR0103 omfattar års- och kvartalskonsumtion efter COICOP, inte en fullständig metod för BNP eller sektorräkenskaper. Skilj ändamålsfördelade utgifter från hushållens total S14 och hushåll inklusive HIO, S14+S15. Beakta ofördelade utlandsposter. Använd löpande priser för utgiftsandelar och publicerade volymmått för tillväxt. Summera inte kedjade volymkomponenter och dra inte slutsatser om låginkomsthushållens ekonomiska överkomlighet från nationella aggregat. Kontrollera klassifikation, referensår, justeringar och revideringar för varje tabell.

## Grundmetod: Företagens ekonomi

Använd `references/enterprise-economy-workflow.md` för årliga struktur- och ekonomiska uppgifter om icke-finansiella företag och deras verksamhet. Avgör om frågan gäller företagsenhet, verksamhetsenhet eller lokal verksamhetsenhet. Från referensår 2022 är dessa skilda statistiska enheter. Matcha enhet och geografi, kontrollera SNI och revideringsnoter och skilj totaler i löpande priser från serier i fasta priser. Tolka inte företagens samlade räkenskapsuppgifter som kausala politikeffekter eller som företagsdemografiska antal.

## Grundmetod: Konsumentprisindex

Använd `references/cpi-workflow.md` för konsumentpriser, inflation och indexuppräkning. Skilj indexnivåer från månads- och årsförändringar i procent. Välj KPI, KPIF, KPIF-XE eller HIKP efter syftet. För perioder före 2026, kontrollera den serie och klassifikation som faktiskt publicerades då. År 2026 införs basår 2020 och COICOP 2018, med vissa tillbakaräknade historiska delserier. Använd fastställda indextal för avtalsreglerad indexuppräkning. Över basårsbytet 2026, använd SCB:s ombasade fastställda serier så att månaderna har samma bas, och ange vilka värden som är ombasade. Jämför de faktiska skuggindextalen och fastställda nivåerna innan en avvikelse tillskrivs skuggindexjusteringar i stället för avrundning. Använd inte KPI som automatisk deflator för konsumtionen i nationalräkenskaperna.

## Grundmetod: Boende och bostadsförhållanden

Avgör först om frågan gäller hushållens faktiska boende och bostadsyta (HE0111), bostadsbeståndets struktur (BO0104), boendeutgifter och deras förhållande till inkomster (HE0202) eller ett särskilt trångboddhetsmått. Använd `references/housing-workflow.md` för enheter, täckning, geografi, urvals- eller registerkällor och begränsningar. Behandla ihågkomna tabell-id:n som sökledtrådar och kontrollera aktuella metadata. Likställ inte beståndets upplåtelseformer med invånarnas faktiska boendeform och anta inte att boendeutgifterna omfattar alla hushåll.

## Grundmetod: BAS

Använd `references/bas-workflow.md` för den folkbokförda befolkningens sysselsättning, arbetslöshet och övriga arbetsmarknadsstatus. Skilj BAS från AKU:s arbetslöshetsmått enligt ILO och från Arbetsförmedlingens statistik över inskrivna arbetslösa. Matcha ålder, geografi och preliminär eller slutlig status innan perioder jämförs.

## Grundmetod: AKU

Använd `references/aku-workflow.md` för Arbetskraftsundersökningarna (AKU). Behandla AKU som en urvalsundersökning med ILO:s arbetskraftsbegrepp, inte som en administrativ totalräkning. Matcha åldersgrupp, period, ojusterad eller säsongrensad serie, statistiskt mått och geografi. Beakta skattningsosäkerhet, tidsseriebrottet 2021 och aktuella tabellspecifika kvalitetsnoter.

## Grundmetod: Pendling

Skilj antalet sysselsatta personer klassificerade efter bostads- och arbetsställekommun från faktiska resor, resfrekvens, avstånd, färdväg och färdsätt. Använd `references/commuting-workflow.md` för riktning, aktuellt årsregister, metodnoter och begränsning av stora uttag mellan start- och målområden. Behandla tabell-id:n som `TAB1830` som sökledtrådar och kontrollera aktuella metadata vid varje uppgift.

## Grundmetod: Migration

Skilj folkbokförda flyttningar från resor och tillfällig rörlighet. Avgör om frågan gäller samtliga in- eller utflyttningar, inrikes flyttningar, invandring, utvandring eller flyttnetto. Använd `references/migration-workflow.md` för tabellval, komponenternas innebörd, uppdelade tidsserier och röjandeskydd. Hämta aktuella tabell-id:n och värdekoder från metadata. Anta inte att koder är identiska mellan närliggande tabeller.

## Regler för API och klienter

- Läs `references/PxAPI-2.yml` för det inkluderade API-kontraktet. Det är en ögonblicksbild av den officiella OpenAPI-specifikationen. Det aktuella API:et och tabellernas metadata har företräde vid avvikelser.
- Vanlig basadress för SCB:s v2-API är `https://statistikdatabasen.scb.se/api/v2`. Kontrollera sökvägar och parameternamn i specifikationen. GET-filtreringen använder `valuecodes` med gemener enligt denna version. POST tar emot ett JSON-objekt med urvalet.
- Om inga värden anges tillämpar dataändpunkten tabellens standardurval. Kontrollera `/tables/{id}/defaultselection` vid oklarheter. Utelämnade valfria variabler kan ge ett aggregat. Kontrollera svarets struktur; anta inte att utelämnat filter betyder vare sig alla kategorier eller totalen.
- Använd `/tables` för tabellsökning, `/tables/{id}` för kompakta tabellmetadata, `/tables/{id}/metadata` för dimensioner, kategorivärden och noter samt `/tables/{id}/data` för observationer. Ange språk uttryckligen när det behövs. Hantera resultatsidor och svarsfel. Anta inte att första sidan innehåller alla kandidater.
- `pxstatspy` är en valfri tredjepartsklient, inte en SCB-produkt eller en semantisk sökmotor. Kontrollera om biblioteket är installerat och vilken version och vilka API-funktioner det erbjuder. Använd det endast för funktioner det stöder väl och validera anrop och svar mot API-kontraktet. Gör det inte till ett obligatoriskt beroende och installera det inte automatiskt. Om biblioteket saknas eller inte passar, anropa det dokumenterade REST-API:et direkt med en tillgänglig HTTP-klient.
- Lita inte på ihågkomna tabell-id:n eller koder från äldre gränssnitt. Kontrollera dem mot aktuella API-metadata vid varje uppgift.
- Följ API-gränserna i SCB:s aktuella dokumentation och konfiguration. Minimera antalet anrop, hämta inte alla kategorier om det inte behövs och dela upp stora urval endast vid behov.
- Antyd inte att all SCB-statistik finns i PxWebApi. För raster och geodata, använd SCB:s geodatatjänster eller nedladdningsbara filer enligt `references/geodata-workflow.md`. Förklara när högre upplösning eller egen geografi kräver beställda uppgifter. Aggregera, sammanfoga geografiskt eller summera inte rutdata utan att kontrollera mått, gränser, version och röjandeskydd.

## Underhåll av produktstödet

Uppdatera `SKILL.md` i samma ändring varje gång en statistikprodukt eller ett ämnesområde läggs till, även när en befintlig guide utökas. Håll beskrivningens sökbegrepp, relevant grundmetod eller hänvisning och referenslistan förenliga med det faktiska stödet. Länka varje ny guide direkt härifrån. En fristående referensfil räcker inte som färdigt produktstöd. Kontrollera aktuella metadata och dokumentera statistisk enhet, population, geografi, referensperiod, enheter, jämförbarhet och röjandeskydd i guiden. Lägg till eller uppdatera ett realistiskt statistiskt acceptansfall. Kör den befintliga strukturella valideringen utan nätverk och redovisa statistiska kontroller separat från strukturella. Håll nya kontroller mot det aktuella API:et åtskilda från den nätverksfria valideringen.

## Referenser

- `references/semantic-workflow.md` — jämförelse av tabellkandidater och genomarbetat befolkningsexempel.
- `references/geodata-workflow.md` — när geodata behövs, åtkomstvägar och hantering av ZIP och GeoPackage.
- `references/bas-workflow.md` — arbetsmarknadsstatus, tabellval, ålder, geografi, revideringar och skillnader mot AKU.
- `references/aku-workflow.md` — arbetskraftsbegrepp, urvalsskattningar, tidsserier, geografi och kvalitetsbegränsningar.
- `references/commuting-workflow.md` — tabellval, pendlingsriktning, uttagsstorlek och jämförbarhet.
- `references/household-workflow.md` — hushållsdefinition, tabellval, täckning, geografi och röjandeskydd.
- `references/income-workflow.md` — disponibel inkomst, ekonomisk standard, prisnivå, population och jämförbarhet.
- `references/education-workflow.md` — högsta utbildning (UREG), studiedeltagande (RPU), SUN och jämförbarhet.
- `references/regional-accounts-workflow.md` — BRP, hushållsinkomster, löner, sysselsättning, investeringar, geografi och priser.
- `references/national-accounts-workflow.md` — konsumtionsutgifter efter COICOP, sektorer och nämnare, löpande priser, kedjade volymer och revideringar.
- `references/enterprise-economy-workflow.md` — företags- och verksamhetsenheter, omsättning, förädlingsvärde, produktivitet, investeringar och jämförbarhet.
- `references/cpi-workflow.md` — KPI och närliggande mått, indexuppräkning, basårs- och klassifikationsbyten 2026 samt prisnivå.
- `references/housing-workflow.md` — boende, bostadsbestånd, boendeutgifter, bostadsyta, trångboddhet, täckning och jämförbarhet.
- `references/migration-workflow.md` — flyttningar, invandring, utvandring, flyttnetto, tabellval och jämförbarhet.
- `references/pxstatspy-assessment.md` — när det valfria Pythonbiblioteket är användbart.
- `references/OpenAPI-source.md` — källor och versionsuppgifter för det inkluderade API-kontraktet.
- `references/PxAPI-2.yml` — ögonblicksbild av det officiella API-kontraktet.
