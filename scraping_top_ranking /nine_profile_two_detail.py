# URL de la page à scraper
url = "https://www.binance.com/en/futures-activity/leaderboard/top-ranking"

data_list = []  # Liste pour stocker les données de chaque élément

try:
    # Ouvre la page web
    driver.get(url)
    time.sleep(5)  # Attente pour le chargement de la page

    # Boucle pour cliquer sur les 9 premiers éléments
    for i in range(9):
        # Clique sur l'élément
        elements = driver.find_elements(By.CLASS_NAME, "TraderCard.css-vurnku")
        if i < len(elements):
            elements[i].click()
            time.sleep(5)  # Attente après le clic

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
            time.sleep(3)  # Attente après être revenu à la liste principale
        else:
            break

    # Créez un DataFrame à partir des données
    df = pd.DataFrame(data_list)

    # Affichez le DataFrame
    print(df)

finally:
    # Fermeture du navigateur
    driver.quit()
