from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    birthdate = models.DateField()

class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=50)

class Photo(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='photos')
    cover_image = models.ImageField(upload_to='book_covers/')