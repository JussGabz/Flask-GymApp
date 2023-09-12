from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql+psycopg2://postgres:admin@localhost/new_gymapp")

# Test connection 

with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())

