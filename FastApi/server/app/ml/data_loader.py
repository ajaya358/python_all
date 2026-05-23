"""ML data loading helpers for CSV and database sources."""
from __future__ import annotations
import os
from typing import Any, Dict, List, Optional, Tuple

import pandas as pd
from sqlalchemy import create_engine, inspect, text
from sqlalchemy.engine import Engine

DEFAULT_SQLITE_URL = os.getenv("ML_DATA_DB_URL", "sqlite:///./ml_data.db")


def create_engine_from_url(url: str = DEFAULT_SQLITE_URL) -> Engine:
    return create_engine(url, echo=False, future=True)


def load_csv(path: str, **kwargs: Any) -> pd.DataFrame:
    """Load a CSV file into a pandas DataFrame."""
    return pd.read_csv(path, **kwargs)


def load_train_test_csv(
    train_path: str,
    test_path: str,
    **kwargs: Any,
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Load separate train and test CSV files."""
    train_df = pd.read_csv(train_path, **kwargs)
    test_df = pd.read_csv(test_path, **kwargs)
    return train_df, test_df


def list_db_tables(connection_url: Optional[str] = None) -> List[str]:
    """Return table names for a SQL database."""
    engine = create_engine_from_url(connection_url or DEFAULT_SQLITE_URL)
    inspector = inspect(engine)
    return inspector.get_table_names()


def load_data_from_db(
    query: str,
    connection_url: Optional[str] = None,
    **kwargs: Any,
) -> pd.DataFrame:
    """Load a query result from a SQL database into a DataFrame."""
    engine = create_engine_from_url(connection_url or DEFAULT_SQLITE_URL)
    with engine.connect() as conn:
        return pd.read_sql_query(text(query), conn, **kwargs)


def load_table_from_db(
    table_name: str,
    connection_url: Optional[str] = None,
    limit: Optional[int] = None,
) -> pd.DataFrame:
    """Load an entire table from a SQL database."""
    engine = create_engine_from_url(connection_url or DEFAULT_SQLITE_URL)
    query = f"SELECT * FROM {table_name}"
    if limit is not None:
        query += f" LIMIT {limit}"
    with engine.connect() as conn:
        return pd.read_sql_query(text(query), conn)
