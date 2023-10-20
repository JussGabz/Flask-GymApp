from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define the database connection URL
db_url = "postgresql+psycopg2://postgres:admin@localhost/new_gymapp"

# Create the SQLAlchemy engine
engine = create_engine(db_url, echo=True)

Session = sessionmaker(bind=engine)