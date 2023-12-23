from pydantic import BaseModel,constr, FilePath
from .models import Author, Book  
from datetime import date
from typing import List
from ninja import NinjaAPI, Schema
class AuthorSchema(BaseModel):
    name: str
    birthdate: date

class PhotoSchema(Schema):
    book_id: int
    cover_image: str

class BookSchema(Schema):
    id: int
    title: str
    description: str
    author_id: int
    isbn: str
    photos: List[PhotoSchema] = []
    

api = NinjaAPI()