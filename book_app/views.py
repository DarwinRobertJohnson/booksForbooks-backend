from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import BookEntry
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='sign in')
def index(request):
    if request.method == "GET":
        return render(request, "book_app/index.html")
    if request.method == "POST":
        book_entry = BookEntry(
            user_name = request.user, 
            book_name = request.POST["book_name"], 
            author_name = request.POST["author_name"], 
            book_status = request.POST["book_status"]
            )
        book_entry.save()
        return render(request, "book_app/index.html")

def sign_in_post(request):
    user = authenticate(username=request.POST["user_name"], password=request.POST["password"])
    if user is not None:
        login(request, user)
        return redirect("index")
    else:
        return render(request, "book_app/sign_in.html")

def sign_in(request):
    if request.method=="POST":
        return sign_in_post(request)
    elif request.method=="GET":
        return render(request, "book_app/sign_in.html")

def sign_out(request):
    logout(request)
    return redirect("sign in")


def recent_reads(request):
    if request.method =="GET":
        recently_read_books = {"book_list":list(BookEntry.objects.values('user_name','book_name','author_name'))}
        return render(request, "book_app/recent_reads.html",recently_read_books)
        
def user_others(request, user_name):
    user_read_books = BookEntry.objects.filter(user_name= user_name)
    currently_reading = BookEntry.objects.filter(book_status= True)
    context={'user_name':user_name, 'book_list':user_read_books,'current_read':currently_reading}
    return render(request, "book_app/user_others.html",context)
