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
