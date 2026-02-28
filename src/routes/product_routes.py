from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.models.product import Product
from src.schemas.product import ProductCreate
from src.database import get_db
router = APIRouter()

@router.post("/products")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    new_product = Product(name=product.name, price=product.price)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return {
        "id": new_product.id,
        "name": new_product.name,
        "price": new_product.price,
    }


@router.get("/products")
def get_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return [
        {
            "id": product.id,
            "name": product.name,
            "price": product.price,
        }
        for product in products
    ]