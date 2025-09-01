import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
#load sample dataset from seaborn
df=sns.load_dataset('tips')
#display few first rows of the dataset
print("sample data sets(Tips):")
print(df.head())
print(df.info())
print(df.describe())
##scatter plot - visualizing relationship between total_bill and tip
plt.figure(figsize=(7,5))
sns.scatterplot(data= df, x="total_bill" , y="tip",hue ="sex")
plt.title("Scatter plot between total bill and tip")
plt.show()

#count plot '#count plot is used to show the count of  observation in plot
plt.figure(figsize=(7,5))
sns.countplot(data=df,x='day',hue='sex')
plt.title('Count plot of days with')
plt.show()

#box plot - visualizing distribution of total_bill across different days
plt.figure(figsize=(7,5))
sns.boxplot(data=df,x='day',y='total_bill',hue='sex')
plt.title('Box plot of total bill ditribution by day and gender')
plt.show()

#swarm plot  shows the distribution of individual data points acroos the categories
plt.figure(figsize=(7,5))
sns.swarmplot(data=df,x='day',y='total_bill',hue='sex')
plt.title('Swarm plot of total bill distribution by day')
plt.show()

#heatmap - visualizing correlation between numerical variables in the dataset
plt.figure(figsize=(7,5))
sns.heatmap(df.select_dtypes(include='number').corr(),annot=True, cmap='coolwarm')
plt.title('Heatmap: correlation matrix')
plt.show()
#pair plot - visualizing pairwise relationships in the dataset
plt.figure(figsize=(7,5))
sns.pairplot(df,hue='sex')
plt.title('Pair plot of tips dataset')
plt.show()