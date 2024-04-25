# Automatiseret Dataudvinding med Selenium og asyncio

Dette kodeeksempel demonstrerer automatiseret dataudvinding fra en webside ved hjælp af Selenium og asyncio i Python. Det gør brug af en Chrome WebDriver til at interagere med websiderne.

## Installation

For at køre koden skal du først installere de nødvendige biblioteker ved at køre følgende kommandoer:

```bash
pip install selenium asyncio
Sørg også for at have den seneste version af Chrome WebDriver installeret og tilgængelig i dit system PATH.

Tilpasning af koden
Erstat XPaths og URLs i koden med dem, der er relevante for den hjemmeside, du vil interagere med.
Justér ventetider, sideantal og andre parametre efter behov.
Kørsel af koden
Naviger til mappen, hvor din Python-scriptfil (dattekniker.py) er gemt, og kør scriptet fra kommandolinjen eller din foretrukne IDE ved at køre følgende kommando:

bash
Copy code
python datatekniker.py
Output
Efter kørslen vil koden interagere med hjemmesiden, udføre dataudvinding og gemme resultaterne i tekstfiler. Du kan finde virksomhedsnavne med e-mails i virksomheds.txt og individuelle e-mails for hver side i filer med formatet page_{side_num}_emails.txt.

Bemærkninger
Sørg for at have en stabil internetforbindelse, da koden er afhængig af adgang til internettet for at fungere korrekt.
Hvis der opstår fejl under kørslen, skal du kontrollere konsoloutputet for at identificere problemet og justere koden efter behov.
