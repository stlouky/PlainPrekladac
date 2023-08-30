from selenium.common import UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def escape_text(text):
    # Nahrazení speciálních znaků
    text = text.replace('"', '\\"').replace("'", "\\'")
    return text
def prekladej():
    from selenium import webdriver
    import time

    def load_input_file(filename):
        with open(filename, 'r', encoding='utf-8') as file:
           content = file.read()
           return content.split('\n\n')  # rozdělení obsahu souboru podle dvou nových řádků (prázdný řádek)


    def translate_text_using_slovicka(text):
        #driver = webdriver.Chrome()
        if text != "":
            driver.get('https://www.slovnicek.cz/')

            # Nastavte hodnoty obou rozbalovacích seznamů pomocí JavaScriptu
            driver.execute_script("""
                var srcSelect = document.getElementById("srcLang");
                var tgtSelect = document.getElementById("tgtLang");

                srcSelect.value = "en";
                tgtSelect.value = "cz";

                // Spuštění události "change" informuje stránku o změně
                var event = new Event('change', {'bubbles': true});
                srcSelect.dispatchEvent(event);
                tgtSelect.dispatchEvent(event);
            """)

            js_input_script = f"document.getElementById('translate_textarea').value = '{text}';"
            driver.execute_script(js_input_script)

            # Odeslání formuláře pomocí JavaScriptu
            js_submit_script = "document.getElementById('top-tran-translate-button').click();"
            driver.execute_script(js_submit_script)

            # Čekání, než se překlad dokončí (v závislosti na rychlosti webové stránky můžete chtít upravit dobu čekání)
            time.sleep(5)  # Přidáno umělé čekání pro demonstraci, můžete to upravit podle potřeby

            # Získání výsledku překladu z výstupního textarea pomocí JavaScriptu
            translated_text = driver.execute_script("return document.getElementById('result_textarea').value;")
            #driver.quit()

            return translated_text

    input_file = 'translate.txt'
    output_file = 'vystup.txt'

    chunks = load_input_file(input_file)

    driver = webdriver.Chrome()

    with open(output_file, 'w', encoding='utf-8') as out_file:
        for chunk in chunks:
            chunk = escape_text(chunk)
            translated_chunk = translate_text_using_slovicka(chunk)
            out_file.write(translated_chunk)
            out_file.write('\n')  # Oddělení bloků výsledků dvěma novými řádky

    driver.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    prekladej()
