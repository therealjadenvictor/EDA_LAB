import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

train_df = pd.read_csv('fraudTrain.csv')
test_df = pd.read_csv('fraudTest.csv')

print(f"Train set rows: {len(train_df)} | Test set rows: {len(test_df)}")

scaler = StandardScaler()

train_df['amt_scaled'] = scaler.fit_transform(train_df[['amt']])
test_df['amt_scaled'] = scaler.transform(test_df[['amt']])

z_threshold = 3.0

train_outliers = train_df[np.abs(train_df['amt_scaled']) > z_threshold]
test_outliers = test_df[np.abs(test_df['amt_scaled']) > z_threshold]

print("\n--- Outliers Detected in fraudTrain.csv ---")
print(f"Total anomalies: {len(train_outliers)}")
print(train_outliers[['trans_date_trans_time', 'cc_num', 'merchant', 'amt', 'amt_scaled']].head())

print("\n--- Outliers Detected in fraudTest.csv ---")
print(f"Total anomalies: {len(test_outliers)}")
print(test_outliers[['trans_date_trans_time', 'cc_num', 'merchant', 'amt', 'amt_scaled']].head())
