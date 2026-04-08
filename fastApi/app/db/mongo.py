from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings
import logging

logger = logging.getLogger('uvicorn.error')

class MongoDB:
    client: AsyncIOMotorClient = None
    # Instead of one 'db', we define slots for multiple databases
    main_db = None
    network_db = None
    analytics_db = None  # You can add a 3rd or 4th here

db_context = MongoDB()

async def connect_to_mongo():
    try:
        # 1. Establish the single connection to the cluster
        db_context.client = AsyncIOMotorClient(settings.MONGO_URL)
        
        # 2. Access different databases using the SAME client
        # In Node, this was: db.useDb('name')
        # In Motor, it is just: client['name']
        db_context.main_db = db_context.client[settings.MONGO_DB]
        """ db_context.network_db = db_context.client[settings.MONGO_DB_NETWORK] """
        db_context.analytics_db = db_context.client["analytics_logs"] # Example of a 3rd DB
        
        # Verify connection
        await db_context.client.admin.command('ping')
        logger.info("✅ Connected to MongoDB Cluster (Main, Network, and Analytics DBs)")
        
    except Exception as e:
        logger.error(f"❌ MongoDB Connection Error: {e}")
        raise e

async def close_mongo_connection():
    if db_context.client:
        db_context.client.close()
        logger.info("🔌 All MongoDB connections closed.")

# Helper functions to get specific DBs in your routes
def get_main_db():
    return db_context.main_db

""" def get_network_db():
    return db_context.network_db """

def get_analytics_db():
    return db_context.analytics_db