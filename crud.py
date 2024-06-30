'''
Funkcje CRUD - Create, Read, Update, Delete - do zarządzania postami w bazie danych
'''

from sqlalchemy.orm import Session # zarządzanie transakcjami z bazą
import models, schemas
from datetime import date

def get_post(db: Session, post_id: int):
    return db.query(models.Post).filter(models.Post.id == post_id).first()

def get_posts(db: Session):
    return db.query(models.Post).order_by(models.Post.created_at.desc()).all()

def create_post(db: Session, post: schemas.PostCreate):
    db_post = models.Post(title=post.title, content=post.content, created_at=date.today())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def update_post(db: Session, post_id: int, post: schemas.PostCreate):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if db_post:
        db_post.title = post.title
        db_post.content = post.content
        db.commit()
        db.refresh(db_post)
    return db_post

def delete_post(db: Session, post_id: int):
    print("crud>delete_post> początek")
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if db_post:
        db.delete(db_post)
        db.commit()
    print("crud>delete_post> koniec")
    return db_post

