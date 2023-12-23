from django.shortcuts import get_object_or_404
from ninja import NinjaAPI,File,Router
from books.models import Author, Book,Photo
from .pydantic import BookSchema,PhotoSchema
from typing import Dict ,List

api= NinjaAPI()

router = Router()
@api.get("/books/{book_id}")
def book_detail(request,book_id):
    book=Book.objects.filter(id=book_id).first()
    return {
        "id":book.id,
        "title":book.title,
        "author":book.author.id,
        "isbn":book.isbn,

    }

@api.post("/books", response=BookSchema)
def create_books(request, payload: BookSchema):
    author = get_object_or_404(Author, id=payload.author_id)
    book = Book.objects.create(
        title=payload.title,
        description=payload.description,
        author=author,
        isbn=payload.isbn
    )
    return BookSchema.from_django(book)

@api.put("/books/{book_id}", response=BookSchema)
def update_book(request, book_id: int, payload: BookSchema):
    book = get_object_or_404(Book, id=book_id)
    author = get_object_or_404(Author, id=payload.author_id)

    book.title = payload.title
    book.description = payload.description
    book.author = author
    book.isbn = payload.isbn
    book.save()

    return BookSchema.from_django(book)


@api.delete("/books/{book_id}", response=Dict[str, str])
def delete_book(request, book_id: int):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return {"message": "Book deleted successfully"}


@api.post("/photos/")
def create_photo(request, payload: PhotoSchema):
    book = Book.objects.get(id=payload.book_id)
    photo = Photo.objects.create(book=book, cover_image=payload.cover_image)
    return {"id": photo.id, "book_id": photo.book.id, "cover_image": photo.cover_image.url}

@api.get("/books/", response=List[BookSchema])
def list_books(request):
    books = Book.objects.prefetch_related('photos').all()
    return books