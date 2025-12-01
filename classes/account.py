
class account:

    def __init__(self, user_name,email_id,book_items=None):
        self.user_name = user_name
        self.email_id = email_id
        self.book_items = book_items

    def add_book(self, new_book):
        self.book_items.append(new_book)
    
    def remove_book(self, target_book):
        self.book_items.pop(target_book)