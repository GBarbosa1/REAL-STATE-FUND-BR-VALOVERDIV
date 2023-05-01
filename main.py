import pandas as pd
import numpy as np
from scrap_engine import scrap_init, get_url, get_element_xpath, click, send_keys, buffer, strip
from graph_handler import plotter
from dataframe_handler import dataframe_build

base_url = "https://statusinvest.com.br/fundos-imobiliarios/"
buffer(1)

fii_list = pd.read_excel("FII_LIST.xlsx")
div_list=[]
name_list=[]
pvp_list=[]
value_list=[]
title = 'Realstate fund'
xlabel = 'PVE'
ylabel = 'Dividends'
    
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
    
    value = get_element_xpath(browser, xpath= "/html//main[@id='main-2']//div[@title='Valor atual do ativo']/strong[@class='value']")
    value_val = strip(value)
    value_list.append(value_val)
    

full_asset_data = {'COD':name_list,'DIV':div_list,'PVP':pvp_list,'VALUE':value_list}

asserted_fii_list = dataframe_build(full_asset_data, ['COD', 'DIV', 'PVP','VALUE'])
asserted_fii_list = asserted_fii_list.apply(lambda x: x.str.replace(',','.'))
asserted_fii_list = asserted_fii_list.apply(lambda x: x.str.replace('-',''))
asserted_fii_list.replace('null',np.NaN, inplace=True)

asserted_fii_list = asserted_fii_list.astype({'PVP': 'float', 'DIV':'float', 'VALUE':'float'}, errors= 'raise')
asserted_fii_list.dropna(axis=0, how='any', inplace=True)


asserted_fii_list = asserted_fii_list[asserted_fii_list.VALUE > 0]
asserted_fii_list = asserted_fii_list[asserted_fii_list.DIV> 0]

asserted_fii_list.to_csv("FII_LIST_ACTIVE.CSV")

plotter(asserted_fii_list.pop('PVP'), asserted_fii_list.pop('DIV'),asserted_fii_list('COD'),asserted_fii_list('VALUE'),title,xlabel,ylabel)