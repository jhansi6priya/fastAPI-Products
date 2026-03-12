from fastapi import Depends, FastAPI
from models import Product
from database import Session, engine
import database_models

app = FastAPI()

database_models.Base.metadata.create_all(bind = engine)

@app.get("/")
def greet():
    return "Welcome to Amazon"

products = [
    Product(id=1, name="phone", description="budget phone", price=99, quantity=10),
    Product(id=2, name="laptop", description="gaming laptop", price=999, quantity=5),
    Product(id=3, name="watch", description="casio", price=199, quantity=1),
    Product(id=4, name="iphone", description="iphone 17 pro max", price=200, quantity=1),
]

#to connect to the DB once instead of creating a session every single time
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = Session()

    count = db.query(database_models.Product).count

    if count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump())) 
        db.commit()

init_db()
#DB connection
#query 


@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    db_products = db.query(database_models.Product).all()
    return db_products

@app.get("/product/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        return db_product
    else:
        return "product not found"

@app.post("/product")
def add_product(product: Product, db: Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump())) 
    db.commit()
    return product

@app.put("/product")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return "Product updated"
    else:
        return "No product Found"

@app.delete("/product")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
    else:
        return "Product not Found"