import pandas as pd

df = pd.read_csv('inflation_vs_metals.csv')

df.set_index('Date', inplace=True)

print(df.info())

