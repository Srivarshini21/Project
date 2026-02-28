from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import OperationalError
import time
from src.config import DATABASE_URL

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def init_db():
    from src.models.user import User
    from src.models.product import Product
    from src.models.order import Order

    last_error = None
    for _ in range(20):
        try:
            Base.metadata.create_all(bind=engine)
            return
        except OperationalError as exc:
            last_error = exc
            time.sleep(2)

    raise RuntimeError("Database is not ready after waiting") from last_error

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()