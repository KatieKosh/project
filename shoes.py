from bs4 import BeautifulSoup
from html.parser import HTMLParser
import requests

url = "https://www.runnersworld.com/gear/a20853527/the-best-running-shoes-of-the-year/"
r = requests.get(url)

# print(text[0:3000])

soup = BeautifulSoup(r.text, "html.parser")

article = soup.find_all('p', class_='body-text')

# print(article)



# headline = soup.p
print(article)

