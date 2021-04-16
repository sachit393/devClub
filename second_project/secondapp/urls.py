from django.urls import path

from . import views

app_name='secondapp'
urlpatterns=[
    path('', views.index, name='index'),

    path('books/action/', views.action_books_view,name='actionbooks'),
    path('books/fiction/', views.fiction_books_view,name='fictionbooks'),
    path('books/drama/', views.drama_books_view,name='dramabooks'),
    path('books/motivation/', views.motivation_books_view,name='motivationbooks'),
    path('books/acads/', views.acads_books_view,name='acadsbooks'),
    path('registration/',views.registrationform,name='registrationform'),
    path('book/<str:booktitle>',views.book,name='book'),
    path('book/request/',views.request_book,name='Borrow'),
    path('login/',views.login,name='login'),
    path('mybooks<str:name>',views.mybooks,name='mybooks')
]