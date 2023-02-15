import requests
import string
from collections import Counter
from bs4 import BeautifulSoup
from pathlib import Path

#########

# url = "https://www.bbc.com/news"
# response = requests.get(url)
# siteHTML = response.text

# soup = BeautifulSoup(siteHTML, 'html.parser')
# articles = soup.findAll('a')

# for article in articles:
#     link = article.get("href")
#     if link.startswith("/news/world/"):
#         print(link)

#########

url = "https://www.pusd.us/phs"
response = requests.get(url)
print(response.text)

html = response.text
soup = BeautifulSoup(html, 'html.parser')
elements = soup.findAll("span")

for element in elements:
    content = element.get_text()
    if str.__contains__(content, "Bulldog"):
        print(content)