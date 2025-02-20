import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


# Load the dataset
df = pd.read_csv(r"C:/Users/sabni/Documents/SKILL/hi2.csv")

# Display the first 200 rows of the dataset
df.head(200)

# Plot 1: Histogram of Age with KDE
plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], kde=True, bins=30)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Plot 2: Histogram of Heart Rate with KDE
plt.figure(figsize=(10, 6))
sns.histplot(df['Heart_Rate'], kde=True, bins=30)
plt.title('Heart Rate Distribution')
plt.xlabel('Heart Rate')
plt.ylabel('Frequency')
plt.show()

# Plot 3: Histogram of Resting BP with KDE
plt.figure(figsize=(10, 6))
sns.histplot(df['Resting_BP'], kde=True, bins=30)
plt.title('Resting BP Distribution')
plt.xlabel('Resting BP')
plt.ylabel('Frequency')
plt.show()

# Plot 4: Scatterplot of Resting_BP vs. Heart_Rate, colored by Heart_Attack_Risk
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="Resting_BP", y="Heart_Rate", hue="Heart_Attack_Risk", palette='viridis')
plt.title('Resting BP vs. Heart Rate')
plt.xlabel('Resting BP')
plt.ylabel('Heart Rate')
plt.legend(title="Heart Attack Risk")
plt.show()

# Plot 5: Scatterplot of Age vs. Heart_Rate, colored by Heart_Attack_Risk
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="Age", y="Heart_Rate", hue="Heart_Attack_Risk", palette='coolwarm')
plt.title('Age vs. Heart Rate')
plt.xlabel('Age')
plt.ylabel('Heart Rate')
plt.legend(title="Heart Attack Risk")
plt.show()

# Plot 6: Bar plot of Age vs. Heart Rate
plt.figure(figsize=(10, 6))
sns.barplot(x='Age', y="Heart_Rate", data=df)  # ci=None to avoid confidence intervals
plt.title('Age vs. Heart Rate')
plt.xlabel('Age')
plt.ylabel('Heart Rate')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()

# Plot 7: Box plot of Heart Rate vs. Stress Level
plt.figure(figsize=(10, 6))
sns.boxplot(x='Heart_Rate', y="Stress_Level", data=df)
plt.title('Heart Rate vs. Stress Level')
plt.xlabel('Heart Rate')
plt.ylabel('Stress Level')
plt.show()

#Plot 8: lineplot with marker of Age vs.Heart_Attack_Risk
plt.figure(figsize=(10,6))
sns.lineplot(data=df, x="Age",y="Heart_Attack_Risk", label="lineplot with marker", color="blue", marker="o" )
plt.title('Age vs.Heart_Attack_Risk')
plt.xlabel('Age')
plt.ylabel('Heart_Attack_Risk')
plt.show()
# Count the occurrences of each unique value in the 'Heart_Attack_Risk' column
risk_counts = df['Heart_Attack_Risk'].value_counts()

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(risk_counts, labels=risk_counts.index, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'salmon','yellow'])
plt.title('Heart Attack Risk Distribution')
plt.show()

