import requests 
from bs4 import BeautifulSoup

def get_headlines():
  response = requests.get("https://cnn.com/politics")
  html = response.text

  soup = BeautifulSoup(html, "html.parser")
  headings = soup.find_all(class_="container__headline-text")

  headlines = set()

  for heading in headings:
    try:
      headline = heading.contents[0]
      headlines.add(headline)
    except:
      continue

  return list(headlines)