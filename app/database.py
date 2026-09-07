from collections.abc import Generator

from sqlalchemy import URL, create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.config import settings


class Base(DeclarativeBase):
    pass


database_url = URL.create(
    drivername="postgresql+psycopg",
    username=settings.database_user,
    password=settings.database_password.get_secret_value(),
    host=settings.database_host,
    port=settings.database_port,
    database=settings.database_name,
)

engine = create_engine(database_url)
SessionFactory = sessionmaker(bind=engine)


def get_db() -> Generator[Session, None, None]:
    with SessionFactory() as session:
        yield session
