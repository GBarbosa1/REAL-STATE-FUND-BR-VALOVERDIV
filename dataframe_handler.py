import pandas as pd

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
