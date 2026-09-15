from decimal import Decimal

from sqlalchemy import (
    CheckConstraint,
    ForeignKey,
    Identity,
    Numeric,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Category(Base):
    __tablename__ = "categories"
    __table_args__ = (
        CheckConstraint(
            "length(btrim(name)) > 0",
            name="ck_categories_name_not_blank",
        ),
        UniqueConstraint("name", name="uq_categories_name"),
    )

    id: Mapped[int] = mapped_column(Identity(), primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str | None] = mapped_column(Text)
    products: Mapped[list["Product"]] = relationship(
        back_populates="category",
        passive_deletes="all",
    )


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Identity(), primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    description: Mapped[str | None] = mapped_column(Text)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    stock: Mapped[int]
    category_id: Mapped[int | None] = mapped_column(
        ForeignKey(
            "categories.id",
            name="fk_products_category_id_categories",
            ondelete="RESTRICT",
        ),
        index=True,
    )
    category: Mapped[Category | None] = relationship(back_populates="products")
