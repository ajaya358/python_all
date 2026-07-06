"""
ML TRAINING EXAMPLES - Different Datasets

This file shows how to train models on different datasets by modifying the script.
Copy any of these examples into train_ml_models.py
"""

# ============================================================================
# EXAMPLE 1: Simple House Price Prediction (Current Setup)
# ============================================================================
example_1 = """
# File: ml-practice/dummy_data.csv
target_column = "price"
result = train_model(
    df=df,
    target_column=target_column,
    task="regression",           # Predicting continuous value
    test_size=0.2,
    model_name="house_price_model.joblib"
)
# RMSE: shows average prediction error
# R²: shows how well model fits data (0-1, higher is better)
"""


# ============================================================================
# EXAMPLE 2: House Classification (Good/Bad/Excellent)
# ============================================================================
example_2 = """
# First, add category to your CSV:
# square_feet,bedrooms,bathrooms,age,location,price,price_category
# 850,2,1,10,suburb,120000,good
# 900,3,2,5,suburb,145000,excellent

target_column = "price_category"
result = train_model(
    df=df,
    target_column=target_column,
    task="classification",       # Predicting category
    test_size=0.2,
    model_name="house_category_model.joblib"
)
# Accuracy: percentage of correct predictions
"""


# ============================================================================
# EXAMPLE 3: Using Kaggle Dataset (House Prices - Advanced)
# ============================================================================
example_3 = """
# Download from: https://www.kaggle.com/c/house-prices-advanced-regression-techniques
# Save train.csv to ml-practice/house_prices_kaggle/

from app.ml import load_csv

df = load_csv("ml-practice/house_prices_kaggle/train.csv")

# Dataset info:
# - 1460 houses
# - 80 features (size, bedrooms, bathrooms, etc)
# - Target: SalePrice

# Clean the data:
df = df.dropna()  # Remove rows with missing values
df_numeric = df.select_dtypes(include=['int64', 'float64'])  # Keep only numbers

target_column = "SalePrice"
result = train_model(
    df=df_numeric,
    target_column=target_column,
    task="regression",
    test_size=0.2,
    model_name="kaggle_house_prices_model.joblib"
)
"""


# ============================================================================
# EXAMPLE 4: Classification - Iris Dataset (Flowers)
# ============================================================================
example_4 = """
# Built-in dataset - no file needed
# Predicts: setosa, versicolor, virginica

from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target_names[iris.target]

target_column = "target"
result = train_model(
    df=df,
    target_column=target_column,
    task="classification",
    test_size=0.2,
    model_name="iris_flower_model.joblib"
)
"""


# ============================================================================
# EXAMPLE 5: Time Series - Stock Price (Regression)
# ============================================================================
example_5 = """
# File: ml-practice/stock_prices.csv
# date,open,high,low,close,volume
# 2024-01-01,100.50,101.20,100.10,101.00,1000000

df = load_csv("ml-practice/stock_prices.csv")

# Create features from time-based data
df['date'] = pd.to_datetime(df['date'])
df['day_of_week'] = df['date'].dt.dayofweek
df['month'] = df['date'].dt.month
df = df.drop('date', axis=1)  # Remove date column

target_column = "close"  # Predict closing price
result = train_model(
    df=df,
    target_column=target_column,
    task="regression",
    test_size=0.2,
    model_name="stock_price_model.joblib"
)
"""


# ============================================================================
# EXAMPLE 6: Text Data - Sentiment Classification
# ============================================================================
example_6 = """
# File: ml-practice/reviews.csv
# text,sentiment
# "Great product!",positive
# "Terrible quality",negative

# WARNING: Text needs preprocessing before training!
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

df = load_csv("ml-practice/reviews.csv")

# This is more complex - requires text vectorization
# Better to use specialized NLP libraries (transformers, nltk)
# For now: use only numeric features
"""


# ============================================================================
# EXAMPLE 7: Multiple CSV Files - Train/Test Split
# ============================================================================
example_7 = """
# Files: ml-practice/train.csv and ml-practice/test.csv

from app.ml import load_csv

train_df = load_csv("ml-practice/train.csv")
test_df = load_csv("ml-practice/test.csv")

# Combine for training
combined_df = pd.concat([train_df, test_df], ignore_index=True)

target_column = "price"
result = train_model(
    df=combined_df,
    target_column=target_column,
    task="regression",
    test_size=0.2,
    model_name="combined_model.joblib"
)
"""


# ============================================================================
# EXAMPLE 8: Database Query - Train on Database Data
# ============================================================================
example_8 = """
# Load data directly from PostgreSQL

from app.ml import load_data_from_db

query = \"\"\"
SELECT 
    square_feet, bedrooms, bathrooms, age, location, price 
FROM houses 
WHERE price IS NOT NULL
\"\"\"

connection_url = "postgresql://user:password@localhost/real_estate_db"
df = load_data_from_db(query, connection_url=connection_url)

target_column = "price"
result = train_model(
    df=df,
    target_column=target_column,
    task="regression",
    test_size=0.2,
    model_name="db_house_model.joblib"
)
"""


# ============================================================================
# EXAMPLE 9: Data Cleaning - Remove Outliers
# ============================================================================
example_9 = """
# Load and clean data

from app.ml import load_csv
import numpy as np

df = load_csv("ml-practice/dummy_data.csv")

# Remove duplicates
df = df.drop_duplicates()

# Remove rows where target is null
df = df[df['price'].notna()]

# Remove outliers using IQR method
Q1 = df['price'].quantile(0.25)
Q3 = df['price'].quantile(0.75)
IQR = Q3 - Q1
df = df[(df['price'] >= Q1 - 1.5 * IQR) & (df['price'] <= Q3 + 1.5 * IQR)]

print(f"After cleaning: {len(df)} rows")

target_column = "price"
result = train_model(
    df=df,
    target_column=target_column,
    task="regression",
    test_size=0.2,
    model_name="cleaned_house_model.joblib"
)
"""


# ============================================================================
# HOW TO USE THESE EXAMPLES:
# ============================================================================
"""
1. Copy the code from an example above
2. Replace the corresponding section in train_ml_models.py
3. Update file paths if needed
4. Run: python train_ml_models.py
5. Model will be saved to: FastApi/server/app/ml_models/

NEXT: Create FastAPI endpoint to use these trained models!
"""
