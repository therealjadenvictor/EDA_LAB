import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

FILE_PATH = "/home/matlab/Downloads/catholic.csv"

if not os.path.exists(FILE_PATH):
    print(f"Error: Could not find the file at {FILE_PATH}")
    exit()

df = pd.read_csv(FILE_PATH)
print("Data loaded successfully!")


def show_scatter():
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x='read12', y='math12', hue='female', alpha=0.7)
    plt.title("Reading Scores vs Math Scores")
    plt.xlabel("12th Grade Reading Score")
    plt.ylabel("12th Grade Math Score")
    plt.show()

def show_correlation_heatmap():
    plt.figure(figsize=(12, 10))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()


def show_pairplot():
    subset_df = df[['read12', 'math12', 'lfaminc', 'cathhs']]
    sns.pairplot(subset_df, hue='cathhs', palette='Set1')
    plt.show()


show_correlation_heatmap()
