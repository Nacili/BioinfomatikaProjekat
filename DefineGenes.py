import pandas as pd
from pandas import ExcelWriter

def DefineGenes():

    for x in range(1, 23):
        file_name = "chr_" + str(x) + "_split.xlsx"
        df = pd.read_excel(file_name, "Sheet1")
        range_index = int(df['Length'].mean())
        df = df.sort_values("Start")
        df = df.reset_index(drop=True)

        pd.options.mode.chained_assignment = None
        if x == 1:
            g = 0
        else:
            g = g + 1
        df.iloc[0, df.columns.get_loc('depMapID')] = g
        start_old = df["Start"][0]
        n = len(df.index)
        for i in range(1, n):
            start_new = df["Start"][i]
            if start_new != start_old and not (start_new < start_old + range_index):
                g = g + 1
                start_old = start_new
            df.iloc[i, df.columns.get_loc('depMapID')] = g
        
        file_name = "defined_" + str(x) + ".xlsx"
        writer = ExcelWriter(file_name)
        df.to_excel(writer,'Sheet1', index=False)
        writer.save()