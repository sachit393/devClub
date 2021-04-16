from django.contrib import admin
from secondapp.models import Book,User,Request
from secondapp.modelforms import ModelForm
# Register your models here.
admin.site.register(Book)
admin.site.register(User)
admin.site.register(Request)