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