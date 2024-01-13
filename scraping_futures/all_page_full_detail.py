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

            for trader_index in range(15):
                traders = driver.find_elements(By.XPATH, "//div[contains(@class, 'TraderCard')]")
                if len(traders) > trader_index:
                    traders[trader_index].click()
                    time.sleep(3)

                    name = driver.find_element(By.CLASS_NAME, "name-wrap.css-4cffwv").text

                    # Récupérer tous les éléments 'Number css-rtly53'
                    rois = driver.find_elements(By.CLASS_NAME, "Number.css-rtly53")
                    time.sleep(1)
                    total_roi_elements = driver.find_elements(By.CLASS_NAME, "Number.css-hw12on")
                    time.sleep(1)
                    total_roi = total_roi_elements[0].text if len(total_roi_elements) > 0 else 'N/A'
                    time.sleep(1)
                    total_pnl = total_roi_elements[1].text if len(total_roi_elements) > 1 else 'N/A'
                    time.sleep(1)
                    following_elements = driver.find_elements(By.CLASS_NAME, "css-1qj0ymt")
                    time.sleep(1)
                    following = following_elements[0].text if len(following_elements) > 0 else 'N/A'
                    time.sleep(1)
                    followers = following_elements[1].text if len(following_elements) > 1 else 'N/A'
                    time.sleep(1)
                    weekly_ranking_elements = driver.find_elements(By.CLASS_NAME, "label.css-1l80a32")
                    time.sleep(1)
                    weekly_ranking = weekly_ranking_elements[0].text if len(weekly_ranking_elements) > 0 else 'N/A'

                    trader_info.append({
                        'Nom': name,
                        'Daily ROI': rois[0].text if len(rois) > 0 else 'N/A',
                        'Daily PNL (USD)': rois[1].text if len(rois) > 1 else 'N/A',
                        'Weekly ROI': rois[2].text if len(rois) > 2 else 'N/A',
                        'Weekly PNL (USD)': rois[3].text if len(rois) > 3 else 'N/A',
                        'Monthly ROI': rois[4].text if len(rois) > 4 else 'N/A',
                        'Monthly PNL (USD)': rois[5].text if len(rois) > 5 else 'N/A',
                        'Total ROI': total_roi if total_roi else 'N/A',
                        'Total PNL': total_pnl if total_pnl else 'N/A',
                        'Following': following if following else 'N/A',
                        'Followers': followers if followers else 'N/A',
                        'Weekly Ranking': weekly_ranking
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
trader_info = get_trader_info(url, 7)
print(trader_info)
