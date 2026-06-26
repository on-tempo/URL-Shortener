import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Read the database URL from the environment (set by docker-compose).
# Fall back to a local default so it still runs outside Docker if needed.
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/urlshortener")

# Create the DB engine (no SQLite-specific connect_args anymore)
engine = create_engine(DATABASE_URL)

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