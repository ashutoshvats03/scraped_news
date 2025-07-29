from bs4 import BeautifulSoup
import os
import pandas as pd

d={'name':[], 'MRP':[], 'price':[],'dis':[]}
# name=KzDlHZ
# MRP yRaY8j ZYYwLA
# price Nx9bqj _4b5DiR
# dis UkUFwK
for file in os.listdir("sel/data/"):
    if file.endswith(".html"):
        with open(f"sel/data/{file}", "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")
            name=soup.find('div', class_="KzDlHZ")
            mrp=soup.find('div', class_="yRaY8j ZYYwLA")
            price=soup.find('div', class_="Nx9bqj _4b5DiR")
            dis=soup.find('div', class_="UkUFwK")
            
            d['name'].append(name.text.strip() if name else "N/A")
            d['MRP'].append(mrp.text.strip() if mrp else "N/A")
            d['price'].append(price.text.strip() if price else "N/A")
            d['dis'].append(dis.text.strip() if dis else "N/A")

df=pd.DataFrame(d)
df.to_csv(f"sel/data/laptop.csv", index=False)
            