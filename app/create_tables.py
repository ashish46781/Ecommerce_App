from app.database import Base, engine
from app.models import Category, Product


def create_tables() -> None:
    Base.metadata.create_all(
        bind=engine,
        tables=[Category.__table__, Product.__table__],
    )


if __name__ == "__main__":
    create_tables()
