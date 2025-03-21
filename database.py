import logging
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()
# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")

# Attempt to create the database engine with error handling
try:
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    logger.info("Database connection established successfully.")
except Exception as e:
    logger.error("Failed to connect to the database", exc_info=True)
    raise

Base = declarative_base()

def get_db():
    """Provides a database session, ensuring proper closure."""
    db = None
    try:
        db = SessionLocal()
        yield db
    except Exception as e:
        logger.error("Database session error", exc_info=True)
        raise
    finally:
        if db:
            db.close()
            logger.info("Database session closed.")
