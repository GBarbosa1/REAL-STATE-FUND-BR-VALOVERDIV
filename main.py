import pandas as pd
import seaborn as sns
from scrap_engine import scrap_init, get_url, get_element_xpath, click, send_keys, buffer, strip

base_url = "https://statusinvest.com.br/fundos-imobiliarios/"
buffer(1)

fii_list = pd.read_excel("FII_LIST.xlsx")
div_list=[]
name_list=[]
browser = scrap_init(base_url)

for index,row in fii_list.iterrows():
    asset = fii_list.iloc[index,0]
    name_list.append(asset)
    get_url(browser, base_url + asset)
    buffer(1)
    div = get_element_xpath(browser, "/html//main[@id='main-2']//div[@title='Dividend Yield com base nos últimos 12 meses']/strong[@class='value']")
    div_value = strip(div)
    div_list.append(div_value)
    pvp = ge
    print(name_list)

    


