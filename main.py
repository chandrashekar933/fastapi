from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import SessionLocal, engine
from models import Base, Product


Base.metadata.create_all(engine)

app = FastAPI(title="Cafe")
templates = Jinja2Templates(directory="templates")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={"cafe_name": "Python Cafe"},
    )


@app.get("/products", response_class=HTMLResponse)
def products(request: Request, db: Session = Depends(get_db)):
    items = db.scalars(select(Product).order_by(Product.id)).all()
    return templates.TemplateResponse(
        request=request,
        name="products.html",
        context={"cafe_name": "Python Cafe", "items": items},
    )