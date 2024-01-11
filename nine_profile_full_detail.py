from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time

# URL de la page à scraper
url = "https://www.binance.com/en/futures-activity/leaderboard/top-ranking"

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
    time.sleep(5)  # Attente pour le chargement de la page

    # Boucle pour cliquer sur les 9 premiers éléments
    for i in range(9):
        # Clique sur l'élément
        elements = driver.find_elements(By.CLASS_NAME, "name.css-vurnku")
        if i < len(elements):
            elements[i].click()
            time.sleep(2)  # Attente après le clic

            # Obtention du code source de la page après le clic
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, 'html.parser')

            # Récupération des ROIs
            rois = soup.find_all(class_="Number css-rtly53")
            total_roi = soup.find(class_="Number css-hw12on")
            total_pnl = soup.find_all(class_="Number css-hw12on")[1]
            following = soup.find(class_="css-1qj0ymt")
            followers = soup.find_all(class_="css-1qj0ymt")[1]
            weekly_ranking = soup.find(class_="label css-1l80a32")

            data = {
                'Nom': nom,
                'Daily ROI': rois[0].text,
                'Daily PNL (USD)': rois[1].text,
                'Weekly ROI': rois[2].text,
                'Weekly PNL (USD)': rois[3].text,
                'Monthly ROI': rois[4].text,
                'Monthly PNL (USD)': rois[5].text,
                'Total ROI': total_roi.text if total_roi else 'N/A',
                'Total PNL': total_pnl.text if total_pnl else 'N/A',
                'Following': following.text if following else 'N/A',
                'Followers': followers.text if followers else 'N/A',
                'Weekly Ranking': weekly_ranking.text if weekly_ranking else 'N/A'
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
