import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis, shapiro, normaltest, jarque_bera
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import boxcox, yeojohnson
import scipy.stats as stats
import statsmodels.api as sm
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
"""
#print(f"mean : {mean}, std : {std}")
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
       # plt.title(f"Histogram of {col} ")
       # plt.show()
col = "mpg"
data= mtcars[col]


# Shapiro - Wilk Test
stat, p =shapiro(data)
print(f"Shapiro-Wilk Test: p={p :.4f} -> {'Normal' if p>0.05 else 'Not Normal'}")

#D'Agostino's K^2 Test
stat, p = normaltest(data)
print(f"D'Agostino's K^2 Test: p={p :.4f} -> {'Normal' if p>0.05 else 'Not Normal'}")

#Jarque-Bera Test
stat, p = jarque_bera(data)
print(f"Jarque-Bera Test: p={p :.4f} -> {'Normal' if p>0.05 else 'Not Normal'}")

    square root transformation:
    
    cube root transformation :
    y=cuberoot(y)
    intution 
     works on the positive and negative values
    BOX-cox transformation:
    formaula 
    general family of power transformation
    chooses an optimal lambda that minimizes skewness

limitation :
1. requires x>0
2. sensitive to outliers
3. sometime hard to interpret the values

Yeo - John transformation :
     -extension of box cox
     -can handle zero and negative values

col="acceleration"
data=mtcars[col]
    #different transformations
transformations={
        "original":data,
        "log":np.log(data),
        "square root":np.sqrt(data),
        "cube-root": np.chart(data),
        "Box-Cox":None,
        "Yeo-Johnson":None
    }
    #box-cox(only if data>0)
    
    if (data>0).all():
        transformations["Box-Cox"],_=boxcox(data)
    #yejohnoson 
    tranformations["Yeo-Johnson"],_=yeojohnson(data)
    #shapiro afteer the treansformation 
    for name, tdata in transformations.items():
        if data is not None:
            stat, p = shapiro(tdata)

            """
data = mtcars["weight"]
#plot messy raw dsitribution
sns.histplot(data, kde=True,color ="salmon")
plt.title("Raw Distribution")
#plt.show()
#QPPLY CLT :SAMPLING DSTRIBUTION MEAN 
np.random.seed(42)
sample_means=[np.mean(np.random.choice(data,size=5,replace=True)) for _ in range(1000)]
sns.histplot(sample_means, kde=True,color="green")
plt.title("Sampling Distribution of the Mean (CLT applied)")
#print(plt.show()) 
col="acceleration"
data=mtcars[col]
#QQ plot

sm.qqplot(data, line ='s')
plt.title(f"Q-Q plot of {col}")
plt.show()
#apply clt :sampling distribution of mean
np.random.seed(42)
sample_means=[np.mean(np.random.choice(data,size=30,replace=True)) for _ in range(1000)]
sample_means=np.array(sample_means)
sm.qqplot(sample_means, line='s')
plt.title(f"Q-Q plot of Sampling Distribution of the Mean (CLT applied) for {col}")
plt.show()

