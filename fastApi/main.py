from fastapi import FastAPI
import uvicorn
import logging
import sys
from app.db.mongo import connect_to_mongo, close_mongo_connection
# from app.db.postgres import engine, Base

app = FastAPI()

# Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("uvicorn")

@app.on_event("startup")
async def startup_db():
    # 1. Connect to MongoDB
    await connect_to_mongo()
    
    # 2. Setup PostgreSQL Tables
    # This checks your 'models' and creates tables in Postgres if they are missing
    # Base.metadata.create_all(bind=engine)
    # logger.info("✅ PostgreSQL Tables Checked/Created")
    logger.info("🚀 All systems are go!")

@app.on_event("shutdown")
async def shutdown_db():
    await close_mongo_connection()

@app.get("/")
async def root():
    logger.info("Root API request processed.")
    return {"message": "FastAPI Server with Dual DB (Mongo + Postgres) is working"}

@app.get("/status")
async def status():
    return {"status": "running and healthy", "databases": ["mongodb", "postgresql"]}

if __name__ == "__main__":
    logger.info("Starting FastAPI server...")
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)