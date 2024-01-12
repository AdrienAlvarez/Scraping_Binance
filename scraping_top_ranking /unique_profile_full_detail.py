# URL de la page à scraper
url = "https://www.binance.com/en/futures-activity/leaderboard/top-ranking"

try:
    # Ouvre la page web
    driver.get(url)

    # Attente pour que le contenu de la page se charge
    time.sleep(5)

    # Clique sur le premier élément avec la classe "name css-vurnku"
    element = driver.find_element(By.CLASS_NAME, "TraderCard.css-vurnku")
    element.click()

    # Attendez 5 secondes après le clic
    time.sleep(5)

    # Obtention du code source de la page après le clic
    page_source = driver.page_source

    # Utilisation de BeautifulSoup pour analyser le code HTML
    soup = BeautifulSoup(page_source, 'html.parser')

    # Récupération des informations
    nom = soup.find_all(class_="name css-1ta711")[0].text
    rois = soup.find_all(class_="Number css-rtly53")
    total_roi = soup.find(class_="Number css-hw12on")
    total_pnl = soup.find_all(class_="Number css-hw12on")[1]
    following = soup.find(class_="css-1qj0ymt")
    followers = soup.find_all(class_="css-1qj0ymt")[1]
    weekly_ranking = soup.find(class_="label css-1l80a32")

    # Assurez-vous qu'il y a 6 valeurs ROI
    if len(rois) == 6:
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
    else:
        data = {'Error': 'Nombre inattendu de valeurs ROI'}

    # Créez un DataFrame à partir des données
    df = pd.DataFrame([data])

    # Affichez le DataFrame
    print(df)

finally:
    # Fermeture du navigateur
    driver.quit()
