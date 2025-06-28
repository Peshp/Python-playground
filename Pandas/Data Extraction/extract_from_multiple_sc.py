import os
import pandas as pd

path = './data'
extension = '.csv'

files = [file for file in os.listdir("data") if file.endswith(extension)]

dfs = []
for file in files:
    df = pd.read_csv(os.path.join(path, file))
    df['source_file'] = file
    df = df.drop_duplicates()
    dfs.append(df)

combined_df = pd.concat(dfs, ignore_index=True)
output_path = os.path.join(path, 'combined_transformed.csv')
combined_df.to_csv(output_path, index=False)

print(f"Transformed data loaded into {output_path}")