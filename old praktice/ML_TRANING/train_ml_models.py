"""
Step-by-step ML training script (runs outside FastAPI)
Raw data → Data Cleaning → Model Training → Save Model

This script:
1. Loads raw CSV/JSON data from ml-practice/
2. Cleans and prepares data
3. Trains models step by step
4. Saves trained models to FastApi/server/app/ml_models/
"""

import os
import sys
from pathlib import Path
from typing import Dict, Tuple, Any

import pandas as pd

# Add FastAPI app to path so we can import ml modules
fastapi_root = Path(__file__).resolve().parent / "FastApi" / "server"
sys.path.insert(0, str(fastapi_root))

from app.ml import (
    load_csv,
    load_json,
    train_model,
    save_model,
    load_saved_model,
)

# Paths
ML_DATA_DIR = Path(__file__).resolve().parent / "ml-practice"
ML_MODELS_DIR = fastapi_root / "app" / "ml_models"

print("=" * 70)
print("ML TRAINING PIPELINE - Step by Step")
print("=" * 70)


# STEP 1: Load Raw Data
def step_1_load_data() -> pd.DataFrame:
    """Load raw data from CSV or JSON file."""
    print("\n[STEP 1] Loading Raw Data")
    print("-" * 70)
    
    csv_path = ML_DATA_DIR / "dummy_data.csv"
    json_path = ML_DATA_DIR / "dummy_data.json"
    
    if csv_path.exists():
        print(f"✓ Found CSV file: {csv_path}")
        df = load_csv(str(csv_path))
    elif json_path.exists():
        print(f"✓ Found JSON file: {json_path}")
        df = load_json(str(json_path))
    else:
        raise FileNotFoundError(f"No data file found in {ML_DATA_DIR}")
    
    print(f"✓ Loaded {len(df)} rows, {len(df.columns)} columns")
    print(f"  Columns: {list(df.columns)}")
    print(f"\nFirst 3 rows:")
    print(df.head(3).to_string())
    
    return df


# STEP 2: Explore and Clean Data
def step_2_clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and prepare data for training."""
    print("\n[STEP 2] Data Cleaning & Exploration")
    print("-" * 70)
    
    print(f"✓ Dataset shape: {df.shape}")
    print(f"✓ Data types:\n{df.dtypes.to_string()}")
    
    # Check for missing values
    missing = df.isnull().sum()
    if missing.any():
        print(f"⚠ Missing values found:")
        print(missing[missing > 0].to_string())
    else:
        print("✓ No missing values")
    
    # Check for duplicates
    duplicates = df.duplicated().sum()
    if duplicates > 0:
        print(f"⚠ Found {duplicates} duplicate rows")
        df = df.drop_duplicates()
        print(f"✓ Removed duplicates. New shape: {df.shape}")
    else:
        print("✓ No duplicate rows")
    
    # Basic statistics
    print(f"\n✓ Data Statistics:")
    print(df.describe().to_string())
    
    return df


# STEP 3: Train Model
def step_3_train_model(df: pd.DataFrame, target_col: str, model_name: str) -> Dict[str, Any]:
    """Train a regression model on the data."""
    print(f"\n[STEP 3] Training Model - Predicting '{target_col}'")
    print("-" * 70)
    
    print(f"Target column: {target_col}")
    print(f"Model file: {model_name}")
    
    result = train_model(
        df=df,
        target_column=target_col,
        task="regression",
        test_size=0.2,
        model_name=model_name
    )
    
    print(f"✓ Model trained successfully!")
    print(f"  RMSE: {result.get('rmse', 'N/A'):.4f}")
    print(f"  R² Score: {result.get('r2', 'N/A'):.4f}")
    print(f"  Saved to: {result['model_path']}")
    
    return result


# STEP 4: Test Model Predictions
def step_4_test_predictions(model_name: str) -> None:
    """Load model and make test predictions."""
    print(f"\n[STEP 4] Testing Model Predictions")
    print("-" * 70)
    
    model = load_saved_model(model_name)
    print(f"✓ Loaded model: {model_name}")
    
    # Test prediction with sample data
    test_input = {
        "square_feet": 1200,
        "bedrooms": 3,
        "bathrooms": 2,
        "age": 10,
        "location": "suburb"
    }
    
    print(f"\nTest input: {test_input}")
    
    from app.ml.predict import predict
    prediction = predict(model, test_input)
    
    print(f"✓ Predicted price: ${prediction[0]:.2f}")


# MAIN EXECUTION
def main():
    """Run the complete training pipeline."""
    try:
        # Step 1: Load data
        df = step_1_load_data()
        
        # Step 2: Clean data
        df = step_2_clean_data(df)
        
        # Step 3: Train model
        result = step_3_train_model(
            df=df,
            target_col="price",
            model_name="house_price_model.joblib"
        )
        
        # Step 4: Test predictions
        step_4_test_predictions("house_price_model.joblib")
        
        print("\n" + "=" * 70)
        print("✅ TRAINING PIPELINE COMPLETED SUCCESSFULLY")
        print("=" * 70)
        print(f"\n📁 Models saved to: {ML_MODELS_DIR}")
        print(f"📊 Model ready for FastAPI to use!")
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        raise


if __name__ == "__main__":
    main()
