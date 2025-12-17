from fastapi import FastAPI
from app.database import engine
from app import models
from app.routers import author, posts

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Blog API")

app.include_router(author.router)
app.include_router(posts.router)
