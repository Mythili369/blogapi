from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app import models, schemas

router = APIRouter(prefix="/authors", tags=["Authors"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.AuthorResponse)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    new_author = models.Author(**author.dict())
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author

@router.get("/", response_model=list[schemas.AuthorResponse])
def get_authors(db: Session = Depends(get_db)):
    return db.query(models.Author).all()

@router.delete("/{id}")
def delete_author(id: int, db: Session = Depends(get_db)):
    author = db.query(models.Author).get(id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")

    db.delete(author)
    db.commit()
    return {"message": "Author deleted"}

# ✅ Nested Resource Endpoint
@router.get("/{id}/posts")
def get_author_posts(id: int, db: Session = Depends(get_db)):
    author = db.query(models.Author).get(id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")

    return author.posts
