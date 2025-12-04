from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import BookEntry
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
@login_required(login_url='sign in')
def user_home(request):
    if request.method == "GET":
        user_read_books = BookEntry.objects.filter(user_name= request.user.username)
        return render(request, "book_app/index.html", {'self_data':user_read_books})
    if request.method == "POST":
        book_entry = BookEntry(
            user_name = request.user, 
            book_name = request.POST["book_name"], 
            author_name = request.POST["author_name"], 
            book_status = request.POST["book_status"]
            )
        book_entry.save()
        return redirect("index")

def sign_in_post(request):
    user = authenticate(username=request.POST["user_name"], password=request.POST["password"])
    if user is not None:
        login(request, user)
        print("correct authentication")
        return redirect("user-dash-board")
    else:
        return redirect("sign in")

def sign_in(request):
    if request.method=="POST":
        return sign_in_post(request)
    elif request.method=="GET":
        return render(request, "book_app/sign_in.html")

def sign_out(request):
    logout(request)
    return redirect("sign in")

def sign_up(request):
    if request.method == "GET":
        form = UserCreationForm()
        return render(request, "book_app/sign_up.html", {'form':form})
    elif request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("sign in")
    return render(request, "book_app/sign_up.html",{"form":form})

@login_required(login_url='sign in')
def delete(request, id):
    if BookEntry.objects.get(pk=id) is not None:
        BookEntry.objects.get(pk=id).delete()
    return redirect("index")

def recent_reads(request):
    if request.method =="GET":
        recently_read_books = {"book_list":list(BookEntry.objects.values('user_name','book_name','author_name'))}
        return render(request, "book_app/recent_reads.html",recently_read_books)
        
def user_others(request, user_name):
    user_read_books = BookEntry.objects.filter(user_name= user_name)
    currently_reading = BookEntry.objects.filter(book_status= True)
    context={'user_name':user_name, 'book_list':user_read_books,'current_read':currently_reading[0]}
    return render(request, "book_app/user_others.html",context)
