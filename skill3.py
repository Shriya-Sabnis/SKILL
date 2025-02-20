import pandas as pd
from scipy.stats import zscore
df = pd.read_csv(r"C:/Users/sabni/Documents/SKILL/hi2.csv")
# Calculate Z-scores for each numeric column
for col in df.columns:
    if df[col].dtype in ['int64', 'float64']:
        z_scores = zscore(df[col])
        print(f"Z-scores for column '{col}':")
        print(z_scores)


# Function to remove outliers using IQR
def remove_outliers_iqr(df):
    for col in df.columns:
        if df[col].dtype in ['int64', 'float64']:  # Only process numerical columns
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            # Filter out outliers
            df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]

    return df

# Apply the function to remove outliers
df_no_outliers_iqr = remove_outliers_iqr(df)



# Function to remove outliers using Z-score
def remove_outliers_zscore(df, threshold=1):
    for col in df.columns:
        if df[col].dtype in ['int64', 'float64']:  # Only process numerical columns
            z_scores = zscore(df[col])
            df = df[abs(z_scores) <= threshold]

    return df

# Apply the function to remove outliers
df_no_outliers_zscore = remove_outliers_zscore(df)



print("Original DataFrame:")
print(df)
print("\n\n\n\n")
print("\nDataFrame after removing outliers:")
print(df_no_outliers_iqr)
print("\n\n\n\n")
print("\nDataFrame after removing outliers using Z-score:")
print(df_no_outliers_zscore)
print("\n\n\n\n")
output_path = r"C:/Users/sabni/Documents/SKILL/hi3.csv"
df_no_outliers_iqr.to_csv(output_path, index=False)
output_path = r"C:/Users/sabni/Documents/SKILL/hi4.csv"
df_no_outliers_zscore.to_csv(output_path, index=False)
