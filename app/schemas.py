from datetime import datetime
from pickletools import string1
import string
from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from typing_extensions import Annotated

class PostBase(BaseModel):
  pass
  # title: str
  # content: str
  # published: bool = True

class PostCreate(PostBase):
  pass

class UserOut(BaseModel):
  id: int
  email: EmailStr
  created_at: datetime

  class Config:
    orm_mode = True


class Post(PostBase):
  id: int
  title: str
  content: str
  published: bool = True
  created_at: datetime
  owner_id: int
  owner: UserOut
  class Config:
    orm_mode = True


class PostOut(PostBase):
  Post: Post
  votes: int
  class Config:
    orm_mode = True


class UserCreate(BaseModel):
  email: EmailStr
  password: str


class UserLogin(BaseModel):
  email: EmailStr
  password: str

class Token(BaseModel):
  access_token: str
  token_type: str

class TokenData(BaseModel):
  id: Optional[int] = None
  
class Vote(BaseModel):
  post_id: int
  dir: Annotated[int, Field(strict=True, ge=0, le=1)]