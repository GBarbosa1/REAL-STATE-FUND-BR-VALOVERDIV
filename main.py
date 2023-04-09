import pandas as pd
from scrap_engine import scrap_init, get_url, get_element_xpath, click, send_keys, buffer, strip
from graph_handler import plotter
from dataframe_handler import dataframe_build, dataframe_sort,drop

base_url = "https://statusinvest.com.br/fundos-imobiliarios/"
buffer(1)

fii_list = pd.read_excel("FII_LIST.xlsx")
div_list=[]
name_list=[]
pvp_list=[]

browser = scrap_init(base_url)

for index,row in fii_list.iterrows():
    asset = fii_list.iloc[index,0]
    name_list.append(asset)
    get_url(browser, (base_url + asset))
    buffer(1)
    div = get_element_xpath(browser, "/html//main[@id='main-2']//div[@title='Dividend Yield com base nos últimos 12 meses']/strong[@class='value']")
    div_value = strip(div)
    div_list.append(div_value)
    pvp = get_element_xpath(browser, "/html//main[@id='main-2']/div[@class='container pb-7']/div[5]/div/div[2]/div/div[1]/strong[@class='value']")
    pvp_value = strip(pvp)
    pvp_list.append(pvp_value)
    print(pvp_list)

full_asset_data = {'ASSET_NAME':name_list,'DIV':div_list,'PVP':pvp_list}

asserted_fii_list = dataframe_build(full_asset_data, ['COD', 'PVP', 'DIV'])
asserted_fii_list = asserted_fii_list.astype('PVP': 'float', 'DIV':'float')
print(asserted_fii_list)
asserted_fii_list = drop(asserted_fii_list,'null', 0, True)

plotter(asserted_fii_list.pop('DIV'), asserted_fii_list.pop('PVP'))

