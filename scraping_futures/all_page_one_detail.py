from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

def get_trader_names(url, pages):

    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

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

            # Cliquer sur le premier trader
            driver.find_element(By.CLASS_NAME, "TraderCard.css-vurnku").click()
            time.sleep(3)

            # Récupérer le nom du trader
            name = driver.find_element(By.CLASS_NAME, "name-wrap.css-4cffwv").text
            trader_names.append(name)

            # Retour à la page principale
            driver.back()
            time.sleep(3)

    finally:
        driver.quit()

    return trader_names

# URL de la page
url = "https://www.binance.com/en/futures-activity/leaderboard/futures/"

# Obtenir les noms des traders des 5 premières pages
trader_names = get_trader_names(url, 5)
print(trader_names)
