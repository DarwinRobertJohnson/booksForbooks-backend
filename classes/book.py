
class book:

    def __init__(self, book_name, author_name, book_status):
        self.book_name = book_name
        self.author_name = author_name
        self.book_status = book_status

    def change_book_name(self, updated_book_name):
        self.book_name = new_book_name
    
    def change_author_name(self, updated_author_name):
        self.author_name = updated_author_name

    def update_status(self, updated_status):
        self.book_status = update_status