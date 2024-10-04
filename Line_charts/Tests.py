
import pandas as pd
import numpy as np
xauusd = pd.read_csv("xauusd_d.csv",parse_dates=["Date"],index_col="Date")
xagusd = pd.read_csv("xagusd_d.csv",parse_dates=["Date"],index_col="Date")
ndq = pd.read_csv("ndq_d.csv",parse_dates=["Date"],index_col="Date")
spx = pd.read_csv("spx_d.csv",parse_dates=["Date"],index_col="Date")

merged_close_interpolated_df=pd.read_csv("merged_close_interpolated_df.csv",parse_dates=["Date"],index_col="Date")

#Checks for NUlls in datasets

def check_nulls(*dfs):
    i = 1
    for df in dfs:
        print(f"Dataset {i} null values overview")
        print(df.isnull().sum())
        print("\n"+"-"*30+"\n")
        i+=1


check_nulls(xauusd,xagusd,ndq,spx,merged_close_interpolated_df)


