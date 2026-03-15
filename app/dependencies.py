from app import models
from app.database import SessionLocal
from app.models import Product

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


products = [
    Product(id=1, name="phone", description="budget phone", price=99, quantity=10),
    Product(id=2, name="laptop", description="gaming laptop", price=999, quantity=5),
    Product(id=3, name="watch", description="casio", price=199, quantity=1),
    Product(id=4, name="iphone", description="iphone 17 pro max", price=200, quantity=1),
]

def init_db():
    db = SessionLocal()

    count = db.query(models.Product).count()

    if count == 0:
        for product in products:
            db.add(models.Product(**product.model_dump())) 
        db.commit()

init_db()