from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import BookEntry
# Create your views here.

def index(request):
    if request.method == "GET":
        return render(request, "book_app/index.html")
    if request.method == "POST":
        book_entry = BookEntry(
            user_name = request.POST["user_name"], 
            book_name = request.POST["book_name"], 
            author_name = request.POST["author_name"], 
            book_status = request.POST["book_status"]
            )
        book_entry.save()
        return render(request, "book_app/index.html")

def recent_reads(request):
    recently_read_books = {"book_list":list(BookEntry.objects.values('user_name','book_name','author_name'))}
    print(recently_read_books)
    return render(request, "book_app/recent_reads.html",recently_read_books)
