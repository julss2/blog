'''
Główna aplikacja FasAPI

'''
import logging
from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
import schemas, crud
from database import engine, Base, get_db
from datetime import datetime

# Konfiguracja logowania
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

Base.metadata.create_all(bind=engine)

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/posts/", response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    print()
    return crud.create_post(db=db, post=post)

@app.get("/posts/", response_model=list[schemas.Post])
def read_posts(db: Session = Depends(get_db)):
    posts = crud.get_posts(db)
    return posts

@app.put("/posts/{post_id}", response_model=schemas.Post)
def update_post(post_id: int, post: schemas.PostCreate, db: Session = Depends(get_db)):
    db_post = crud.get_post(db, post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return crud.update_post(db=db, post=post, post_id=post_id)

@app.delete("/posts/{post_id}", response_model=schemas.Post)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    logger.info("main>delete_post> początek")
    db_post = crud.get_post(db=db, post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    logger.info("crud>delete_post> koniec")
    return crud.delete_post(db=db, post_id=post_id)