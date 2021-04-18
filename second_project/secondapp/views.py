from django.shortcuts import render
from . import forms
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from . import modelforms
from . import  models

from django.core import validators

# Create your views here.


def index(request):
    new_books=models.NewArrivals.objects.all()
    dict={
        'newbooks':new_books
    }
    return render(request,'secondapp/index.html',dict)

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
        'genre':'Action'

    }
    return render(request,'secondapp/books.html',context=dict1)

def fiction_books_view(request):
    books2 = models.Book.objects.filter(genre='fiction')
    dict2={
        'books':books2,
        'genre': 'Fiction'
    }
    return render(request,'secondapp/books.html',context=dict2)

def drama_books_view(request):
    books3 = models.Book.objects.filter(genre='drama')
    dict3={
        'books':books3,
        'genre':'Drama'
    }
    return render(request,'secondapp/books.html',context=dict3)

def motivation_books_view(request):
    books4 = models.Book.objects.filter(genre='motivation')
    dict4={
        'books':books4,
        'genre':'Motivation'
    }
    return render(request,'secondapp/books.html',context=dict4)

def acads_books_view(request):
    books5 = models.Book.objects.filter(genre='acads')
    dict5={
        'books':books5,
        'genre':'Academic'
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

        namelist=models.User.objects.all()

        if form.is_valid():

            for user in namelist:
                if user.name==form.cleaned_data['name']:
                            form.save(commit=True)
                            #do something after receiving data
                            # print("validation success")
                            return after_request(request,'book')
            return HttpResponse('<h1>Register Yourself First</h1>')



    dict={
        'form':form,
    }
    return render(request,'secondapp/Borrow.html',dict)


def login(request):
    form=forms.FormName()
    dict = {
        'form': form
    }
    if request.method=='POST':
        form = forms.FormName(request.POST)
        if form.is_valid()==True:
            form.accept=False
            dict = {
                'form': form
            }
            name=form.cleaned_data['name']
            password=form.cleaned_data['password']

            return mybooks(request,name,password)


    return render(request, 'secondapp/login.html',dict)

def mybooks(request,name,password):
    namelist = models.User.objects.all()

    for user in namelist:
        if user.name==name:
            print(user.password)
            if user.password==password:
                accepted_list=models.Request.objects.filter(name=name,accept=True)
                accepted_renew_list=models.RenewalRequests.objects.filter(name=name,accept=True)
                if len(accepted_list)!=0 or len(accepted_renew_list):
                    for book in accepted_list:
                        mybook=models.Mybooks.objects.get_or_create(name=book.name,book=book.book,due=book.due)
                    book_list = models.Mybooks.objects.filter(name=name)
                    models.Request.objects.filter(name=name,accept=True).delete()
                    for book in accepted_renew_list:
                        mybook = models.Mybooks.objects.get_or_create(name=book.name, book=book.book, due=book.renewal_time)
                    book_list = models.Mybooks.objects.filter(name=name)
                    models.RenewalRequests.objects.filter(name=name, accept=True).delete()
                if (len(accepted_list)==0 and len(accepted_renew_list)==0):

                    book_list = models.Mybooks.objects.filter(name=name)
                    if(len(book_list)==0):
                        return HttpResponse('NO ISSUED BOOKS ')
                    dict={
                        'mybooks':book_list,
                        'name':name,
                    }
                    return render(request,'secondapp/mybooks.html',dict)
            else:
                return HttpResponse('INVALID PASSWORD')

    return HttpResponse('FIRST REGISTER YOURSELF')

def after_request(request,book):
    dict={
        'book':book,
    }
    return render(request,'secondapp/after_request.html',dict)

def renewal_form(request):
    form=modelforms.RenewForm()
    dict={
        'form':form
    }
    if request.method=='POST':
        form = modelforms.RenewForm(request.POST)

        if form.is_valid()==True:
            form.accept = False
            form.save(commit=True)

            dict = {
                'form': form
            }
            return render(request,'secondapp/after_request.html',dict)
    return render(request,'secondapp/Renewal_form.html',context=dict)

def rating(request,book):
    form=modelforms.RatingForm()
    dict={
        'form':form
    }
    if request.method=='POST':
        form=modelforms.RatingForm(request.POST)

        if form.is_valid()==True:
            form.save(commit=True)
            dict={
                'form':form
            }
            return render(request,'secondapp/index.html',context=dict)
    return render(request,'secondapp/rating.html',context=dict)

def messages(request,name):
    messages=models.Warnings.objects.filter(name=name)
    if len(messages)==0:
        return HttpResponse('No messages from Librarian')
    dict={
        'messages':messages
    }
    return render(request,'secondapp/messages.html',context=dict)

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