from bs4 import BeautifulSoup
# from html.parser import HTMLParser
import requests
from lxml import html


url = "https://www.runnersworld.com/gear/a20853527/the-best-running-shoes-of-the-year/"
r = requests.get(url)

# print(text[0:2000])

soup = BeautifulSoup(r.text, "html.parser")

article = soup.find_all('h2', class_='body-h3', text=True)
for text in article:
    print(text)
#article.find_all('p')

# print(article)
for h2_tag in soup.find_all('h2'):
    print (h2_tag.text)
    


for p_tag in soup.find_all('strong'):
    print (p_tag.text)

# headline = soup.p
print(article)

