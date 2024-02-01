import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
import re
import spacy
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def basicUrl(input_string):
    url_pattern = re.compile(r'https?://[^\s/$.?#].[^\s]*')
    urls = re.findall(url_pattern, input_string)
    valid_urls = [url for url in urls if 'google.com' not in url]
    if valid_urls:
      parsed_url = urlparse(valid_urls[0])
      netloc = parsed_url.netloc
      tld = netloc.split('/')[-1]
      url = 'https://' + tld
      return url

def remove_duplicates(url):
    unique_urls_set = set(url)
    unique_urls_list = list(unique_urls_set)
    return unique_urls_list

def scrape_website(website_url):
    # response = requests.get(website_url)
    # if response.status_code == 200:
    #     soup = BeautifulSoup(response.text, 'html.parser')
    #     urls = []
    #     for a_tag in soup.find_all('a', href=True):
    #         href_value = a_tag['href']
    #         if(basicUrl(href_value)):
    #           urls.append(basicUrl(href_value))
    #     urls = remove_duplicates(urls)
    #     print(urls)
    #     # urls = ['https://p-s-sakai.net', 'https://import-cars.co.jp', 'https://www.yeiwa.co.jp', 'https://www.proconce.co.jp', 'https://www.ichiyaku.jp', 'https://www.itsuwa.net', 'https://www.sheltd.co.jp', 'https://cucinastyle.jp', 'https://www.honsyu-p.co.jp', 'https://www.epson-tcform.co.jp']
    #     for url in urls:
    #         print(url)
    #         get_anchor_text(url)
    #         print('----------------')
    # else:
    #     print("Failed to retrieve the page. Status code:", response.status_code)
    data = []
    urls = ['https://www.epson-tcform.co.jp', 'https://p-s-sakai.net', 'https://import-cars.co.jp', 'https://www.yeiwa.co.jp', 'https://www.proconce.co.jp', 'https://www.ichiyaku.jp', 'https://www.itsuwa.net', 'https://www.sheltd.co.jp', 'https://cucinastyle.jp', 'https://www.honsyu-p.co.jp']
    for url in urls:
        get_anchor_text(url)

def remove_tabs(text):
    return text.replace('\t', '').strip()

def get_anchor_text(url):
    print('----------------------------')
    print(url)
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, verify=False)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            footer_tag = soup.find('footer')
            if footer_tag:
                footer_text = footer_tag.get_text()
                for line in footer_text.split('\n'):
                    if any(keyword in line for keyword in ['会社', '〒', 'TEL']):
                        text = remove_tabs(line.strip())
                        print(text)
            else:
                return None
            print('----------------------------')
        else:
            return None

    except requests.exceptions.RequestException as e:
        return None

search_query = 'https://www.google.com/search?q=適切に保護することを社会的責務と考え 下記の方針に基づき その保護を徹底してまいります'


# import requests

# # Example URL for FileMaker Data API
# filemaker_url = 'https://your-filemaker-server/fmi/data/v1/databases/YourDatabase/layouts/YourLayout/records'

# # Example data to be inserted
# data_to_insert = {
#     "fieldData": {
#         "CompanyName": "Example Company",
#         "Address": "123 Main Street",
#         "PhoneNumber": "555-1234"
#     }
# }

# # Sending a POST request to insert data
# response = requests.post(filemaker_url, json=data_to_insert)

# # Check the response status
# if response.status_code == 200:
#     print("Data inserted successfully.")
# else:
#     print(f"Failed to insert data. Status code: {response.status_code}")

scrape_website(search_query)