"""Training utilities for scikit-learn models."""
from __future__ import annotations
import os
from pathlib import Path
from typing import Any, Dict, List, Optional

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error, accuracy_score, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

MODEL_DIR = Path(os.getenv("ML_MODEL_DIR", "ml_models"))
MODEL_DIR.mkdir(parents=True, exist_ok=True)


def _build_pipeline(numeric_features: List[str], categorical_features: List[str], task: str = "regression") -> Pipeline:
    numeric_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )

    categorical_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoder", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ("cat", categorical_transformer, categorical_features),
        ]
    )

    if task == "classification":
        model = RandomForestClassifier(n_estimators=100, random_state=42)
    else:
        model = RandomForestRegressor(n_estimators=100, random_state=42)

    return Pipeline(steps=[("preprocessor", preprocessor), ("model", model)])


def train_model(
    df: pd.DataFrame,
    target_column: str,
    feature_columns: Optional[List[str]] = None,
    task: str = "regression",
    test_size: float = 0.2,
    random_state: int = 42,
    model_name: str = "model.joblib",
) -> Dict[str, Any]:
    """Train a model from a DataFrame and save the result."""
    if feature_columns is None:
        feature_columns = [col for col in df.columns if col != target_column]

    X = df[feature_columns]
    y = df[target_column]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    numeric_features = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
    categorical_features = X.select_dtypes(include=["object", "category", "bool"]).columns.tolist()

    pipeline = _build_pipeline(numeric_features, categorical_features, task=task)
    pipeline.fit(X_train, y_train)

    predictions = pipeline.predict(X_test)
    results: Dict[str, Any] = {"model_path": str(MODEL_DIR / model_name)}

    if task == "classification":
        results["accuracy"] = accuracy_score(y_test, predictions)
    else:
        results["rmse"] = mean_squared_error(y_test, predictions, squared=False)
        results["r2"] = r2_score(y_test, predictions)

    joblib.dump(pipeline, MODEL_DIR / model_name)
    return results


def save_model(model: Any, path: str) -> str:
    """Save a trained model to disk."""
    output_path = MODEL_DIR / path
    joblib.dump(model, output_path)
    return str(output_path)


def load_saved_model(path: str) -> Any:
    """Load a saved model from disk."""
    return joblib.load(MODEL_DIR / path)
