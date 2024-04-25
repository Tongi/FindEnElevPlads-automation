Trin 1: Installation af nødvendige biblioteker
For at køre dette kodeeksempel skal du først sikre dig, at du har de nødvendige biblioteker installeret. Du kan gøre dette ved at køre følgende kommando i din terminal:

Copy code
pip install selenium asyncio
Sørg også for at have den seneste version af Chrome WebDriver installeret og tilgængelig i dit system PATH.

Trin 2: Tilpasning af koden
Erstat XPaths og URLs i koden med dem, der er relevante for den hjemmeside, du vil interagere med.
Justér ventetider, sideantal og andre parametre efter behov.
Trin 3: Kør koden
Naviger til mappen, hvor din Python-scriptfil er gemt, og kør scriptet fra kommandolinjen eller din foretrukne IDE ved at køre følgende kommando:

Copy code
python datatekniker.py
Trin 4: Se output
Efter kørslen vil koden interagere med hjemmesiden, udføre dataudvinding og gemme resultaterne i tekstfiler. Du kan finde virksomhedsnavne med e-mails i virksomheds.txt og individuelle e-mails for hver side i filer med formatet page_{side_num}_emails.txt.

Bemærkninger:
Sørg for at have en stabil internetforbindelse, da koden er afhængig af adgang til internettet for at fungere korrekt.
Hvis der opstår fejl under kørslen, skal du kontrollere konsoloutputet for at identificere problemet og justere koden efter behov.
