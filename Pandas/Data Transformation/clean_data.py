import pandas as pd

df = pd.read_csv(r'data\bussiness1.csv')

df.drop_duplicates(inplace=True)

print(df)