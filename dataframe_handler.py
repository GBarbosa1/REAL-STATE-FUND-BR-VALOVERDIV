import pandas as pd

def dataframe_build(data, columns):
    dataframe = pd.DataFrame(data = data, columns=columns)
    return dataframe

def dataframe_sort(dataframe, by, ascending, inplace):
    dataframe.sort_values(by = by, ascending = ascending, inplace = inplace)
    return dataframe

def drop(dataframe, labels, axis, inplace):
    dataframe.drop(labels = labels,axis=axis,inplace=inplace)
    return inplace
    