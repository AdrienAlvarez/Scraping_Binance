# URL de la page à scraper
url = "https://www.binance.com/en/futures-activity/leaderboard/top-ranking"

# Création d'un DataFrame pour stocker les données
df = pd.DataFrame(columns=['Nom', 'Daily ROI'])

try:
    # Ouvre la page web
    driver.get(url)

    # Boucle pour parcourir les pages de 1 à 12
    for page in range(1, 13):
        # Attente pour que le contenu de la page se charge
        time.sleep(3)

        # Clique sur le bouton de la page correspondante
        driver.find_element(By.ID, f"page-{page}").click()

        # Attente pour que le contenu de la nouvelle page se charge
        time.sleep(3)

        # Obtention du code source de la page
        page_source = driver.page_source

        # Utilisation de BeautifulSoup pour analyser le code HTML
        soup = BeautifulSoup(page_source, 'html.parser')

        # Récupération des 5 premiers noms et ROIs
        noms = soup.find_all(class_="name css-vurnku", limit=9)
        rois = soup.find_all(class_="Number css-rtly53", limit=9)

        # Ajout des données dans le DataFrame
        for nom, roi in zip(noms, rois):
            df = df.append({'Nom': nom.text, 'Daily ROI': roi.text}, ignore_index=True)

finally:
    # Fermeture du navigateur
    driver.quit()

# Affichage du DataFrame
print(df)
