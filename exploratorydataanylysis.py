import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = sns.load_dataset("titanic")
df.head()
print("Shape", df.shape)
df.describe(include="all").T
#Handling duplicates
print("Duplicate Rows:",df.duplicated().sum())
#Drop the dupLICATES
df=df.drop_duplicates()
print(df['sex'].unique())  #check categories
df.describe(include=['category','object','bool'])
df['sex'] = df['sex'].str.lower()  #standardize 
print(df['sex'].unique())
df['deck'] = df['deck'].str.upper()  #standardize
print(df['deck'].unique())
df['class'] = df['class'].str.upper()  #standardize
print(df['class'].unique())
sns.histplot(df['age'].dropna(), bins=30, kde=True)
plt.title("Age distribution")
plt.show()
sns.countplot(data=df, x='sex')
plt.title("Sex distribution")
plt.show()sns.heatmap(df.corr(numeric_only=True),annot=True,cmap="coolwarm")
plt.title("Correlation heatmap")
plt.show()df['age'].fillna(df['age'].median(), inplace=True)
print(df.isnull().sum())df.dropna(subset=['embarked'], inplace=True)
print(df.isnull().sum())