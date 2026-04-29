import logging
import time

logger = logging.getLogger(__name__)

def send_welcome_email(email: str, name: str):
    time.sleep(2)  # Simulate email sending delay
    logger.info(f"📧 Welcome email sent to {email} (User: {name})")

def update_inventory(product_name: str):
    time.sleep(1)  # Simulate inventory update
    logger.info(f"📦 Inventory updated for product: {product_name}")
