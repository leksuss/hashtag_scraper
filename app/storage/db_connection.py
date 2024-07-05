from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import settings


engine = create_engine(settings.DATABASE_URL, echo=True, future=True)
session = sessionmaker(autoflush=False, bind=engine)()
