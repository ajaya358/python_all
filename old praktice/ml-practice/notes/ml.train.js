# =========================
# 1. Import Libraries
# =========================
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# =========================
# 2. Load Data
# =========================
data = pd.read_csv("train.csv")

# =========================
# 3. Data Cleaning
# =========================
# Separate numeric and categorical
num_cols = data.select_dtypes(include=[np.number])
cat_cols = data.select_dtypes(include=['object'])

# Fill missing values
data[num_cols.columns] = num_cols.fillna(num_cols.mean())
data[cat_cols.columns] = cat_cols.fillna(cat_cols.mode().iloc[0])

# =========================
# 4. Feature Engineering
# =========================
# Convert text to numbers
data = pd.get_dummies(data)

# =========================
# 5. Split Data
# =========================
X = data.drop("SalePrice", axis=1)
y = data["SalePrice"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =========================
# 6. Train Model
# =========================
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# =========================
# 7. Prediction
# =========================
predictions = model.predict(X_test)

# =========================
# 8. Evaluation
# =========================
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Mean Absolute Error:", mae)
print("R2 Score:", r2)