import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv("https://raw.githubusercontent.com/salemprakash/EDA/main/Data/data.csv")
print(df.head(3))
print(df.tail(3))

print(df.dtypes )

print(df.describe())
pd.isna(df).any()

print(df['price'].str.isnumeric().value_counts())
print(df['price'].loc[df['price'].str.isnumeric() == False] )

price = df['price'].loc[df['price'] != '?']
print(price)
pmean = price.astype(int).mean()
print("Mean =",pmean)
df['price'] = df['price'].replace('?',pmean).astype(int)
df['price'].head(10)

horsepower = df['horsepower'].loc[df['horsepower'] != '?']
hpmean = horsepower.astype(int).mean()
df['horsepower'] = df['horsepower'].replace('?',hpmean).astype(int)
df['horsepower'].head()

df[df['normalized-losses']=='?'].count()
nl=df['normalized-losses'].loc[df['normalized-losses'] !='?'].count()
nmean=nl.astype(int).mean()
df['normalized-losses'] = df['normalized-losses'].replace('?',nmean).astype(int)
df['normalized-losses'].head()

mean = df["height"].mean()
median =df["height"].median()
mode = df["height"].mode()
print(mean)
print(median)
print(mode)

df.make.value_counts().nlargest(30).plot(kind='bar', figsize=(10,6))
plt.title("Number of cars by make")
plt.ylabel('Number of cars')
plt.xlabel('Make of the cars')

sns.FacetGrid(df).map(sns.distplot,"height").add_legend()

sns.FacetGrid(df).map(sns.distplot,"price").add_legend()

sns.boxplot(x="price",data=df)
plt.show()

plt.scatter(df["price"], df["horsepower"])
plt.title("Scatter Plot for horsepower vs price")
plt.xlabel("horsepower")
plt.ylabel("price")

sns.boxplot(x="engine-location",y="price",data=df)
plt.show()

sns.boxplot(x="drive-wheels", y="price",data=df)

sns.pairplot(df,vars = ['normalized-losses', 'price','horsepower'], kind="reg")
plt.show()

sns.set(style="ticks", color_codes=True)
sns.pairplot(df,height=2,vars = ['symboling', 'normalized-losses','wheel-base'], hue="drive-wheels")
plt.show()

corr = stats.pearsonr(df["price"], df["horsepower"])
print("p-value:\t", corr[1])
print("cor:\t\t", corr[0])

correlation = df.corr(method='pearson', numeric_only=True)
print(correlation)

sns.heatmap(correlation,xticklabels=correlation.columns,yticklabels=correlation.columns)
