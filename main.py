import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta
from scrap_engine.scrap_engine import scrap_init, get_url, get_element_xpath, click, buffer, strip
from graph_handler.graph_handler import plotter, plotter_with_hoover, show
from dataframe_handler.dataframe_handler import dataframe_build,dataframe_read
from json_handler.json_handler import json_load

settings_json = json_load('settings.json')

base_url = settings_json['url'][0]['base_url']

buffer(1)
fii_list = pd.read_excel(settings_json['assets'][0]['input_asset_file'])
div_list=[]
name_list=[]
pvp_list=[]
value_list=[]
title = settings_json['graphs'][0]['dividend_over_pve'][0]['title']
xlabel = settings_json['graphs'][0]['dividend_over_pve'][0]['xlabel']
ylabel = settings_json['graphs'][0]['dividend_over_pve'][0]['ylabel']

browser = scrap_init(base_url)
for index,row in fii_list.iterrows():
    asset = fii_list.iloc[index,0]
    name_list.append(asset)
    get_url(browser, (base_url + asset))
    buffer(1)
    
    div = get_element_xpath(browser,xpath= settings_json['scrap'][0]['div_xpath'])
    div_value = strip(div)
    div_list.append(div_value)
    
    pvp = get_element_xpath(browser,xpath= settings_json['scrap'][0]['pvp_xpath'])
    pvp_value = strip(pvp)
    pvp_list.append(pvp_value)
    
    value = get_element_xpath(browser, xpath= settings_json['scrap'][0]['value'])
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
asserted_fii_list.to_excel(settings_json['assets'][0]['output_asset_file'])

buffer(60)
plotter_with_hoover(asserted_fii_list['PVP'], asserted_fii_list.pop['DIV'],asserted_fii_list['COD'],asserted_fii_list['VALUE'],title = title,xlabel = xlabel,ylabel=ylabel)
show()