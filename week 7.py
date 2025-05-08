import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (replace 'dataset.csv' with the actual path to your CSV file)
df = pd.read_csv('dataset.csv')

# Display the first few rows of the dataset
print(df.head())

# Check the structure and data types of the dataset
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Clean the dataset by filling or dropping missing values
df = df.dropna()  # Or you can fill missing values with a method like df.fillna(value)
# Compute basic statistics for numerical columns
print(df.describe())

# Perform groupings by a categorical column (e.g., 'species') and compute the mean of a numerical column (e.g., 'sepal_length')
grouped = df.groupby('species')['sepal_length'].mean()

# Display the results of the grouping
print(grouped)
# Line chart showing trends over time (replace with actual time column if applicable)
plt.figure(figsize=(10,6))
plt.plot(df['date'], df['sales'], label='Sales Over Time')
plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.show()

# Bar chart showing the comparison of numerical values across categories
plt.figure(figsize=(10,6))
df.groupby('species')['sepal_length'].mean().plot(kind='bar')
plt.title('Average Sepal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Sepal Length')
plt.xticks(rotation=0)
plt.show()

# Histogram to visualize the distribution of a numerical column
plt.figure(figsize=(10,6))
plt.hist(df['sepal_length'], bins=20, edgecolor='black')
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.show()

# Scatter plot to visualize the relationship between two numerical columns
plt.figure(figsize=(10,6))
plt.scatter(df['sepal_length'], df['petal_length'])
plt.title('Sepal Length vs. Petal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.show()
plt.savefig('sepal_length_distribution.png')
