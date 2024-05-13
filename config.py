from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

# docker run --name university_db -p 5432:5432 -e POSTGRES_PASSWORD=123456789 -d postgres
engine = create_engine('postgresql+psycopg2://postgres:123456789@localhost/postgres', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
