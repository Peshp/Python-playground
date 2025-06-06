import pandas as pd

# Read the CSV file with semicolon delimiter
df = pd.read_csv('data/economy.csv', delimiter=';')  

# 1. Get the number of rows using the DataFrame index
print(len(df.index))  

# 2. Count non-null values in the first column
print(df[df.columns[0]].count())  

# 3. Store row and column counts
count_row = df.shape[0]  # Number of rows
count_col = df.shape[1]  # Number of columns

# 4. Print rows and cols
print(f"Rows: {count_row}, Columns: {count_col}")