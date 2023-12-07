from django.urls import path
from . import  views 

urlpatterns = [
    path('API/books', views.getAllBooks),
    path('API/addbook', views.addBook),
    path('API/updatebook', views.updateBook)
]