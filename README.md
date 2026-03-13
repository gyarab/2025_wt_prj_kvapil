# Webová aplikace

Vznikla v rámci předmětu Webové technologie na Gymnáziu Arabská ve školním roce 2025/2026 jako závěrečný projekt předmětu WT.

## Odborný článek

Jedná se o ***webovou* databázi** pro zaznamenávání knih, her, seriálů a dalších médií, které jste zkonzumovali a neradi byste na ně zapomněli nebo je třeba jednoduše chtěli ohodnotit. **Uživatel** bude mít možnost své záznamy sdílet s ostatními, ale také si je nechat pouze pro sebe a své přátele. Uživatel nebude vázaný pouze dostupnou databázi, ale naopak si bude moct i **přídávat vlastní** média, které se v databázi ani nenachází - pokud je však bude chtít sdílet s širším publikem, bude muset návrh projít **ověřením**. Ověření bude administrováno **adminem**, který bude zodpovědný za správné ověření, podle **smluvních podmínek** a **pravidel platformy**. Platformu však bude moci navštívit (a částečně) využívat i **nepřihlášený uživatel** - budou mít možnost si média, rpofily a recenze prohlížet.

### Uživatel (nepřihlášený)

Nepřihlášený uživatel bude mít možnost si volně prohlížet stránku ve formě vyhledávání médií, uživatelů a recenzí. Nebude však mít možnost přidávat recenze nebo média.

### Uživatel (přihlášený)

Přihlášený uživatel bude mít stejné možnosti a navíc bude moci přidávat recenze a média, která na stránce chyběla. Dále bude mít možnost nahlašovat profily či média, která nemusí být v souladu s pravidly.

### Admin

Admin bude mít na starost chod stránky - bude posuzovat, zda může být navrhnuté médium přidáno, řešení nahlášeného obsahu/profilů (mazání (média, profily) /úpravy (média, profily\*)) a přidávání médií (tak jako přihlášený uživatel, pod svým jménem)

\**pouze pokud bude mít svolení uživatele*

## Wireframe

![wireframe](readme_resources\wireframe1.jpeg)
![wireframe2](readme_resources\wireframe2.jpeg)

## Userflow

![userflow](readme_resources\userflow.jpeg)

## DB scheme

![DB-scheme](readme_resources\DB-scheme.jpeg)

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
```

Je třeba ujistit se, že jsou nainstalovány všechny závislosti:

```bash
# (venv)$
pip install -r requirements.txt
```

Spustit lokalni server

```bash
cd prj
./manage.py runserver
```

Pokud pouštíme projekt poprvé, je třeba inicializovat DB pomocí

```bash
./manage.py migrate
```

Pokud je DB prázdná a chceme mít přístup do Django administrace, vytvoříme si uživatele pomocí

```bash
./manage.py createsuperuser
```

Doporučuji použít username `admin` a heslo `admin`, bez e-mailu.

## Změna `models.py`

Po kazde zmene v models.py je treba pustit skript, ktery vygeneruje zmenu struktury DB.

```bash
./manage.py makemigrations
```

Pote zmenu DB aplikovat na aktualni zivou DB

```bash
./manage.py migrate
```
