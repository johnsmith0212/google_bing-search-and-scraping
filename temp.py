from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def scrape_search_results(search_query, search_engine):
    if search_engine.lower() == "google":
        driver = webdriver.Chrome()
        search_url = f"https://www.google.com/search?q={search_query}&tbs=qdr:w"
    elif search_engine.lower() == "bing":
        driver = webdriver.Chrome()
        search_url = f"https://www.bing.com/search?q={search_query}&t1=w"
    else:
        print("Unsupported search engine. Supported options are 'google' and 'bing'.")
        return

    driver.get(search_url)

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search"))
        )

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        a_tags = soup.find_all('a', {'jsname': 'UWckNb'})
        href_values = [a.get('href') for a in a_tags]
        return href_values
    except Exception as e:
        print("An error occurred:", e)
    finally:
        driver.quit()

# Example usage
search_query = "適切に保護することを社会的責務と考え 下記の方針に基づき その保護を徹底してまいります"
google_results = scrape_search_results(search_query, "google")
# bing_results = scrape_search_results(search_query, "bing")

print("Google results:", google_results)
# print("Bing results:", bing_results)
