"""add category relationship to products

Revision ID: 0e449183369b
Revises: e72c0d41701f
Create Date: 2026-09-15 17:12:53.621319

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "0e449183369b"
down_revision: Union[str, Sequence[str], None] = "e72c0d41701f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "products",
        sa.Column("category_id", sa.Integer(), nullable=True),
    )
    op.create_index(
        "ix_products_category_id",
        "products",
        ["category_id"],
        unique=False,
    )
    op.create_foreign_key(
        "fk_products_category_id_categories",
        "products",
        "categories",
        ["category_id"],
        ["id"],
        ondelete="RESTRICT",
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(
        "fk_products_category_id_categories",
        "products",
        type_="foreignkey",
    )
    op.drop_index("ix_products_category_id", table_name="products")
    op.drop_column("products", "category_id")
