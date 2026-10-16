
from sqlalchemy import select

from database import SessionLocal, engine
from models import Base, Product

Base.metadata.create_all(engine)

items = [
    ("Espresso", 120),
    ("Cappuccino", 160),
    ("Latte", 180),
    ("Cold Coffee", 190),
    ("Veg Sandwich", 140),
    ("Chocolate Brownie", 110),
]

with SessionLocal() as db:
    if db.scalars(select(Product)).first():
        print("Table already has items, nothing added.")
    else:
        db.add_all([Product(name=n, price=p) for n, p in items])
        db.commit()
        print(f"Added {len(items)} items.")