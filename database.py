'''
Plik zawiera konfigurację połączenia z bazą danych
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = 'postgresql://postgres:postgres1@localhost:5432/Quiz'
# DATABASE_URL = "postgresql+psycopg2://postgres:postgres1@localhost/blog_db"

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    print("Uruchamiam apke.")
    try:
        yield db
    finally:
        print("Zamykam apke.")
        db.close()

