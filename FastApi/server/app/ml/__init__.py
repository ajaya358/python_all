"""ML helper package for the FastAPI application."""
from app.ml.data_loader import create_engine_from_url, load_csv, load_data_from_db, list_db_tables, load_table_from_db
from app.ml.train_model import train_model, save_model, load_saved_model
from app.ml.predict import load_model, predict, predict_from_file
from app.ml.db_auto_train import discover_tables, train_from_table, inspect_and_train
from app.ml.chat_agent import ChatAgent

__all__ = [
    "create_engine_from_url",
    "load_csv",
    "load_data_from_db",
    "list_db_tables",
    "load_table_from_db",
    "train_model",
    "save_model",
    "load_saved_model",
    "load_model",
    "predict",
    "predict_from_file",
    "discover_tables",
    "train_from_table",
    "inspect_and_train",
    "ChatAgent",
]
