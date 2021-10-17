from scrape_khana_academy.helpers import *

def scraper(link):
    while True:
        try:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--mute-audio")
            chrome_options.add_argument("--window-size=%s" % "1024,768")
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
            khan_academy_scraper(driver, link)
            break
        except:
            driver.close()
            continue