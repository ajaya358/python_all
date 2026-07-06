# ML Training Pipeline - Step by Step Guide

## 📁 Folder Structure

```
python/
├── train_ml_models.py          ← Standalone training script (RUN THIS)
├── FastApi/
│   └── server/
│       └── app/
│           ├── ml/                 ← ML helper modules (data_loader, train_model, predict)
│           ├── ml_models/          ← Saved trained models (.joblib files)
│           └── api/                ← FastAPI endpoints (use models here)
└── ml-practice/
    ├── dummy_data.csv             ← Raw CSV data
    ├── dummy_data.json            ← Raw JSON data
    └── house_pd/                  ← Kaggle house dataset (optional)
```

## 🎯 Workflow

### For Data Scientists (Training)
1. **Collect raw data** → `ml-practice/train.csv` or `ml-practice/raw_data.json`
2. **Run training script** → `python train_ml_models.py`
   - Step 1: Load raw data
   - Step 2: Clean data (remove duplicates, handle missing values)
   - Step 3: Train model
   - Step 4: Test predictions
3. **Model gets saved** → `FastApi/server/app/ml_models/house_price_model.joblib`

### For API Developers (Using Models)
1. Model file is already in `ml_models/`
2. In FastAPI endpoint, use:
   ```python
   from app.ml import load_model, predict
   
   model = load_model("house_price_model.joblib")
   result = predict(model, user_input)
   ```
3. Return prediction to user

## 🚀 How to Run Training

```bash
# Make sure you're in the python folder
cd d:\Jayaram\jai\python

# Run the training pipeline
python train_ml_models.py
```

**What happens:**
- ✓ Loads data from `ml-practice/`
- ✓ Shows data statistics
- ✓ Trains model (80% train, 20% test)
- ✓ Shows accuracy (RMSE, R²)
- ✓ Saves model to `FastApi/server/app/ml_models/`

## 📊 Data Files Format

### CSV Format (train.csv)
```csv
square_feet,bedrooms,bathrooms,age,location,price
850,2,1,10,suburb,120000
900,3,2,5,suburb,145000
```

### JSON Format (raw_data.json)
```json
[
  {"square_feet": 850, "bedrooms": 2, "bathrooms": 1, "age": 10, "location": "suburb", "price": 120000},
  {"square_feet": 900, "bedrooms": 3, "bathrooms": 2, "age": 5, "location": "suburb", "price": 145000}
]
```

## 🔧 What Each Module Does

| File | Purpose |
|------|---------|
| `train_ml_models.py` | Standalone script - train models step by step |
| `app/ml/data_loader.py` | Load data from CSV, JSON, or database |
| `app/ml/train_model.py` | Build pipeline, train model, save to disk |
| `app/ml/predict.py` | Load model, make predictions |
| `app/ml_models/` | Where trained models are stored |

## ✅ Next Steps

1. **Add more data**: Put any CSV/JSON data in `ml-practice/`
2. **Modify training script**: Edit `train_ml_models.py` to handle different datasets
3. **Create API endpoint**: In `app/api/`, create endpoint that uses the trained model
4. **Deploy**: Move model file + FastAPI to production server

