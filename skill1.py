import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv(r"C:\Users\sabni\Documents\SKILL\hi.csv")
print(df.head(20))
print("\n\n\n\n")

# Drop missing values
df.dropna(axis=0, inplace=True)

# Display info and basic stats
print("DataFrame Info:")
print(df.info())
print("\n\n\n\n")

print("Descriptive Statistics:")
print(df.describe())
print("\n\n\n\n")

# Check for null values
print("Any Null Values Present:")
print(df.isnull().any())
print("\n\n\n\n")

print("Sum of Null Values per Column:")
print(df.isnull().sum())
print("\n\n\n\n")

# Check for duplicates
print("Any Duplicated Rows:")
print(df.duplicated().any())
print("\n\n\n\n")

# Drop duplicates
df.drop_duplicates(inplace=True)

# Save the cleaned DataFrame
output_path = r"C:\Users\sabni\Documents\SKILL\hi2.csv"
df.to_csv(output_path, index=False)

