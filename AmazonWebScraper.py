#Importing Modules
from bs4 import BeautifulSoup
import requests
import time 
import datetime
import smtplib
import csv


#Website connections
URL = "https://www.amazon.com/MuscleTech-Protein-Sustained-Release-Chocolate/dp/B00BEOHFKO/?_encoding=UTF8&pd_rd_w=nlgGM&content-id=amzn1.sym.bc5f3394-3b4c-4031-8ac0-18107ac75816&pf_rd_p=bc5f3394-3b4c-4031-8ac0-18107ac75816&pf_rd_r=2N9GNWST3RCN7FQM59SP&pd_rd_wg=7SH0U&pd_rd_r=59f98f7c-9d7d-4aa3-a26c-ab8a1219c071&ref_=pd_gw_ci_mcx_mr_hp_atf_m&th=1"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}

page = requests.get(URL, headers=headers)

Soup1 = BeautifulSoup(page.content, "html.parser")

title = Soup1.find(id='productTitle').getText()
price = Soup1.find(id='priceblock_ourpice').getText()


print(title)
print(price)

#deleting whitespaces and deleting dollar sign
price.strip()[1:]
title.strip()

print(title)
print(price)

#generating timestamp
import datetime
today = datetime.date.today()

#Creating csv file and importing data
header = ['Title', 'Price', 'Date']
data = [title, price, today]

with open("Amazon_Product_Price.csv", "w", newlines="", encoding ='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)

#Generating Dataset
import pandas as pd
df = pd.read_csv(r"C:\Users\rohan\Amazon_Product_Price_dataser.csv")

#Appending data to dataset
with open("Amazon_Product_Price.csv", "a+", newlines="", encoding ='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)

#Automating the process
def check_price():
    URL = "https://www.amazon.com/MuscleTech-Protein-Sustained-Release-Chocolate/dp/B00BEOHFKO/?_encoding=UTF8&pd_rd_w=nlgGM&content-id=amzn1.sym.bc5f3394-3b4c-4031-8ac0-18107ac75816&pf_rd_p=bc5f3394-3b4c-4031-8ac0-18107ac75816&pf_rd_r=2N9GNWST3RCN7FQM59SP&pd_rd_wg=7SH0U&pd_rd_r=59f98f7c-9d7d-4aa3-a26c-ab8a1219c071&ref_=pd_gw_ci_mcx_mr_hp_atf_m&th=1"

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}

    page = requests.get(URL, headers=headers)

    Soup1 = BeautifulSoup(page.content, "html.parser")

    title = Soup1.find(id='productTitle').getText()
    
    price = Soup1.find(id='priceblock_ourpice').getText()
    
    price.strip()[1:]
    
    title.strip()
    
    import datetime
    today = datetime.date.today()

    import csv
    header = ['Title', 'Price', 'Date']

    data = [title, price, today]

    with open("Amazon_Product_Price.csv", "a+", newlines="", encoding ='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)


while(True):
    check_price()
    time.sleep(5)
