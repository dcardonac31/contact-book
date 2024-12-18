from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import Config
import psycopg2

# Create the base class for entities
Base = declarative_base()

# Create the engine to connect to the database
engine = create_engine(
    f"postgresql+psycopg2://{Config.DB_USER}:{Config.DB_PASSWORD}@{Config.DB_HOST}:{Config.DB_PORT}/{Config.DB_NAME}",
    echo=True,
    pool_pre_ping=True
)

# Create the session local object to manage the session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Function to get the session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# Function to init the tables in the database
def init_db():
    Base.metadata.create_all(bind=engine)