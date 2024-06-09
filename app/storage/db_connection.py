from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import settings


engine = create_engine(settings.DATABASE_URL, echo=True, future=True)
db_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = db_session()
    try:
        yield db
    finally:
        db.close()
