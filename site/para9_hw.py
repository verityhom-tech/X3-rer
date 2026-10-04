from bs4 import BeautifulSoup
import requests

response = requests.get("https://bank.gov.ua/ua/markets/exchangerates")

soup = BeautifulSoup(response.text, features="html.parser")
soup.list = soup.find_all("td", {"data-label": "Офіційний курс"})
res = soup.list[7]

print(res.text)