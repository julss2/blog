'''
Definicje schematów Pydantic -
'''

from pydantic import BaseModel
from datetime import date

class PostBase(BaseModel):
    title: str
    content: str
    created_at: date

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int

    class Config:
        from_attributes = True

# mam to w pliku database.py
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

