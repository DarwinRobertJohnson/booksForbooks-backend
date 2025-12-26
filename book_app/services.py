
from .models import BookEntry

def save_book_entry(entry):
    book_entry = BookEntry(
        user_name = entry["user_name"], 
        book_name = entry["book_name"], 
        author_name = entry["author_name"], 
        book_status = entry["book_status"],
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

def toggle_book_status(id):
    book_entry = BookEntry.objects.get(pk=id)
    state=False
    if book_entry.book_status:
        state = False
    else:
        state = True
    book_entry.book_status = state
    book_entry.save()
