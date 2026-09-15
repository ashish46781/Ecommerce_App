from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Path, Response, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.config import settings
from app.database import get_db
from app.models import Category, Product
from app.schemas import (
    CategoryCreate,
    CategoryResponse,
    ProductCreate,
    ProductResponse,
    ProductUpdate,
)

app = FastAPI(title=settings.app_name, debug=settings.debug)


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": settings.app_name}


@app.get("/categories", response_model=list[CategoryResponse])
def list_categories(
    session: Annotated[Session, Depends(get_db)],
) -> list[Category]:
    statement = select(Category).order_by(Category.id)
    return list(session.scalars(statement).all())


@app.post(
    "/categories",
    response_model=CategoryResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_409_CONFLICT: {
            "description": "Category name already exists",
        }
    },
)
def create_category(
    category_data: CategoryCreate,
    session: Annotated[Session, Depends(get_db)],
) -> Category:
    category = Category(**category_data.model_dump())
    session.add(category)

    try:
        session.commit()
    except IntegrityError as error:
        session.rollback()
        diagnostics = getattr(error.orig, "diag", None)
        constraint_name = getattr(diagnostics, "constraint_name", None)
        if constraint_name == "uq_categories_name":
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Category name already exists",
            ) from error
        raise

    session.refresh(category)
    return category


@app.get("/products", response_model=list[ProductResponse])
def list_products(
    session: Annotated[Session, Depends(get_db)],
) -> list[Product]:
    statement = select(Product).order_by(Product.id)
    return list(session.scalars(statement).all())


@app.get(
    "/products/{product_id}",
    response_model=ProductResponse,
    responses={status.HTTP_404_NOT_FOUND: {"description": "Product not found"}},
)
def get_product(
    product_id: Annotated[int, Path(gt=0, le=2_147_483_647)],
    session: Annotated[Session, Depends(get_db)],
) -> Product:
    product = session.get(Product, product_id)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )
    return product


@app.put(
    "/products/{product_id}",
    response_model=ProductResponse,
    responses={status.HTTP_404_NOT_FOUND: {"description": "Product not found"}},
)
def update_product(
    product_id: Annotated[int, Path(gt=0, le=2_147_483_647)],
    product_data: ProductUpdate,
    session: Annotated[Session, Depends(get_db)],
) -> Product:
    product = session.get(Product, product_id)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )

    product.name = product_data.name
    product.description = product_data.description
    product.price = product_data.price
    product.stock = product_data.stock

    session.commit()
    session.refresh(product)
    return product


@app.delete(
    "/products/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={status.HTTP_404_NOT_FOUND: {"description": "Product not found"}},
)
def delete_product(
    product_id: Annotated[int, Path(gt=0, le=2_147_483_647)],
    session: Annotated[Session, Depends(get_db)],
) -> Response:
    product = session.get(Product, product_id)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )

    session.delete(product)
    session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.post(
    "/products",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {
            "headers": {
                "Location": {
                    "description": "Path of the newly created product",
                    "schema": {"type": "string"},
                }
            }
        }
    },
)
def create_product(
    product_data: ProductCreate,
    response: Response,
    session: Annotated[Session, Depends(get_db)],
) -> Product:
    product = Product(**product_data.model_dump())
    session.add(product)
    session.commit()
    session.refresh(product)
    response.headers["Location"] = f"/products/{product.id}"
    return product
