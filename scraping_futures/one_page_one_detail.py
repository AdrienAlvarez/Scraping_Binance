from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time

# URL de la page à scraper
url = "https://www.binance.com/en/futures-activity/leaderboard/futures"

# Configuration du WebDriver
chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

data_list = []  # Liste pour stocker les données de chaque élément

try:
    # Ouvre la page web
    driver.get(url)
    time.sleep(2)  # Attente pour le chargement de la page

    # Boucle pour cliquer sur les 15 premiers éléments
    for i in range(15):
        # Clique sur l'élément
        elements = driver.find_elements(By.CLASS_NAME, "name.css-vurnku")
        if i < len(elements):
            elements[i].click()
            time.sleep(2)  # Attente après le clic

            # Obtention du code source de la page après le clic
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, 'html.parser')

            # Récupération des données
            nom = soup.find_all(class_="name css-1ta711")[0].text
            rois = soup.find_all(class_="Number css-rtly53")

            data = {
                'Nom': nom,
                'Daily ROI': rois[0].text,
                'Daily PNL': rois[1].text
            }


            data_list.append(data)
            driver.back()
            time.sleep(2)  # Attente après être revenu à la liste principale
        else:
            break

    # Créez un DataFrame à partir des données
    df = pd.DataFrame(data_list)

    # Affichez le DataFrame
    print(df)

finally:
    # Fermeture du navigateur
    driver.quit()
