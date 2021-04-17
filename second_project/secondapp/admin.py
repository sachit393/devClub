from django.contrib import admin
from secondapp.models import Book,User,Request,Mybooks,RenewalRequests
from secondapp.modelforms import ModelForm
# Register your models here.
admin.site.register(Book)
admin.site.register(User)
admin.site.register(Request)
admin.site.register(Mybooks)
admin.site.register(RenewalRequests)
