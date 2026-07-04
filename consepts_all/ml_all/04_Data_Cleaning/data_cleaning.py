import pandas as pd
import numpy as np

# Sample data with issues
data = {
    "name": ["Ajay", "Ravi", None, "Priya", "Ravi"],
    "age": [25, None, 22, 30, 30],
    "salary": [50000, 70000, 45000, None, 70000]
}
df = pd.DataFrame(data)
print("Original:\n", df)

# 1. Check missing values
print("\nMissing values:\n", df.isnull().sum())

# 2. Fill missing values
df["age"].fillna(df["age"].mean(), inplace=True)
df["salary"].fillna(df["salary"].median(), inplace=True)
df["name"].fillna("Unknown", inplace=True)

# 3. Remove duplicates
df.drop_duplicates(inplace=True)

# 4. Reset index
df.reset_index(drop=True, inplace=True)

print("\nCleaned:\n", df)
