### README.md pro PlainPrekladac

# PlainPrekladac

## Popis

PlainPrekladac je nástroj pro překlad textových souborů. Tento projekt obsahuje různé Python skripty pro manipulaci s textem, kontrolu gramatiky a překlad. Aktuálně jsou k dispozici následující skripty:

1. `text_manipulation.py` - Skript pro odstranění stránkových čísel a přebytečných mezer z textových souborů.
2. `grammar_check.py` - Skript pro kontrolu anglické gramatiky pomocí knihovny `language_tool_python`.
3. `web_translation.py` - Skript pro automatický překlad textu pomocí webové stránky `slovnicek.cz`.

## Instalace

Pro použití těchto skriptů je nutné mít nainstalován Python 3.x. Dále je třeba nainstalovat následující balíčky:

```bash
pip install language_tool_python
pip install selenium
```

## Použití

### Kontrola gramatiky

Spusťte skript `text_manipulation.py`:

```bash
python text_manipulation.py
```

### Překlad

Spusťte skript `web_translation.py`:

```bash
python web_translation.py
```

## Jak to funguje

1. `text_manipulation.py` načte vstupní textový soubor form.txt, odstraní přebytečné mezery a stránková čísla, provede jednoduchou kontrolu anglické gramatiky a uloží zpracovaný text do translate.txt.
2. `web_translation.py` načte opravený textový soubor translate.txt a provede jeho překlad. Přeložený text se uloží do souboru vystup.txt.
4. `grammar_check.py` načte text z přeloženého textového souboru vytup.txt, provede kontrolu gramatiky a uloží do prelozeno.txt.

## Licence

Tento projekt je dostupný pod licencí MIT.

---

Tento README soubor můžete vložit do kořenového adresáře vašeho GitHub repozitáře. Skripty, které jste poskytl, mohou být uloženy v samostatných souborech (`text_manipulation.py`, `grammar_check.py`, `web_translation.py`).
