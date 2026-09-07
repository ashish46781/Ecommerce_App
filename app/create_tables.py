from app.database import Base, engine
from app.models import Product


def create_tables() -> None:
    Base.metadata.create_all(bind=engine, tables=[Product.__table__])


if __name__ == "__main__":
    create_tables()
