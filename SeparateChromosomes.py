import pandas as pd
from pandas import ExcelWriter

def SeparateChromosomes():

    #data
    df = pd.read_excel("Cleaned.xlsx", "Sheet1")
    df = df.sort_values("Chromosome")
    df = df.reset_index(drop=True)

    # number of instances per chromosome
    lengths = [0 for i in range(22)]
    for i in range(1, 23):
        lengths[i-1] = df[df['Chromosome'] == i].count()['Chromosome']
   
    # create dataframes for each chromosome
    df1 = pd.DataFrame(columns=['sample', 'Chromosome', 'Start', 'End', 'Num_Probes', 'Length',
       'Modal_HSCN_1', 'Modal_HSCN_2', 'Modal_Total_CN', 'Subclonal_HSCN_a1',
       'Subclonal_HSCN_a2', 'Cancer_cell_frac_a1', 'Ccf_ci95_low_a1',
       'Ccf_ci95_high_a1', 'Cancer_cell_frac_a2', 'Ccf_ci95_low_a2',
       'Ccf_ci95_high_a2', 'LOH', 'Homozygous_deletion', 'depMapID'], index=[i for i in range(df[df['Chromosome'] == 1].count()['Chromosome'])])
    df2 = pd.DataFrame(columns=['sample', 'Chromosome', 'Start', 'End', 'Num_Probes', 'Length',
       'Modal_HSCN_1', 'Modal_HSCN_2', 'Modal_Total_CN', 'Subclonal_HSCN_a1',
       'Subclonal_HSCN_a2', 'Cancer_cell_frac_a1', 'Ccf_ci95_low_a1',
       'Ccf_ci95_high_a1', 'Cancer_cell_frac_a2', 'Ccf_ci95_low_a2',
       'Ccf_ci95_high_a2', 'LOH', 'Homozygous_deletion', 'depMapID'], index=[i for i in range(df[df['Chromosome'] == 2].count()['Chromosome'])])
    df3 = pd.DataFrame(columns=['sample', 'Chromosome', 'Start', 'End', 'Num_Probes', 'Length',
       'Modal_HSCN_1', 'Modal_HSCN_2', 'Modal_Total_CN', 'Subclonal_HSCN_a1',
       'Subclonal_HSCN_a2', 'Cancer_cell_frac_a1', 'Ccf_ci95_low_a1',
       'Ccf_ci95_high_a1', 'Cancer_cell_frac_a2', 'Ccf_ci95_low_a2',
       'Ccf_ci95_high_a2', 'LOH', 'Homozygous_deletion', 'depMapID'], index=[i for i in range(df[df['Chromosome'] == 3].count()['Chromosome'])])
    df4 = pd.DataFrame(columns=['sample', 'Chromosome', 'Start', 'End', 'Num_Probes', 'Length',
       'Modal_HSCN_1', 'Modal_HSCN_2', 'Modal_Total_CN', 'Subclonal_HSCN_a1',
       'Subclonal_HSCN_a2', 'Cancer_cell_frac_a1', 'Ccf_ci95_low_a1',
       'Ccf_ci95_high_a1', 'Cancer_cell_frac_a2', 'Ccf_ci95_low_a2',
       'Ccf_ci95_high_a2', 'LOH', 'Homozygous_deletion', 'depMapID'], index=[i for i in range(df[df['Chromosome'] == 4].count()['Chromosome'])])
    df5 = pd.DataFrame(columns=['sample', 'Chromosome', 'Start', 'End', 'Num_Probes', 'Length',
       'Modal_HSCN_1', 'Modal_HSCN_2', 'Modal_Total_CN', 'Subclonal_HSCN_a1',
       'Subclonal_HSCN_a2', 'Cancer_cell_frac_a1', 'Ccf_ci95_low_a1',
       'Ccf_ci95_high_a1', 'Cancer_cell_frac_a2', 'Ccf_ci95_low_a2',
       'Ccf_ci95_high_a2', 'LOH', 'Homozygous_deletion', 'depMapID'], index=[i for i in range(df[df['Chromosome'] == 5].count()['Chromosome'])])
    df6 = pd.DataFrame(columns=['sample', 'Chromosome', 'Start', 'End', 'Num_Probes', 'Length',
       'Modal_HSCN_1', 'Modal_HSCN_2', 'Modal_Total_CN', 'Subclonal_HSCN_a1',
       'Subclonal_HSCN_a2', 'Cancer_cell_frac_a1', 'Ccf_ci95_low_a1',
       'Ccf_ci95_high_a1', 'Cancer_cell_frac_a2', 'Ccf_ci95_low_a2',
       'Ccf_ci95_high_a2', 'LOH', 'Homozygous_deletion', 'depMapID'], index=[i for i in range(df[df['Chromosome'] == 6].count()['Chromosome'])])
    df7 = pd.DataFrame(columns=['sample', 'Chromosome', 'Start', 'End', 'Num_Probes', 'Length',
       'Modal_HSCN_1', 'Modal_HSCN_2', 'Modal_Total_CN', 'Subclonal_HSCN_a1',
       'Subclonal_HSCN_a2', 'Cancer_cell_frac_a1', 'Ccf_ci95_low_a1',
       'Ccf_ci95_high_a1', 'Cancer_cell_frac_a2', 'Ccf_ci95_low_a2',
       'Ccf_ci95_high_a2', 'LOH', 'Homozygous_deletion', 'depMapID'], index=[i for i in range(df[df['Chromosome'] == 7].count()['Chromosome'])])
    df8 = pd.DataFrame(columns=['sample', 'Chromosome', 'Start', 'End', 'Num_Probes', 'Length',
       'Modal_HSCN_1', 'Modal_HSCN_2', 'Modal_Total_CN', 'Subclonal_HSCN_a1',
       'Subclonal_HSCN_a2', 'Cancer_cell_frac_a1', 'Ccf_ci95_low_a1',
       'Ccf_ci95_high_a1', 'Cancer_cell_frac_a2', 'Ccf_ci95_low_a2',
       'Ccf_ci95_high_a2', 'LOH', 'Homozygous_deletion', 'depMapID'], index=[i for i in range(df[df['Chromosome'] == 8].count()['Chromosome'])])
    df9 = pd.DataFrame(columns=['sample', 'Chromosome', 'Start', 'End', 'Num_Probes', 'Length',
       'Modal_HSCN_1', 'Modal_HSCN_2', 'Modal_Total_CN', 'Subclonal_HSCN_a1',
       'Subclonal_HSCN_a2', 'Cancer_cell_frac_a1', 'Ccf_ci95_low_a1',
       'Ccf_ci95_high_a1', 'Cancer_cell_frac_a2', 'Ccf_ci95_low_a2',
       'Ccf_ci95_high_a2', 'LOH', 'Homozygous_deletion', 'depMapID'], index=[i for i in range(df[df['Chromosome'] == 9].count()['Chromosome'])])
    df10 = pd.DataFrame(columns=['sample', 'Chromosome', 'Start', 'End', 'Num_Probes', 'Length',
       'Modal_HSCN_1', 'Modal_HSCN_2', 'Modal_Total_CN', 'Subclonal_HSCN_a1',
       'Subclonal_HSCN_a2', 'Cancer_cell_frac_a1', 'Ccf_ci95_low_a1',
       'Ccf_ci95_high_a1', 'Cancer_cell_frac_a2', 'Ccf_ci95_low_a2',
       'Ccf_ci95_high_a2', 'LOH', 'Homozygous_deletion', 'depMapID'], index=[i for i in range(df[df['Chromosome'] == 10].count()['Chromosome'])])
    df11 = pd.DataFrame(columns=['sample', 'Chromosome', 'Start', 'End', 'Num_Probes', 'Length',
       'Modal_HSCN_1', 'Modal_HSCN_2', 'Modal_Total_CN', 'Subclonal_HSCN_a1',
       'Subclonal_HSCN_a2', 'Cancer_cell_frac_a1', 'Ccf_ci95_low_a1',
       'Ccf_ci95_high_a1', 'Cancer_cell_frac_a2', 'Ccf_ci95_low_a2',
       'Ccf_ci95_high_a2', 'LOH', 'Homozygous_deletion', 'depMapID'], index=[i for i in range(df[df['Chromosome'] == 11].count()['Chromosome'])])
    df12 = pd.DataFrame(columns=['sample', 'Chromosome', 'Start', 'End', 'Num_Probes', 'Length',
       'Modal_HSCN_1', 'Modal_HSCN_2', 'Modal_Total_CN', 'Subclonal_HSCN_a1',
       'Subclonal_HSCN_a2', 'Cancer_cell_frac_a1', 'Ccf_ci95_low_a1',
       'Ccf_ci95_high_a1', 'Cancer_cell_frac_a2', 'Ccf_ci95_low_a2',
       'Ccf_ci95_high_a2', 'LOH', 'Homozygous_deletion', 'depMapID'], index=[i for i in range(df[df['Chromosome'] == 12].count()['Chromosome'])])
    df13 = pd.DataFrame(columns=['sample', 'Chromosome', 'Start', 'End', 'Num_Probes', 'Length',
       'Modal_HSCN_1', 'Modal_HSCN_2', 'Modal_Total_CN', 'Subclonal_HSCN_a1',
       'Subclonal_HSCN_a2', 'Cancer_cell_frac_a1', 'Ccf_ci95_low_a1',
       'Ccf_ci95_high_a1', 'Cancer_cell_frac_a2', 'Ccf_ci95_low_a2',
       'Ccf_ci95_high_a2', 'LOH', 'Homozygous_deletion', 'depMapID'], index=[i for i in range(df[df['Chromosome'] == 13].count()['Chromosome'])])
    df14 = pd.DataFrame(columns=['sample', 'Chromosome', 'Start', 'End', 'Num_Probes', 'Length',
       'Modal_HSCN_1', 'Modal_HSCN_2', 'Modal_Total_CN', 'Subclonal_HSCN_a1',
       'Subclonal_HSCN_a2', 'Cancer_cell_frac_a1', 'Ccf_ci95_low_a1',
       'Ccf_ci95_high_a1', 'Cancer_cell_frac_a2', 'Ccf_ci95_low_a2',
       'Ccf_ci95_high_a2', 'LOH', 'Homozygous_deletion', 'depMapID'], index=[i for i in range(df[df['Chromosome'] == 14].count()['Chromosome'])])
    df15 = pd.DataFrame(columns=['sample', 'Chromosome', 'Start', 'End', 'Num_Probes', 'Length',
       'Modal_HSCN_1', 'Modal_HSCN_2', 'Modal_Total_CN', 'Subclonal_HSCN_a1',
       'Subclonal_HSCN_a2', 'Cancer_cell_frac_a1', 'Ccf_ci95_low_a1',
       'Ccf_ci95_high_a1', 'Cancer_cell_frac_a2', 'Ccf_ci95_low_a2',
       'Ccf_ci95_high_a2', 'LOH', 'Homozygous_deletion', 'depMapID'], index=[i for i in range(df[df['Chromosome'] == 15].count()['Chromosome'])])
    df16 = pd.DataFrame(columns=['sample', 'Chromosome', 'Start', 'End', 'Num_Probes', 'Length',
       'Modal_HSCN_1', 'Modal_HSCN_2', 'Modal_Total_CN', 'Subclonal_HSCN_a1',
       'Subclonal_HSCN_a2', 'Cancer_cell_frac_a1', 'Ccf_ci95_low_a1',
       'Ccf_ci95_high_a1', 'Cancer_cell_frac_a2', 'Ccf_ci95_low_a2',
       'Ccf_ci95_high_a2', 'LOH', 'Homozygous_deletion', 'depMapID'], index=[i for i in range(df[df['Chromosome'] == 16].count()['Chromosome'])])
    df17 = pd.DataFrame(columns=['sample', 'Chromosome', 'Start', 'End', 'Num_Probes', 'Length',
       'Modal_HSCN_1', 'Modal_HSCN_2', 'Modal_Total_CN', 'Subclonal_HSCN_a1',
       'Subclonal_HSCN_a2', 'Cancer_cell_frac_a1', 'Ccf_ci95_low_a1',
       'Ccf_ci95_high_a1', 'Cancer_cell_frac_a2', 'Ccf_ci95_low_a2',
       'Ccf_ci95_high_a2', 'LOH', 'Homozygous_deletion', 'depMapID'], index=[i for i in range(df[df['Chromosome'] == 17].count()['Chromosome'])])
    df18 = pd.DataFrame(columns=['sample', 'Chromosome', 'Start', 'End', 'Num_Probes', 'Length',
       'Modal_HSCN_1', 'Modal_HSCN_2', 'Modal_Total_CN', 'Subclonal_HSCN_a1',
       'Subclonal_HSCN_a2', 'Cancer_cell_frac_a1', 'Ccf_ci95_low_a1',
       'Ccf_ci95_high_a1', 'Cancer_cell_frac_a2', 'Ccf_ci95_low_a2',
       'Ccf_ci95_high_a2', 'LOH', 'Homozygous_deletion', 'depMapID'], index=[i for i in range(df[df['Chromosome'] == 18].count()['Chromosome'])])
    df19 = pd.DataFrame(columns=['sample', 'Chromosome', 'Start', 'End', 'Num_Probes', 'Length',
       'Modal_HSCN_1', 'Modal_HSCN_2', 'Modal_Total_CN', 'Subclonal_HSCN_a1',
       'Subclonal_HSCN_a2', 'Cancer_cell_frac_a1', 'Ccf_ci95_low_a1',
       'Ccf_ci95_high_a1', 'Cancer_cell_frac_a2', 'Ccf_ci95_low_a2',
       'Ccf_ci95_high_a2', 'LOH', 'Homozygous_deletion', 'depMapID'], index=[i for i in range(df[df['Chromosome'] == 19].count()['Chromosome'])])
    df20 = pd.DataFrame(columns=['sample', 'Chromosome', 'Start', 'End', 'Num_Probes', 'Length',
       'Modal_HSCN_1', 'Modal_HSCN_2', 'Modal_Total_CN', 'Subclonal_HSCN_a1',
       'Subclonal_HSCN_a2', 'Cancer_cell_frac_a1', 'Ccf_ci95_low_a1',
       'Ccf_ci95_high_a1', 'Cancer_cell_frac_a2', 'Ccf_ci95_low_a2',
       'Ccf_ci95_high_a2', 'LOH', 'Homozygous_deletion', 'depMapID'], index=[i for i in range(df[df['Chromosome'] == 20].count()['Chromosome'])])
    df21 = pd.DataFrame(columns=['sample', 'Chromosome', 'Start', 'End', 'Num_Probes', 'Length',
       'Modal_HSCN_1', 'Modal_HSCN_2', 'Modal_Total_CN', 'Subclonal_HSCN_a1',
       'Subclonal_HSCN_a2', 'Cancer_cell_frac_a1', 'Ccf_ci95_low_a1',
       'Ccf_ci95_high_a1', 'Cancer_cell_frac_a2', 'Ccf_ci95_low_a2',
       'Ccf_ci95_high_a2', 'LOH', 'Homozygous_deletion', 'depMapID'], index=[i for i in range(df[df['Chromosome'] == 21].count()['Chromosome'])])
    df22 = pd.DataFrame(columns=['sample', 'Chromosome', 'Start', 'End', 'Num_Probes', 'Length',
       'Modal_HSCN_1', 'Modal_HSCN_2', 'Modal_Total_CN', 'Subclonal_HSCN_a1',
       'Subclonal_HSCN_a2', 'Cancer_cell_frac_a1', 'Ccf_ci95_low_a1',
       'Ccf_ci95_high_a1', 'Cancer_cell_frac_a2', 'Ccf_ci95_low_a2',
       'Ccf_ci95_high_a2', 'LOH', 'Homozygous_deletion', 'depMapID'], index=[i for i in range(df[df['Chromosome'] == 22].count()['Chromosome'])])

    # split
    y = df["Chromosome"]
    i = 0
    j = 0
    for item in y:
        if item == 1:
            df1.loc[j] = df.loc[i]
            i += 1
            j += 1
            if lengths[0] == j:
                j = 0
            continue
        if item == 2:
            df2.loc[j] = df.loc[i]
            i += 1
            j += 1
            if lengths[1] == j:
                j = 0
            continue
        if item == 3:
            df3.loc[j] = df.loc[i]
            i += 1
            j += 1
            if lengths[2] == j:
                j = 0
            continue
        if item == 4:
            df4.loc[j] = df.loc[i]
            i += 1
            j += 1
            if lengths[3] == j:
                j = 0
            continue
        if item == 5:
            df5.loc[j] = df.loc[i]
            i += 1
            j += 1
            if lengths[4] == j:
                j = 0
            continue
        if item == 6:
            df6.loc[j] = df.loc[i]
            i += 1
            j += 1
            if lengths[5] == j:
                j = 0
            continue
        if item == 7:
            df7.loc[j] = df.loc[i]
            i += 1
            j += 1
            if lengths[6] == j:
                j = 0
            continue
        if item == 8:
            df8.loc[j] = df.loc[i]
            i += 1
            j += 1
            if lengths[7] == j:
                j = 0
            continue
        if item == 9:
            df9.loc[j] = df.loc[i]
            i += 1
            j += 1
            if lengths[9] == j:
                j = 0
            continue
        if item == 10:
            df10.loc[j] = df.loc[i]
            i += 1
            j += 1
            if lengths[9] == j:
                j = 0
            continue
        if item == 11:
            df11.loc[j] = df.loc[i]
            i += 1
            j += 1
            if lengths[10] == j:
                j = 0
            continue
        if item == 12:
            df12.loc[j] = df.loc[i]
            i += 1
            j += 1
            if lengths[11] == j:
                j = 0
            continue
        if item == 13:
            df13.loc[j] = df.loc[i]
            i += 1
            j += 1
            if lengths[12] == j:
                j = 0
            continue
            if item == 14:
                df14.loc[j] = df.loc[i]
                i += 1
                j += 1
                if lengths[13] == j:
                    j = 0
                continue
            if item == 15:
                df15.loc[j] = df.loc[i]
                i += 1
                j += 1
                if lengths[14] == j:
                    j = 0
                continue
            if item == 16:
                df16.loc[j] = df.loc[i]
                i += 1
                j += 1
                if lengths[15] == j:
                    j = 0
                continue
            if item == 17:
                df17.loc[j] = df.loc[i]
                i += 1
                j += 1
                if lengths[16] == j:
                    j = 0
                continue
            if item == 18:
                df18.loc[j] = df.loc[i]
                i += 1
                j += 1
                if lengths[17] == j:
                    j = 0
                continue
            if item == 19:
                df19.loc[j] = df.loc[i]
                i += 1
                j += 1
                if lengths[18] == j:
                    j = 0
                continue
            if item == 20:
                df20.loc[j] = df.loc[i]
                i += 1
                j += 1
                if lengths[19] == j:
                    j = 0
                continue
            if item == 21:
                df21.loc[j] = df.loc[i]
                i += 1
                j += 1
                if lengths[20] == j:
                    j = 0
                continue
            if item == 22:
                df22.loc[j] = df.loc[i]
                i += 1
                j += 1
                if lengths[21] == j:
                    j = 0
                continue
            
            
            # save
            for i in range(1, 23):
                file_name = "chr_" + str(i) + "_split.xlsx"
                writer = ExcelWriter(file_name)
                if i == 1:
                    df1.to_excel(writer,'Sheet1', index=False)
                if i == 2:
                    df2.to_excel(writer,'Sheet1', index=False)
                if i == 3:
                    df3.to_excel(writer,'Sheet1', index=False)
                if i == 4:
                    df4.to_excel(writer,'Sheet1', index=False)
                    if i == 5:
                        df5.to_excel(writer,'Sheet1', index=False)
                    if i == 6:
                        df6.to_excel(writer,'Sheet1', index=False)
                    if i == 7:
                        df7.to_excel(writer,'Sheet1', index=False)
                    if i == 8:
                        df8.to_excel(writer,'Sheet1', index=False)
                    if i == 9:
                        df9.to_excel(writer,'Sheet1', index=False)
                    if i == 10:
                        df10.to_excel(writer,'Sheet1', index=False)
                    if i == 11:
                        df11.to_excel(writer,'Sheet1', index=False)
                    if i == 12:
                        df12.to_excel(writer,'Sheet1', index=False)
                    if i == 13:
                        df13.to_excel(writer,'Sheet1', index=False)
                    if i == 14:
                        df14.to_excel(writer,'Sheet1', index=False)
                    if i == 15:
                        df15.to_excel(writer,'Sheet1', index=False)
                    if i == 16:
                        df16.to_excel(writer,'Sheet1', index=False)
                    if i == 17:
                        df17.to_excel(writer,'Sheet1', index=False)
                    if i == 18:
                        df18.to_excel(writer,'Sheet1', index=False)
                    if i == 19:
                        df19.to_excel(writer,'Sheet1', index=False)
                    if i == 20:
                        df20.to_excel(writer,'Sheet1', index=False)
                    if i == 21:
                        df21.to_excel(writer,'Sheet1', index=False)
                    if i == 22:
                        df22.to_excel(writer,'Sheet1', index=False)
                    writer.save()