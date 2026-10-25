# SCB-statistik

En fristående ChatGPT-färdighet som hjälper till att hitta, granska och hämta statistik från Statistiska centralbyrån (SCB). Färdigheten använder SCB:s PxWebApi v2 och, för vissa geografiska frågor, SCB:s öppna geodata.

Den hjälper ChatGPT att välja en relevant tabell, kontrollera metadata och kategorier, bygga ett giltigt urval och förklara vad statistiken visar. Den är ett instruktions- och referenspaket – inte en egen statistiktjänst eller en garanti för att ChatGPT alltid väljer rätt tabell eller räknar rätt.

## Statistikområden

Färdigheten omfattar bland annat befolkning, hushåll, hushållsinkomster och ekonomisk standard, boende, KPI/KPIF/HIKP, utbildning, regional- och nationalräkenskaper, företagens ekonomi, arbetsmarknad (AKU och BAS), pendling, migration, geografi samt hushållens konsumtionsutgifter efter COICOP. Se [SKILL.md](SKILL.md) för aktuell omfattning och arbetsgång.

## Använd färdigheten

Ställ en vanlig fråga på svenska, till exempel:

- Hur har folkmängden i Helsingborg förändrats 2000–2025?
- Hur många bor i Malmö och arbetar i Lund?
- Hur har KPI och KPIF utvecklats sedan 2020?
- Vad var medianen för hushållens disponibla inkomst i Uppsala län?
- Hur stor andel av hushållens konsumtionsutgifter går till transporter?

Be gärna om tabelltitel, referensperiod, urval, enhet och länk till källan. Färdigheten ska kontrollera aktuella tabellmetadata och tillgängliga värden; tabell-id:n och kategorikoder kan ändras.

## Installation och förutsättningar

Hämta eller klona hela repositoryt. Färdighetens katalog ska ha den här strukturen:

```text
scb-statistik/
├── SKILL.md
├── agents/
└── references/
```

Behåll `SKILL.md` direkt i katalogens rot och följande kataloger tillsammans med den. Referensfilerna innehåller ämnesspecifika arbetsflöden och API-kontraktet. Om de utelämnas kan instruktionerna hänvisa till filer som inte finns.

Lägg till eller importera färdigheten i ChatGPT enligt de installationsmöjligheter som finns i din ChatGPT-miljö. Repositoryt anger ingen universell installationsmetod: stöd för att importera en färdighet och möjligheten att köra kod eller göra nätverksanrop beror på miljön. Att kopiera in enbart `SKILL.md` i en chatt är inte samma sak som att installera hela färdigheten.

För att hämta aktuell statistik behöver ChatGPT-miljön ha ett tillgängligt sätt att nå SCB:s API eller geodata. En färdighetsinstruktion ger inte i sig nätverksåtkomst, kodkörning eller nya verktygsbehörigheter. Om åtkomst saknas kan färdigheten fortfarande hjälpa till med metod och tabellval, men den kan inte lova ett aktuellt datauttag.

Ingen separat MCP-server ingår. Pythonbiblioteket [`pxstatspy`](https://github.com/tompet64/pxstatspy) är valfritt och installeras eller körs inte automatiskt av färdigheten.

## Tester

Strukturtesterna körs från repositoryts rot:

```bash
python -m pip install pytest==8.3.5 PyYAML==6.0.2
python -m pytest -q tests/test_scb_skill.py
```

Testerna kontrollerar bland annat färdighetens YAML-metadata, referenser, dokumenterade ämnesområden och filstruktur. De är avsiktligt nätverksfria och kräver inte `pxstatspy`. GitHub Actions kör samma validering med Python 3.11.

Detta är **inte** ett test av SCB:s aktuella API-svar, ChatGPT:s tabellval eller statistiska beräkningar. [Acceptansfallen](docs/scb-statistik-acceptance.md) innehåller kontrollfrågor och dokumenterade referenser för separat manuell eller modellbaserad granskning. Ett referensvärde kan behöva uppdateras när SCB reviderar statistiken.

## Källor och licenser

- [SCB: API för Statistikdatabasen](https://www.scb.se/vara-tjanster/oppna-data/api-for-statistikdatabasen/) – officiell dokumentation och åtkomst till API:t.
- [Projektets licens](LICENSE.md) – MIT License.
- [Källa och licens för den inkluderade PxWebApi-specifikationen](references/OpenAPI-source.md) – specifikationen omfattas separat av Apache License 2.0; licenstext finns i `references/LICENSES/pxapispecs-apache-2.0.txt`.

Specifikationen är en versionsbunden referens, inte en källa till aktuella statistikvärden. Kontrollera alltid SCB:s aktuella dokumentation och metadata vid uttag.
