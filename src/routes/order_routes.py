from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.database import get_db
from src.schemas.order import OrderCreate
from src.services.order_service import create_order, get_orders
router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/")
def create(order: OrderCreate, db: Session = Depends(get_db)):
    try:
        return create_order(db, order)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Invalid user_id or product_id. Please use existing records.",
        )


@router.get("/")
def read(db: Session = Depends(get_db)):
    return get_orders(db)