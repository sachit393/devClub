from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=264)
    author=models.CharField(max_length=264)
    publisher=models.CharField(max_length=264)
    genre=models.CharField(max_length=264)
    summary=models.CharField(max_length=3000)

    def __str__(self):
        return self.title

class User(models.Model):
    name=models.CharField(max_length=264)
    email_id=models.CharField(max_length=300)
    def __str__(self):
        return self.name


class Request(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    name=models.CharField(max_length=264)
    email_id=models.CharField(max_length=264)
    accept=models.BooleanField(default=False)
    due=models.CharField(max_length=200,default='10 days')
    password = models.CharField(max_length=200,default='')

    def __str__(self):
        return f'Name:{self.name}, Book:{ self.book}'

class Mybooks(models.Model):
    name=models.CharField(max_length=264)
    book=models.CharField(max_length=264)
    due=models.CharField(max_length=264,default='10 days')

    def __str__(self):
        return f'Name:{self.name}, Book:{self.book}'


class RenewalRequests(models.Model):
    name=models.CharField(max_length=264)
    book=models.CharField(max_length=264)
    renewal_time=models.CharField(max_length=264)
    accept=models.BooleanField(default=False)

    def __str__(self):
        return f'Name:{self.name}, Book:{self.book}'

class Ratings(models.Model):
    name=models.CharField(max_length=264)
    book=models.CharField(max_length=264)
    comments=models.CharField(max_length=3000,default='')
    SCORE_CHOICES = zip(range(1, 6), range(1, 6))
    stars = models.IntegerField(choices=SCORE_CHOICES, default=3)
    def __str__(self):
        return f'Name:{self.name}, Book:{self.book},Stars:{self.stars}'
    
class Warnings(models.Model):
    name=models.CharField(max_length=264)
    warning=models.TextField(max_length=3000)
    def __str__(self):
        return f'Name:{self.name}'
