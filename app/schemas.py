from pydantic import BaseModel, EmailStr
class AuthorCreate(BaseModel):
    name: str
    email: EmailStr

class AuthorResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True
class PostCreate(BaseModel):
    title: str
    content: str
    author_id: int

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    author: AuthorResponse

    class Config:
        orm_mode = True
