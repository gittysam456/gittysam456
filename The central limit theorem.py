#The central limit theorem 
    """if u take the  repeated random sample of n size from any population with mean and finite variance , the sampling distribution of 
    the sample mean  approaches a normal distribution as number of samples increases, regardless of the shape of the 
    population distribution.
    The distribution of the sample approaches normality as the sample size increases, even if population distribution is skewed or non-normal.
    """
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()
print("print data types:",df.dtypes)
print("\nMissing values:",df.isnull().sum())
df.describe(include="all").T
#Handling duplicates
print("Duplicate Rows:",df.duplicated().sum())
#Drop the dupLICATES
df=df.drop_duplicates()
print(df['sex'].unique())  #cheeck categories