import pandas as pd
import os

os.chdir(os.path.dirname(__file__))

df = pd.read_csv(r'C:/Users/sabni/Documents/SKILL/hi.csv')

total_rows = len(df)

rows_per_split = total_rows // 5

for i in range(5):
    start_idx = i * rows_per_split
    if i == 4: 
        end_idx = total_rows
    else:
        end_idx = (i + 1) * rows_per_split
    
    part = df.iloc[start_idx:end_idx]
    
    output_file = f'adult_{i+1}.csv'
    part.to_csv(output_file, index=False)

print("Split complete. Created 5 files: adult_part1.csv through adult_part5.csv")