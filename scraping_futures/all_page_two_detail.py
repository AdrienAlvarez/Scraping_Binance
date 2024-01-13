chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

def get_trader_info(url, pages):
    trader_info = []
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)
        time.sleep(5)

        for page in range(1, pages + 1):
            if page > 1:
                driver.execute_script(f"document.getElementById('page-{page}').click()")
                time.sleep(3)

            for trader_index in range(3):
                traders = driver.find_elements(By.XPATH, "//div[contains(@class, 'TraderCard')]")
                if len(traders) > trader_index:
                    traders[trader_index].click()
                    time.sleep(3)

                    name = driver.find_element(By.CLASS_NAME, "name-wrap.css-4cffwv").text

                    # Récupérer tous les éléments 'Number css-rtly53'
                    rois = driver.find_elements(By.CLASS_NAME, "Number.css-rtly53")
                    
                    # Assurez-vous qu'il y a suffisamment d'éléments pour chaque trader
                    if len(rois) >= 2:
                        daily_roi = rois[0].text  # Premier élément pour Daily ROI
                        pnl_roi = rois[1].text    # Deuxième élément pour Daily PNL
                    else:
                        daily_roi = pnl_roi = "N/A"

                    trader_info.append({
                        'Nom': name,
                        'Daily ROI': daily_roi,
                        'Daily PNL': pnl_roi
                    })

                    driver.back()
                    time.sleep(3)

                    if page > 1:
                        driver.execute_script(f"document.getElementById('page-{page}').click()")
                        time.sleep(3)

    finally:
        driver.quit()

    return trader_info

# URL de la page
url = "https://www.binance.com/en/futures-activity/leaderboard/futures/"

# Obtenir les infos des traders des 3 premières pages
trader_info = get_trader_info(url, 3)
print(trader_info)
