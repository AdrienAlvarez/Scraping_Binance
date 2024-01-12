# URL de la page à scraper
url = "https://www.binance.com/en/futures-activity/leaderboard/top-ranking"

try:
    # Ouvre la page web
    driver.get(url)

    # Attente pour que le contenu de la page se charge
    time.sleep(5)

    
    # Changer de page 
    element = driver.find_element(By.ID, "next-page")
    element.click()

    time.sleep(3)

    # Clique sur le premier trader
    element2 = driver.find_element(By.CLASS_NAME, "TraderCard.css-vurnku")
    element2.click()

    # Attendez 5 secondes après le clic
    time.sleep(5)

    # Obtention du code source de la page après le clic
    page_source = driver.page_source

    # Utilisation de BeautifulSoup pour analyser le code HTML
    soup = BeautifulSoup(page_source, 'html.parser')

    # Récupération du Nom
    nom = soup.find_all(class_= "name css-1ta711")

    # Récupération des ROIs
    rois = soup.find_all(class_="Number css-rtly53")

    # Assurez-vous qu'il y a 6 valeurs ROI
    if len(rois) == 6:
        data = {
            'Nom': nom,
            'Daily ROI': rois[0].text,
        }
    else:
        data = {'Error': 'Nombre inattendu de valeurs ROI'}

    # Créez un DataFrame à partir des données
    df = pd.DataFrame([data])

    # Affichez le DataFrame
    print(df)

finally:
    # Fermeture du navigateur
    driver.quit()
