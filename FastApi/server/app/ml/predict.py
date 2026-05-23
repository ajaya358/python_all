"""Prediction utilities for loaded ML models."""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Union

import joblib
import pandas as pd
from pathlib import Path
import os

MODEL_DIR = Path(os.getenv("ML_MODEL_DIR", "ml_models"))


def load_model(model_path: str) -> Any:
    """Load a saved model file from disk."""
    full_path = MODEL_DIR / model_path
    return joblib.load(full_path)


def predict(model: Any, raw_input: Union[Dict[str, Any], List[Dict[str, Any]]]) -> List[Any]:
    """Run prediction on a model using a dictionary or list of dictionaries."""
    if isinstance(raw_input, dict):
        raw_input = [raw_input]

    df = pd.DataFrame(raw_input)
    return model.predict(df).tolist()


def predict_from_file(model: Any, csv_path: str, **kwargs: Any) -> List[Any]:
    """Run predictions from a CSV file."""
    df = pd.read_csv(csv_path, **kwargs)
    return model.predict(df).tolist()
