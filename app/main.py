from typing import Annotated

from fastapi import Depends, FastAPI, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.config import settings
from app.database import get_db
from app.models import Product
from app.schemas import ProductCreate, ProductResponse

app = FastAPI(title=settings.app_name, debug=settings.debug)


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": settings.app_name}


@app.get("/products", response_model=list[ProductResponse])
def list_products(
    session: Annotated[Session, Depends(get_db)],
) -> list[Product]:
    statement = select(Product).order_by(Product.id)
    return list(session.scalars(statement).all())


@app.post(
    "/products",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_product(
    product_data: ProductCreate,
    session: Annotated[Session, Depends(get_db)],
) -> Product:
    product = Product(**product_data.model_dump())
    session.add(product)
    session.commit()
    session.refresh(product)
    return product
