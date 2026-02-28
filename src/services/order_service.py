from sqlalchemy.orm import Session
from src.models.order import Order


def create_order(db: Session, order_data):
    new_order = Order(
        user_id=order_data.user_id,
        product_id=order_data.product_id,
        quantity=order_data.quantity
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order


def get_orders(db: Session):
    return db.query(Order).all()