___Hvordan jeg lagde FlagGuessr med en API i Python___

__steg 1 (preparasjon)__
først begynte jeg med struktur og fulgte veiledningen vi fikk på teams
Jeg hadde static med style.css og templates med index.html og Python filen klar

__steg 2 (tilfeldig flagg)__
jeg let etter en API jeg kunne bruke i dette tilfellet. Først fant jeg ikke en API som kunne hente både flagg image url og navn på land så jeg måtte lage 2 separate API.
Da traff jeg en murvegg. Hvordan kan programmet finne ut hvilket land basert på bilde? Da let jeg enda mer og fant til slutt en API som passet perfekt.
Jeg kopierte API url i nettleseren og så hvordan dataen var bygd opp så jeg kunne hente den med en funksjon jeg lagde som kan kalles og hente et tilfeldig land med flagg.
Jeg brukte flask så jeg kunne kommunisere fra Python til html og sende dataen til index.html som viser et bilde som oppdateres når man returnerer render_template.
Etter det så måtte jeg lage en tekstboks som du kan skrive navnet til landet og lagde en event listener som aktiveres når du trykker på submit knappen.

__steg 3 (poeng og streak system)__
først så må jeg lage 2 session variabler: Points og Streak. Så må jeg oppdatere disse for hver runde. Hvis du får riktig så legges til +1 poeng og +1 streak, men hvis du får feil så mister du streaken og -1 poeng. Jeg opplevde en bug der hvis man refresher så får man infinite poeng. Jeg satt fast ganske lenge på denne buggen, men jeg fant ut at å bare ha Return render_template gjør at flask logikken utføres hver gang man refresher. Jeg brukte istedenfor Return redirect(url_for("home") og når du refresher så oppdateres bare get funksjonen så ingen logikk blir utført.

__steg 4 (hard mode og easy mode)__
min første ide for å lage dette systemet var å bruke 2 Python, 2 index programmer, men det gikk selvfølgelig ikke, så jeg kombinerte heller begge i hverandre, så la jeg bare til "mode" i session så kan du endre den med å bruke en knapp. På easy mode skulle du få 4 knapper der ett land er riktig og 3 er feil og hard mode måtte du skrive selv hvilket land i tekstboksen. Jeg la til alle knappene i session: BTN1, BTN2, BTN3 og BTN4. Så satte jeg verdien til hver knapp til et tilfeldig land og etter det så setter jeg den riktige knappen sitt land til det riktige landet. Da merket jeg en bug, hver gang jeg går til neste runde går det veldig tregt (ca 10 sekunder). Jeg fant ut at å kjøre API 5 ganger (4 for knappene) og en for riktig land var ikke optimalisert. API som jeg brukte returnerer alle land i en array og da trenger jeg ikke å kjøre API for hver gang siden jeg får alle landene bare av å kjøre API en gang. Så jeg kjørte API på start og satte all dataen til en variabel som jeg kunne bruke istedenfor å kjøre API hver eneste gang.

__steg 5 (tilfeldig katt bakgrunn)__
jeg fant en API som henter et tilfeldig bilde av en katt som en image url. Da lagde jeg en funksjon som brukte denne API til å hente et tilfeldig bilde og sende det til session som sendes videre til index.html med flask. Alt jeg trengte å gjøre var å sette <body style="background-image: {{ cat }}";> så den oppdateres hver gang vi sender data til html dokumentet med et nytt katte bilde.

__steg 6 (CSS)__
min første ide for css var en mørkeblå bakgrunn med hvit tekst for stor kontrast, jeg la til en container i midten som har bilde av land og knapper eller tekstboks for å skrive inn navnet på landet. Jeg hadde også score i venstre hjørne. Det ble litt kjedelig så jeg lagde en tilfeldig katt som kom i bakgrunnen.
