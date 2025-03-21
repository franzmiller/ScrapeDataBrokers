import requests
import bs4
import pandas as pd

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
# Here the user agent is for Edge browser on windows 10. You can find your browser user agent from the above given link.

url = "https://blog.incogni.com/data-brokers-incogni-covers/"
r = requests.get(url, headers=headers)
soup = bs4.BeautifulSoup(r.content, 'html5lib')

bltables = soup.find_all("div", class_="wdt-table-loader")
brokers = soup.find_all("tr")

print(brokers)
