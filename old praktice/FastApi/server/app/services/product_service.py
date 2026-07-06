from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.product import Product
from app.schemas.product import ProductCreate
from app.core.exceptions import NotFoundException

def create_product(db: Session, product: ProductCreate):
    new_product = Product(name=product.name, price=product.price, description=product.description)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

def get_products(db: Session, skip: int = 0, limit: int = 10, name: str = None, min_price: float = None, max_price: float = None):
    query = db.query(Product)
    
    if name:
        query = query.filter(Product.name.ilike(f"%{name}%"))
    if min_price is not None:
        query = query.filter(Product.price >= min_price)
    if max_price is not None:
        query = query.filter(Product.price <= max_price)
    
    return query.offset(skip).limit(limit).all()

def get_product(db: Session, product_id: int):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise NotFoundException(f"Product with id {product_id} not found")
    return product

def update_product(db: Session, product_id: int, product: ProductCreate):
    db_product             = get_product(db, product_id)
    db_product.name        = product.name
    db_product.price       = product.price
    db_product.description = product.description
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)
    db.delete(db_product)
    db.commit()
    return {"message": "Product deleted"}
