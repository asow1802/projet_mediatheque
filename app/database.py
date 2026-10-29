from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


# SQLite
DATABASE_URL = "sqlite:///./mediatheque.db"
engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
#db = SessionLocal()

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

if __name__ == "__main__": 
    with engine.connect() as connection:
        result = connection.exec_driver_sql("SELECT 1")
        print(result.scalar())
        

