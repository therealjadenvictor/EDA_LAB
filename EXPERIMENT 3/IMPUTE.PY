import numpy as np
import pandas as pd
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer, SimpleImputer

# Create sample DataFrame with missing values (NaN)
df = pd.DataFrame(
 {
 "Age": [25, np.nan, 30, 45, 22],
 "Salary": [50000, 60000, np.nan, 80000, 45000],
 "Category": ["A", "B", "A", np.nan, "B"],
 }
)

# 1. Mean Imputation (Numerical)
mean_imputer = SimpleImputer(strategy="mean")
df["Age_Mean"] = mean_imputer.fit_transform(df[["Age"]])

# 2. Median Imputation (Numerical - robust to outliers)
median_imputer = SimpleImputer(strategy="median")
df["Salary_Median"] = median_imputer.fit_transform(df[["Salary"]])

# 3. Mode Imputation (Categorical - fixed with .ravel())
mode_imputer = SimpleImputer(strategy="most_frequent")
df["Category_Mode"] = mode_imputer.fit_transform(df[["Category"]]).ravel()
# 4. MICE Imputation (Multivariate Imputation by Chained Equations)
# Select numerical columns for MICE
num_cols = ["Age", "Salary"]
mice_imputer = IterativeImputer(max_iter=10, random_state=42)
df_mice = df[num_cols].copy()
df_mice.iloc[:, :] = mice_imputer.fit_transform(df_mice)
df["Age_MICE"] = df_mice["Age"]
df["Salary_MICE"] = df_mice["Salary"] 
print(df)
