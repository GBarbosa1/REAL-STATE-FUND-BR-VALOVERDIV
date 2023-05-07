import pandas as pd
import os

def dataframe_build(data, columns):
    dataframe = pd.DataFrame(data = data, columns=columns)
    return dataframe

def dataframe_sort(dataframe, by, ascending, inplace):
    dataframe.sort_values(by = by, ascending = ascending, inplace = inplace)
    return dataframe

def dataframe_astype(dataframe,column,type):
    dataframe[column] = dataframe[column].astype(type)
    return dataframe

def dataframe_str_trunc(dataframe, column,number,direction):
    if direction=='right':
        dataframe[column] = dataframe[column].str[:-number]
    elif direction=='left':
        dataframe[column] = dataframe[column].str[number:]
    else:
        pass
    return dataframe

def dataframe_read(file_path, sep=''):
    extension = os.path.splitext(file_path)[1]
    print(extension)
    if extension == '.csv':
        dataframe = pd.read_csv(file_path,sep)
        return dataframe
    elif extension=='.xlsx':
        dataframe=pd.read_excel(file_path)
        return dataframe