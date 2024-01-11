from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

# URL de la page à scraper
url = "https://www.binance.com/en/futures-activity/leaderboard/top-ranking"

# Configurez le WebDriver (Assurez-vous que le pilote correspond à votre navigateur)
# Par exemple, pour Chrome, vous devriez télécharger ChromeDriver
chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)

try:
    # Ouvre la page web
    driver.get(url)

    # Attente pour que le contenu de la page se charge
    time.sleep(5)

    # Obtention du code source de la page
    page_source = driver.page_source

    # Utilisation de BeautifulSoup pour analyser le code HTML
    soup = BeautifulSoup(page_source, 'html.parser')

    # Recherche de tous les éléments avec la classe spécifiée pour les nombres
    numbers = soup.find_all(class_="Number css-rtly53")

    # Recherche de tous les éléments avec la classe spécifiée pour les noms des traders
    names = soup.find_all(class_="name css-vurnku")

    # Créez une liste vide pour stocker les données
    data = []

    # Parcourez les éléments et extrayez les données
    for number, name in zip(numbers, names):
        data.append({
            'Number': number.text,
            'Name': name.text
        })

    # Créez un DataFrame à partir des données
    df = pd.DataFrame(data)

    # Affichez le DataFrame
    print(df)

finally:
    # Fermeture du navigateur
    driver.quit()
