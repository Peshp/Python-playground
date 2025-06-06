import os
import pandas as pd

path = 'data'
extension = '.csv'
files = [file for file in os.listdir(path) if file.endswith(extension)]  

dfs = []
for file in files:
    df = pd.read_csv(os.path.join(path, file))  
    dfs.append(df)

print(df)