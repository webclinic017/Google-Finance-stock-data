# Database Connection is here
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import psycopg2.extras


DATABASE_URL = "postgresql://postgres:yuviboxer@localhost/google_finance"


engine=create_engine(DATABASE_URL,echo=True)

sessionLocal = sessionmaker(bind=engine)

conn=psycopg2.connect('postgresql://postgres:yuviboxer@localhost/google_finance')

Base = declarative_base()

# Base.metadata.create_all(engine)
# print("Created DataBase ....")