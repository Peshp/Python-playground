import pandas as pd

df = pd.read_csv(r'data\bussiness1.csv')

df = df.rename(columns={'Values': 'Integer'})

print(df)