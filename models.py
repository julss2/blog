'''
Definicje modeli SQLAlchemy
'''

from sqlalchemy import Column, Integer, String, Text, DateTime, Date
from sqlalchemy.sql import func
from database import Base
from datetime import date

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text, index=True)
    created_at = Column(Date)


# class Choices(Base):
#     __tablename__ = 'choices'

#     id = Column(Integer, primary_key=True, index=True)
#     choice_text = Column(String, index=True)
#     is_correct = Column(Boolean, default=False)
#     question_id = Column(Integer, ForeignKey("questions.id"))

