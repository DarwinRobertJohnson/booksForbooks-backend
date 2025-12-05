
from .models import BookEntry

def save_book_entry(request):
    book_entry = BookEntry(
        user_name = request.user.username, 
        book_name = request.POST["book_name"], 
        author_name = request.POST["author_name"], 
        book_status = request.POST["book_status"]
        )
    book_entry.save()

def get_user_read_books(request):
    return BookEntry.objects.filter(user_name= request.user.username)

def delete_book_entry(request, id):
    if BookEntry.objects.get(pk=id) is not None:
        BookEntry.objects.get(pk=id).delete()

def get_other_users_books(user_name):
    return BookEntry.objects.filter(user_name= user_name)

def get_currently_reading_book(user_name):
    return BookEntry.objects.filter(user_name=user_name,book_status= True)