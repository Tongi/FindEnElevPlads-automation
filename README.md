# Automatiseret Dataudvinding med Selenium og asyncio

Dette kodeeksempel demonstrerer automatiseret dataudvinding fra en webside ved hjælp af Selenium og asyncio i Python. Det gør brug af en Chrome WebDriver til at interagere med websiderne.

## Installation

For at køre koden skal du først installere de nødvendige biblioteker ved at køre følgende kommandoer:

```bash

pip install selenium asyncio
for at kunne kører programmet, skal du skrive:
python datatekniker.py


Tilpasning af koden
Erstat XPaths og URLs i koden med dem, der er relevante for den hjemmeside, du vil interagere med.
Justér ventetider, sideantal og andre parametre efter behov.


Efter kørslen vil koden interagere med hjemmesiden, udføre dataudvinding og gemme resultaterne i tekstfiler. Du kan finde virksomhedsnavne med e-mails i virksomheds.txt og individuelle e-mails for hver side i filer med formatet page_{side_num}_emails.txt, og til sidst vil der komme en virksomheds.txt.

Bemærkninger:
Må ej gøres til dit eget til at fremvise foran virksomheder.

