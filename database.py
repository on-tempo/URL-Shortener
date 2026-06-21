from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite database file location (creates urls.db in the project folder)
DATABASE_URL = "sqlite:///./urls.db"

# Create the DB engine (SQLite needs this connect_args option)
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Session factory: each request borrows one DB session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class that all table models will inherit from
Base = declarative_base()

# Hands out a DB session per request and closes it when done
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()