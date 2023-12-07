from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
from .models import Book
# Create your views here.


@require_http_methods(["GET"])
def getAllBooks(request):
    books = [i for i in  Book.objects.all().values()]
    return JsonResponse({'books ': books})


@require_http_methods(["POST"])
def addBook(request):
    try:
        book_data = json.loads(request.body)
        name = book_data['name']
        book_id = book_data['id']
        author = book_data['author']
        if Book.objects.filter(book_id=book_id).exists():
            return JsonResponse({'scucess' : False, 'message' : "Book already exists"})
        new_book = Book.objects.create(name=name,book_id=book_id,author=author)
        new_book.save()
        return JsonResponse({'success' :True, 'message' : "Book added"})
    except Exception as err:
        JsonResponse({ 'success' : False ,'message' : "Too few details"})
      
  
@require_http_methods(["PATCH"])
def updateBook(request):
    try:
        book_data = json.loads(request.body)
        id = book_data['id']
        name = book_data['name']
        author = book_data['author']
        if id is not None:
            temp_book = Book.objects.get(id=id)
            if name is not None:
                setattr(temp_book,'name',name)
            if author is not None:
                setattr(temp_book,'author', author)
            temp_book.save()
            return JsonResponse({'success' : True, 'message' : "Book data updated" })
        else:
            return JsonResponse({'success' : False, 'error' : "Book id not provided"})
        
    except Book.DoesNotExist:
        JsonResponse({'success' : False, 'error' : "Book doesnot exists"})
    except json.JSONDecodeError:
        return JsonResponse({ 'success' : False ,'error': 'Invalid JSON data'})
    