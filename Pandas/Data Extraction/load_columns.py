import pandas as pd

df = pd.read_csv(
    'data/economy.csv',  
    usecols=['Period', 'Descriptor'],
    low_memory=True
)

print(df)