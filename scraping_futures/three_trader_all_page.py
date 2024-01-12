from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.by import By
import time
chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

def get_trader_names(url, pages):
    trader_names = []

    try:
        # Accéder à l'URL
        driver.get(url)
        time.sleep(5)  # Attendre que la page soit chargée

        # Boucle pour chaque page
        for page in range(1, pages + 1):
            if page > 1:
                # Utiliser JavaScript pour cliquer sur la page
                driver.execute_script(f"document.getElementById('page-{page}').click()")
                time.sleep(3)

            # Boucle pour cliquer sur les trois premiers traders
            for trader_index in range(3):
                # Utiliser XPath pour sélectionner les traders car les classes peuvent être dynamiques
                traders = driver.find_elements(By.XPATH, "//div[contains(@class, 'TraderCard')]")
                if len(traders) > trader_index:
                    traders[trader_index].click()
                    time.sleep(3)

                    # Récupérer le nom du trader
                    name = driver.find_element(By.CLASS_NAME, "name-wrap.css-4cffwv").text
                    trader_names.append(name)

                    # Retour à la page principale
                    driver.back()
                    time.sleep(3)

                    # Re-cliquer sur la page courante après chaque retour
                    if page > 1:
                        driver.execute_script(f"document.getElementById('page-{page}').click()")
                        time.sleep(3)

    finally:
        driver.quit()

    return trader_names

# URL de la page
url = "https://www.binance.com/en/futures-activity/leaderboard/futures/"

# Obtenir les noms des traders des 5 premières pages
trader_names = get_trader_names(url, 3)
print(trader_names)
