from django.shortcuts import render
from . import forms
from django import forms

from . import modelforms
from . import  models
from django.core import validators

# Create your views here.


def index(request):

    return render(request,'secondapp/index.html')

def registrationform(request):
    form=modelforms.ModelForm()
    if request.method == 'POST':
        form=modelforms.ModelForm(request.POST)

        if form.is_valid():
                #do something after receiving data
                print("validation success")
                form.save(commit=True)

                return index(request)


    return render(request,'secondapp/Registration.html',{'registrationform':form})

def action_books_view(request):
    books1 = models.Book.objects.filter(genre='action')
    dict1={
        'books':books1,

    }
    return render(request,'secondapp/books.html',context=dict1)

def fiction_books_view(request):
    books2 = models.Book.objects.filter(genre='fiction')
    dict2={
        'books':books2,
    }
    return render(request,'secondapp/books.html',context=dict2)

def drama_books_view(request):
    books3 = models.Book.objects.filter(genre='drama')
    dict3={
        'books':books3,
    }
    return render(request,'secondapp/books.html',context=dict3)

def motivation_books_view(request):
    books4 = models.Book.objects.filter(genre='motivation')
    dict4={
        'books':books4,
    }
    return render(request,'secondapp/books.html',context=dict4)

def acads_books_view(request):
    books5 = models.Book.objects.filter(genre='acads')
    dict5={
        'books':books5,
    }
    return render(request,'secondapp/books.html',context=dict5)

def book(request,booktitle):
    book=models.Book.objects.get(title=booktitle)
    dict1={
        'title':book.title,
        'author':book.author,
        'publisher':book.publisher,
        'genre':book.genre,
        'summary':book.summary,
    }

    return render(request,'secondapp/book.html',dict1)

def request_book(request):
    form=modelforms.BorrowForm()
    if request.method == 'POST':
        form=modelforms.BorrowForm(request.POST)
        print(form)
        namelist=models.User.objects.all()
        print(namelist[1].name)
        print(form.cleaned_data['name'])
        if form.is_valid():

            for user in namelist:
                if user.name==form.cleaned_data['name']:
                            form.save(commit=True)
                            #do something after receiving data
                            # print("validation success")
                            return index(request)



    dict={
        'form':form,
    }
    return render(request,'secondapp/Borrow.html',dict)
# def form_name_view(request):
#     form=forms.FormName()
# #to check that somebody has actually posted /submittedsomething
#     if request.method=='POST':
#         form=forms.FormName(request.POST)
#
#         if form.is_valid():
#             #do something after receiving data
#             print("validation success")
#             print(form.cleaned_data['name'])
#             print(form.cleaned_data['email'])



    #
    #
    # return render(request,'secondapp/books.html',{'form':form})