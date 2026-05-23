"""Automatic database discovery and training helpers."""
from __future__ import annotations
import os
from typing import Any, Dict, List, Optional

import pandas as pd
from sqlalchemy import create_engine, inspect, text
from sqlalchemy.engine import Engine

from app.ml.data_loader import create_engine_from_url
from app.ml.train_model import train_model

DEFAULT_DB_URL = os.getenv("ML_DATA_DB_URL", "sqlite:///./ml_data.db")


def _get_engine(connection_url: Optional[str] = None) -> Engine:
    return create_engine_from_url(connection_url or DEFAULT_DB_URL)


def discover_tables(connection_url: Optional[str] = None) -> List[Dict[str, Any]]:
    """Discover tables and candidate training columns in the database."""
    engine = _get_engine(connection_url)
    inspector = inspect(engine)
    tables = []

    for table_name in inspector.get_table_names():
        cols = inspector.get_columns(table_name)
        numeric_cols = [
            col["name"]
            for col in cols
            if hasattr(col["type"], "python_type") and col["type"].python_type in (int, float)
        ]
        all_cols = [col["name"] for col in cols]
        with engine.connect() as conn:
            row_count = int(conn.execute(text(f"SELECT COUNT(*) FROM {table_name}")).scalar())

        tables.append(
            {
                "table": table_name,
                "columns": all_cols,
                "numeric_columns": numeric_cols,
                "row_count": row_count,
            }
        )

    return tables


def train_from_table(
    table_name: str,
    target_column: str,
    connection_url: Optional[str] = None,
    sample_size: int = 10000,
    task: str = "regression",
    model_name: str = "auto_model.joblib",
) -> Dict[str, Any]:
    """Train a model from a database table if the requested columns exist."""
    engine = _get_engine(connection_url)
    query = f"SELECT * FROM {table_name} LIMIT {sample_size}"
    df = pd.read_sql_query(text(query), engine)

    if target_column not in df.columns:
        raise ValueError(f"Target column '{target_column}' not found in {table_name}")

    if df[target_column].isna().all():
        raise ValueError(f"Target column '{target_column}' contains only missing values")

    return train_model(df, target_column=target_column, task=task, model_name=model_name)


def inspect_and_train(
    connection_url: Optional[str] = None,
    target_column_names: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Try to discover a suitable dataset and train an automatic model."""
    engine = _get_engine(connection_url)
    inspector = inspect(engine)
    target_column_names = target_column_names or ["target", "label", "price", "amount", "sales"]

    for table_name in inspector.get_table_names():
        df = pd.read_sql_query(text(f"SELECT * FROM {table_name} LIMIT 5000"), engine)
        for candidate in target_column_names:
            if candidate in df.columns and not df[candidate].dropna().empty:
                return {
                    "table": table_name,
                    "target": candidate,
                    "result": train_model(df, target_column=candidate, model_name=f"auto_{table_name}_{candidate}.joblib"),
                }

    return {"status": "no_data", "message": "No candidate target column found for automatic training."}
