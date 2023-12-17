import pandas as pd
import numpy as np
import time
from graph_handler.graph_handler import plotter_with_hoover, show
from dataframe_handler.dataframe_handler import dataframe_build
from json_handler.json_handler import json_load
from scrap_engine.scrap_engine_bs4 import BeatifullSoupOperator

settings_json = json_load('settings.json')

base_url = settings_json['url'][0]['base_url']

time.sleep(1)
fii_list = pd.read_excel(settings_json['assets'][0]['input_asset_file'])
div_list=[]
name_list=[]
pvp_list=[]
value_list=[]
title = settings_json['graphs'][0]['dividend_over_pve'][0]['title']
xlabel = settings_json['graphs'][0]['dividend_over_pve'][0]['xlabel']
ylabel = settings_json['graphs'][0]['dividend_over_pve'][0]['ylabel']

scrapper_operator = BeatifullSoupOperator()

for index,row in fii_list.iterrows():
    asset = fii_list.iloc[index,0]
    name_list.append(asset)

    scrapper_operator.get_page(base_url + asset)
    scrapper_operator.get_all_fundamentals()

    div_list.append(scrapper_operator.fii_div)
    
    pvp_list.append(scrapper_operator.fii_pvp)
    
    value_list.append(scrapper_operator.fii_value)
    print(asset," ",scrapper_operator.fii_div," ",scrapper_operator.fii_pvp, " ", scrapper_operator.fii_value)
    
full_asset_data = {'COD':name_list,'DIV':div_list,'PVP':pvp_list,'VALUE':value_list}
asserted_fii_list = dataframe_build(full_asset_data, ['COD', 'DIV', 'PVP','VALUE'])
asserted_fii_list = asserted_fii_list.apply(lambda x: x.str.replace(',','.'))
asserted_fii_list = asserted_fii_list.apply(lambda x: x.str.replace('-',''))
asserted_fii_list.replace('null',np.NaN, inplace=True)
asserted_fii_list = asserted_fii_list.astype({'PVP': 'float', 'DIV':'float', 'VALUE':'float'}, errors= 'raise')
asserted_fii_list.dropna(axis=0, how='any', inplace=True)
asserted_fii_list = asserted_fii_list[asserted_fii_list.VALUE > 0]
asserted_fii_list = asserted_fii_list[asserted_fii_list.DIV> 0]
asserted_fii_list.to_excel(settings_json['assets'][0]['output_asset_file'])

time.sleep(60)
plotter_with_hoover(asserted_fii_list['PVP'], asserted_fii_list['DIV'],asserted_fii_list['COD'],asserted_fii_list['VALUE'],title = title,xlabel = xlabel,ylabel=ylabel)
show()