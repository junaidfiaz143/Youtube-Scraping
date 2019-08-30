from bs4 import BeautifulSoup
import requests
import os

def request_webpage(url):
  res = requests.get(url)
  
  try:
    res.raise_for_status()
  except Exception as exp:
    print("Error: ", exp)

  return res

url = "https://www.youtube.com/watch?v=au-MlOmYX80"

coming_soon_page = request_webpage(url)

# coming_soon_page.text

coming_soon_soup = BeautifulSoup(coming_soon_page.text, features="lxml")
# print(coming_soon_soup.prettify())

channelId = coming_soon_soup.find('meta', itemprop='channelId')
print("[CHANNEL-ID] ", channelId["content"])

title = coming_soon_soup.find('meta', property='og:title')
print("[TITLE] ", title["content"])

description = coming_soon_soup.find('meta', property='og:description')
print("[DESCRIPTION] ", description["content"])

views = coming_soon_soup.find('div', attrs={'class': 'watch-view-count'})
print("[VIEWS] ", views.text)

image = coming_soon_soup.find('meta', property='og:image')
print("[IMAGE] ", image["content"])

url = coming_soon_soup.find('meta', property='og:url')
print("[URL] ", url["content"])

print("[TAGS]")
tags = coming_soon_soup.findAll('meta', property='og:video:tag')
for i, tag in enumerate(tags):
  print(str(i+1) + ". ", tag["content"])