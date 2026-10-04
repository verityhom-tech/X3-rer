import requests
from bs4 import BeautifulSoup

response = requests.get("https://coinmarketcap.com/")

soup = BeautifulSoup(response.text, "html.parser")
soup_list = soup.find_all("a")
for a in soup_list:
    print(a.text)