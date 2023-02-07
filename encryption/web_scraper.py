import requests
import string
from collections import Counter
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"
response = requests.get(url)
siteHTML = response.text

soup = BeautifulSoup(siteHTML, 'html.parser')
articles = soup.findAll('a')

for article in articles:
    link = article.get("href")
    if link.startswith("/news/world/"):
        print(link)