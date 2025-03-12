import databases
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from core.db_config import db_config

SQLALCHEMY_DATABASE_URL = (
    'postgresql://{user}:{password}@{host}:{port}/{dbname}'.format(
        user=db_config.db_user,
        password=db_config.db_password,
        host=db_config.db_host,
        port=db_config.db_port,
        dbname=db_config.db_name,
    )
)

database = databases.Database(SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def create_tables():
    Base.metadata.create_all(bind=engine)
