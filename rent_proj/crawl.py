#! usr/bin/python3
# *-* coding=UTF-8 *-*
__author__ = "Rush"

from bs4 import BeautifulSoup
import requests
import csv
import time
import urllib.request

url1 = "https://nj.58.com/chuzu/pn{page}/?minprice=1000_3000"
html = urllib.request.urlopen(url=url1)

# 已完成的页数序号，初始为0
page = 0

csv_file = open("rent.csv","w")
csv_writer = csv.writer(csv_file,delimiter = ',')

while True:
    page += 1
    print("fetch: ", url1.format(page=page))
    time.sleep(3)
    response = requests.get(url1.format(page=page))
    soup = BeautifulSoup(html,'html.parser')
    house_list = soup.select(".house-list > li.house-cell")

    # 循环到找不到新房源为止
    if not house_list:
        break

    for house in house_list:
        house_title = house.findAll("a",attrs={'rel':'nofollow'})
        house_url = house.select("a")[0]["href"]
        house_money = house.findAll("b",attrs={'class':'strongbox'})
        csv_writer.writerrow([house_title,house_money,house_url])

csv_file.close()

