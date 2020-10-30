import requests
from bs4 import BeautifulSoup
import csv

url= "https://finance.naver.com/sise/entryJongmok.nhn?&page="
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

filename = "kospi200.csv"
f = open (filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

title = "종목별 	현재가 	전일비 	등락률 	거래량 	거래대금(백만) 	시가총액(억)".split("\t")
writer.writerow(title)
for page in range(1, 21):
    data = requests.get(url + str(page) , headers=headers)
    data.raise_for_status()

    soup = BeautifulSoup(data.text, 'html.parser')
    stockTable = soup.find("table", {'class': 'type_1'}).find_all("tr")

    for stockTdlist in stockTable:
        stockList = stockTdlist.find_all("td")
        if len(stockList) <= 1:
            continue
        data = [stock.get_text().strip() for stock in stockList]
        print(data)
        writer.writerow(data)
