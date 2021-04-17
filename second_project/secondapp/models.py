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
    def __str__(self):
        return self.name

class Mybooks(models.Model):
    name=models.CharField(max_length=264)
    book=models.CharField(max_length=264)
    due=models.CharField(max_length=264)

    def __str__(self):
        return self.name

class RenewalRequests(models.Model):
    name=models.CharField(max_length=264)
    book=models.CharField(max_length=264)
    renewal_time=models.CharField(max_length=264)
    accept=models.BooleanField(default=False)

    def __str__(self):
        return self.name