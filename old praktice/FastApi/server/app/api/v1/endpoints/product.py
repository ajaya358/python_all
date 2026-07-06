from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from app.db.db import get_product_db
from app.schemas.product import ProductCreate, ProductResponse
from app.services import product_service
from app.tasks.background_tasks import update_inventory

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/", response_model=ProductResponse)
def create_product(product: ProductCreate, background_tasks: BackgroundTasks, db: Session = Depends(get_product_db)):
    new_product = product_service.create_product(db, product)
    background_tasks.add_task(update_inventory, new_product.name)
    return new_product

@router.get("/", response_model=list[ProductResponse])
def get_products(
    skip: int = 0,
    limit: int = 10,
    name: str = None,
    min_price: float = None,
    max_price: float = None,
    db: Session = Depends(get_product_db)
):
    return product_service.get_products(db, skip, limit, name, min_price, max_price)

@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_product_db)):
    return product_service.get_product(db, product_id)

@router.put("/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product: ProductCreate, db: Session = Depends(get_product_db)):
    return product_service.update_product(db, product_id, product)

@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_product_db)):
    return product_service.delete_product(db, product_id)
