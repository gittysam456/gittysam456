#...1. load dataset
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#..load dataset
df=pd.read_csv("matplotlib_data.csv")
df.head()
df.info()
df.describe()
print(df.describe())
#line plot example
df['Sales'].plot(kind='line',title='Line Plot of sales')
plt.xlabel('Index')
plt.ylabel('Sales')
plt.show()

#average sales by category 
avg_sales=df.groupby('Category')['Sales'].plot(kind ='bar',title='Average Sales by Category',color = 'orange')
plt.xlabel('category')
plt.ylabel('Average Sales')
plt.legend()
plt.show()
#pie chart example
category_counts=df['Category'].value_counts()
category_counts.plot(kind='pie',title='Sales Distribution by Category',autopct='%1.1f%%',startangle=90)
plt.ylabel('') #remove the extra label
plt.show()
#plotting two charts sie by side in one window
dg ,axs = plt.subplots(1,2,figsize=(10,4))
axs[0].plot(df['sales'],color='blue',linestyle='--')
axs[0].set_title('Sales')
axs[1],plot(df['Profit'],color='green',linestyle=':')
axs[1].set_title('Profit')
plt.show()
#multiple plots in one chart window
fig,axs=plt.subplots(2,2,figsize=(10,10))
axs[0,0].plot(df['Sales'],color='blue',linestyle='--')
axs[0,0].set_title('Sales')
axs[0,1].plot(df['Sales'],color='green',linestyle=':')
axs[0,1].set_title('Sales')
axs[1,0].plot(df['Sales'],color='red',linestyle='-.')
axs[1,0].set_title('Sales')
axs[1,1].plot(df['Sales'],color='purple',linestyle='-')
axs[1,1].set_title('Sales')
plt.show()
#scatter plot example
plt.scatter(df['Sales'],df['Profit'],alpha=0.6,c=df['Profit'],cmap='viridis') # cmap is for color combiantion
plt.title('Scatter plot:sales vs profit')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.colorbar(label='Profit')
plt.show()