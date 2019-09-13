import pandas as pd
from pandas import ExcelWriter
import numpy as np

def Clean():
    df = pd.read_excel("data_original.xlsx")
    y = df["sample"]

    # Leave only 2 most frequent classe
    i = 0
    for item in y:
        if 'LU' in item:
            df["sample"][i] = 'LUNG'
        elif 'HA' in item:
            df["sample"][i] = 'LYMPH'
        else:
            df = df.drop([i])
            i = i+1
    
    df.drop_duplicates(inplace = True)
    df.replace("NA", np.nan, inplace = True)
    df.replace("", np.nan, inplace = True)

    # Replace NULL values
    features = df.columns[1:].tolist()
    for column in features:
        if df[column].isna().sum() != 0:
            if isinstance(df[column].mode()[0], (np.float64)):
                df[column].replace(np.nan, df[column].mean(), inplace = True)
            else:
                df[column].replace(np.nan, df[column].mode()[0], inplace = True)


    writer = ExcelWriter(r'Cleaned.xlsx')
    df.to_excel(writer,'Sheet1', index=False)
    writer.save()

    