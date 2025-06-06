import pandas as pd

df = pd.read_csv(r'data\bussiness1.csv')

df['Values'] = df['Values'].astype(int)

print(df)