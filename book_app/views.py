from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse,JsonResponse
from .models import BookEntry
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from . import services
from rest_framework import generics
from .serializers import BookEntrySerializer
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User
# Create your views here.

def user_home(request):
    if request.method == "GET":
        user_read_books = services.get_user_read_books(request)
        return render(request, "book_app/index.html", {'self_data':user_read_books})
    if request.method == "POST":
        services.save_book_entry(request)
        return redirect("index")

def sign_in_post(request):
    user = authenticate(username=request.POST["user_name"], password=request.POST["password"])
    if user is not None:
        login(request, user)
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

# @login_required(login_url='sign in')
def delete(request, id):
    services.delete_book_entry(request, id)
    return redirect("index")

def recent_reads(request):
    if request.method =="GET":
        recently_read_books = {"book_list":list(BookEntry.objects.values('user_name','book_name','author_name'))}
        return render(request, "book_app/recent_reads.html",recently_read_books)
        
def user_others(request, user_name):
    user_read_books = services.get_other_users_books(user_name)
    currently_reading = services.get_currently_reading_book(user_name)
    print(currently_reading)
    if currently_reading.exists():
        context={'user_name':user_name, 'book_list':user_read_books,'current_read':currently_reading[0].book_name}
    else:
        context={'user_name':user_name, 'book_list':user_read_books,'current_read':"-"}
    return render(request, "book_app/user_others.html",context)


# API Code
class recently_read_books(generics.ListAPIView):
    queryset = BookEntry.objects.values('user_name','book_name','author_name')
    serializer_class = BookEntrySerializer
    http_method_names = ['get']

def user_others_api(request, user_name):
    user_read_books = list(services.get_other_users_books(user_name).values())
    currently_reading = list(services.get_currently_reading_book(user_name).values())
    return JsonResponse(
    {"user_read_books":user_read_books, 
    "currently_reading":currently_reading
    })

@csrf_exempt
def api_login(request):
    data = json.loads(request.body)
    print(data)
    user = authenticate(username=data['username'], password=data['password'])
    if user:
        login(request, user)  # creates session cookie
        return JsonResponse({'success': True})
    print("Sign in Success")
    return JsonResponse({'success': False}, status=400)

def user_dashboard_api(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated is True:
        user_name = request.user.username
        user_read_books = list(services.get_other_users_books(user_name).values())
        currently_reading = list(services.get_currently_reading_book(user_name).values())
        return JsonResponse(
        {"user_read_books":user_read_books, 
        "currently_reading":currently_reading
        })
    else:
        return JsonResponse({"status":"not Authenticated"})

def user_action_delete(request, id):
    if request.user.is_authenticated:
        services.delete_book_entry(request, id)
        return JsonResponse({"status":"Delete Success"})
    return JsonResponse({"status":"delete failed"})

@csrf_exempt
def user_action_add(request):
    if request.user.is_authenticated:
        data= json.loads(request.body)
        services.save_book_entry({
            "user_name": request.user.username,
            "book_name":data["book_name"],
            "author_name": data["author_name"],
            "book_status":data["book_status"],
            })
        return JsonResponse({
            "status":True
        })
    else:
        return JsonResponse({
            "status":False
        })

@csrf_exempt
def api_signup(request):
    data = json.loads(request.body)
    if User.objects.filter(username=data["username"]).exists():
        return JsonResponse({
            "success":False,
        })
    user = User.objects.create_user(username=data["username"], password=data["password"])
    user.save()
    return JsonResponse({
        "success":True
    })

@csrf_exempt
def api_logout(request):
    logout(request)
    return JsonResponse({
        "success":True
    })

@csrf_exempt
def user_action_toggle(request):
    data = json.loads(request.body)
    services.toggle_book_status(data["id"])
    return JsonResponse({
        "success":True
    })