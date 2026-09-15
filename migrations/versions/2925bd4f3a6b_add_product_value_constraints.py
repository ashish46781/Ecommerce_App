"""add product value constraints

Revision ID: 2925bd4f3a6b
Revises: 0e449183369b
Create Date: 2026-09-16 03:32:19.221088

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "2925bd4f3a6b"
down_revision: Union[str, Sequence[str], None] = "0e449183369b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_check_constraint(
        "ck_products_price_positive",
        "products",
        "price > 0",
    )
    op.create_check_constraint(
        "ck_products_stock_non_negative",
        "products",
        "stock >= 0",
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(
        "ck_products_stock_non_negative",
        "products",
        type_="check",
    )
    op.drop_constraint(
        "ck_products_price_positive",
        "products",
        type_="check",
    )
