from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session, joinedload

from app.database import SessionLocal
from app import models, schemas

router = APIRouter(prefix="/posts", tags=["Posts"])

# ✅ ADD THIS (you forgot it)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.PostResponse)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    author = db.query(models.Author).get(post.author_id)
    if not author:
        raise HTTPException(status_code=400, detail="Author does not exist")

    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get("/", response_model=list[schemas.PostResponse])
def get_posts(
    author_id: int | None = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(models.Post).options(joinedload(models.Post.author))

    if author_id:
        query = query.filter(models.Post.author_id == author_id)

    return query.all()
