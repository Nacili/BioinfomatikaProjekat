import pandas as pd
from pandas import ExcelWriter

def MergeChromosomes():
    
    file_name = "defined_1.xlsx"
    df = pd.read_excel(file_name, "Sheet1")
    for i in range(2, 23):
        file_name = "defined_" + str(i) + ".xlsx"
        tmp_df = pd.read_excel(file_name, "Sheet1")
        df = pd.concat([df, tmp_df], ignore_index=True)

    file_name = "preprocessed.xlsx"
    writer = ExcelWriter(file_name)
    df.to_excel(writer,'Sheet1', index=False)
    writer.save()