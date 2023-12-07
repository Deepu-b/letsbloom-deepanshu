from django.db import models

# Create your models here.
class Book(models.Model):
    book_id = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    