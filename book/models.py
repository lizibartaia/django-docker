from django.db import models

# Create your models here.

class Author(models.Model):
    name  = models.CharField(max_length=100,default='Name')
    surname  = models.CharField(max_length=100,default='Surname')
    personal_thoughts = models.TextField()

class Book(models.Model):
    title  = models.CharField(max_length=100,default='Title')
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100,default='Genre')
    release_date = models.DateTimeField()
    personal_thoughts = models.TextField()
     