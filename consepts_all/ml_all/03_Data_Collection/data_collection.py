import pandas as pd
from sklearn.datasets import load_iris

# --- Method 1: Load built-in dataset ---
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["target"] = iris.target
print("Iris dataset shape:", df.shape)
print(df.head())

# --- Method 2: Load from CSV ---
# df = pd.read_csv("data.csv")  # Uncomment when you have a CSV file

# --- Method 3: Create sample data manually ---
data = {
    "name": ["Ajay", "Ravi", "Priya"],
    "age": [25, 30, 22],
    "salary": [50000, 70000, 45000]
}
df2 = pd.DataFrame(data)
print("\nManual data:")
print(df2)
