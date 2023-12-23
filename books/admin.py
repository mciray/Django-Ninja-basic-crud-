from django.contrib import admin
from .models import Author,Book,Photo
# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('name','birthdate')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','isbn')
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('book_id','cover_image')
