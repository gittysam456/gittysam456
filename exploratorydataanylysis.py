import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = sns.load_dataset("titanic")

# Basic inspection
print(df.head())
print("Shape:", df.shape)

# Describe dataset
print(df.describe(include="all").T)

# Handling duplicates
print("Duplicate Rows:", df.duplicated().sum())
df = df.drop_duplicates()

# Check and standardize categorical data
print(df['sex'].unique())
df['sex'] = df['sex'].str.lower()
print(df['sex'].unique())

df['deck'] = df['deck'].str.upper()
print(df['deck'].unique())

df['class'] = df['class'].str.upper()
print(df['class'].unique())

# Summary of categorical columns
print(df.describe(include=['category', 'object', 'bool']))

# Age distribution
sns.histplot(df['age'].dropna(), bins=30, kde=True)
plt.title("Age Distribution")
plt.show()

# Sex distribution
sns.countplot(data=df, x='sex')
plt.title("Sex Distribution")
plt.show()

# Correlation heatmap
sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlation Heatmap")
plt.show()

# Handle missing values
df['age'] = df['age'].fillna(df['age'].median())
df = df.dropna(subset=['embarked'])

# Final null check
print(df.isnull().sum())
