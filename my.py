# import requests
# from bs4 import BeautifulSoup

# # 二つのURL
# urls = [
#     "https://www.tl-assist.com/user/reservation/r8fteh3p/staff",
#     "https://www.tl-assist.com/user/reservation/f3c296sp/staff"
# ]

# # 会社名、住所、電話番号、URLを格納するリスト
# companies = []

# # URLから情報を取得する関数
# def get_info(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')
#     company_name = soup.find('h1').text.strip()
#     address = soup.find('span', {'class': 'address'}).text.strip()
#     phone_number = soup.find('span', {'class': 'phone'}).text.strip()
#     company_url = url
#     return {
#         'company_name': company_name,
#         'address': address,
#         'phone_number': phone_number,
#         'company_url': company_url
#     }

# # 二つのURLから情報を取得
# for url in urls:
#     companies.append(get_info(url))

# # 共通点を見つける（例えば、会社名が同じであるかどうか）
# common_companies = []
# for company in companies:
#     for other_company in companies:
#         if company != other_company and company['company_name'] == other_company['company_name']:
#             common_companies.append(company)

# # 結果を出力
# for company in common_companies:
#     print("会社名:", company['company_name'])
#     print("住所:", company['address'])
#     print("電話番号:", company['phone_number'])
#     print("URL:", company['company_url'])
#     print()

import requests
from bs4 import BeautifulSoup
import random
import time

def scrape_google(keyword):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    params = {
        'q': keyword,
        'num': 10,  # Number of results per page
        'hl': 'en'  # Language
    }
    
    try:
        response = requests.get('https://www.google.com/search', headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)
        
        search_results = []
        for link in links:
            href = link['href']
            if href.startswith('/url?'):
                url = requests.utils.urlparse(href)
                search_results.append(url.query.split('q=')[1])
        
        return search_results
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return []

def main():
    keywords = ['web scraping', 'data mining', 'machine learning']  # Example keywords
    for keyword in keywords:
        print(f"Scraping Google for keyword: {keyword}")
        search_results = scrape_google(keyword)
        for idx, result in enumerate(search_results, 1):
            print(f"{idx}. {result}")
        print("-" * 50)
        time.sleep(random.uniform(5, 10))  # Add random delay between requests to avoid getting blocked

if __name__ == "__main__":
    main()
