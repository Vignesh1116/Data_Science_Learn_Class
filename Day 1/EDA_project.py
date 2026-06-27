import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

print("Understanding dataset")

file_name = 'sales_data.csv'  # check if the file is exist
if not os.path.exists(file_name):
    print(f"Error:{file_name} is not found")
    exit()

# load the dataset

df = pd.read_csv(file_name)   
print("Successfully loaded")
print(f"Shape of the dataset:Rows:{df.shape[0]},Columns:{df.shape[1]}") 

print(df.head())
print(df.tail())
print(df.describe())

print("Handlimg Missing Values")

print(df.isnull().sum())

# With using Median

median_age=df['Age'].median()
df['Age'] = df['Age'].fillna(median_age)
print(median_age)

 # Using Mean

mean_spending = df['Spending'].mean()
df['Spending'] = df['Spending'].fillna(mean_spending)
print(mean_spending)

# Distribution Analysis

# plt.figure(figsize=(7,4))
# df['Spending'].hist(bins=10,color='skyblue',edgecolor='black')
# plt.title('Distribution of Spending')
# plt.xlabel('Spending Amount')
# plt.ylabel('Number of Customers')
# plt.show()

# # Correlation Matrix

# correlation = df.corr(numeric_only=True)
# print(correlation)

# print("Plotting Correlation Heatmap")
# plt.figure(figsize=(7,4))
# sns.heatmap(correlation,annot=True,cmap='coolwarm',fmt=".2f")
# plt.title("Correlation Heatmap")
# plt.show_()

# # Outlier Detection

# plt.figure(figsize=(7,4))
# sns.boxplot(x=df['Age'],color='lightgreen')
# plt.title("Boxplot of Customer Age")
# plt.xlabel('Age')
# plt.show()

print("Find the Outliers in age")
outliers=df[df['Age']>100]
print("Found Outliers(s):")
print(outliers)

