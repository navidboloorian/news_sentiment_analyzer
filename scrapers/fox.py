import requests 
from bs4 import BeautifulSoup

def get_headlines():
  urls = ["https://foxnews.com/politics", "https://www.foxnews.com/opinion"]

  for url in urls:
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")
    headings = soup.find_all(class_="title")

    headlines = set()

    for heading in headings:
      try:
        link = heading.find("a")
        headlines.add(link.contents[0])
      except:
        continue

  return list(headlines)