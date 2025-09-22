import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis, shapiro, normaltest, jarque_bera
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
"""measure of the central tendencies
    - mean : average
    - median : middle value 
    - mode : count the most frequent value
    measures of the dispersion
    -variance : how far a set of numbers are spread out from their average value
    -standard deviation : how much variation or dispersion of a set of values
    - range : difference between the largest and smallest values
    - quartiles : values that divide a list of numbers into quarters
    - interquartile range : difference between the first and third quartiles
    empirical rule -
    68-95-99.7
    skewness : measure of the asymmetry of the probability distribution of a real-valued random variable about its mean
    kurtosis : measure of the "tailedness" of the probability distribution of a real-valued random variable
    kurtosis > 3 : Leptokurtic(sharper peal , heavier tails, more outliers)
    kurtosis < 3 : platykurtic (flatter peak, lighter tails, fewer outliers)
    kurtosis = 3 : mesokurtic (normal distribution, moderate tails, moderate outliers)
    """
mtcars =  sns.load_dataset("mpg").dropna()
mtcars.head()
mtcars.describe()
col="mpg"
data=mtcars[col]
mean , std= data.mean(), data.std()
print(f"mean : {mean}, std : {std}")
plot histogram with std 
sns.plot(data,  kde="True")
    
for col in ["mpg", "horsepower", "weight"]:
    data=mtcars[col]
    mean , std= data.mean(), data.std()

    print(f"mean : {mean}, std : {std}")
    plt.figure(figsize=(10,5))
    sns.histplot(data, kde=True)
    plt.axvline(mean, color='r', linestyle='--', label='Mean')
    plt.axvline(mean + std, color='g', linestyle='--', label='Mean + 1 Std Dev')
    plt.axvline(mean - std, color='g', linestyle='--', label='Mean - 1 Std Dev')
    plt.title(f'Histogram of {col} with Mean and Std Dev')
    #plt.legend()
    #plt.show()
    Empirical rule - 68-95-99.7%
    for col in ['horsepower','weight','mpg']:
        print(f"{col}Kurtosis: {kurtosis(mtcars[col]):.2f}")
        sns.histplot(mtcars[col], kde=True)
        plt.title(f"Histogram of {col} ")
        plt.show()
        