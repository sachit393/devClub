from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=264)
    author=models.CharField(max_length=264)
    publisher=models.CharField(max_length=264)
    genre=models.CharField(max_length=264)
    summary=models.CharField(max_length=3000)

class User(models.Model):
    name=models.CharField(max_length=264)
    email_id=models.CharField(max_length=300)

class Request(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    name=models.CharField(max_length=264)
    email_id=models.CharField(max_length=264)

class Mybooks(models.Model):
    name=models.CharField(max_length=264)
    book=models.CharField(max_length=264)
    due=models.CharField(max_length=264)
