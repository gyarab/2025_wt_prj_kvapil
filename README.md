# Webová aplikace
Vznikla v předmětu Webové technologie na Gymnáziu Arabská ve školním roce 2025/2026. 
A jedná se o webovou databázi pro zaznamenávání knih, her, seriálů a dalších médií, které jste zkonzumovali a neradi byste na ně zapomněli nebo je třeba jednoduše chtěli ohodnotit. Uživatel bude mít možnost své záznamy sdílet s ostatními, ale také si je nechat pouze pro sebe a své přátele. Uživatel nebude vázaný pouze na dostupnou databázi, ale naopak si bude moct i přídávat vlastní média, které se v databázi ani nenachází - pokud je však bude chtít sdílet s širším publikem, bude muset návrh projít přezkoumáním. 

## Local development

Aplikace používá Python Virtual Environment, před spuštěním je potřeba vytvořit venv (pokud neexistuje):

```bash
# Linux
python3 -m venv venv

# Windows
py -3 -m venv venv
```

Dále je třeba venv aktivovat:

```bash
# [Linux]
source ./venv/bin/activate

# Windows - Bash
source ./venv/Scripts/activate

# Windows - Power shell
...
```

Je třeba ujistit se, že jsou nainstalovány všechny závislosti:

```bash
# (venv)$
pip install -r requirements.txt
```