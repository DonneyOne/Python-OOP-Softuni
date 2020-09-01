class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author: str, book_name: str, days_to_return: int, library):
        for key, value in library.books_available.items():
            if book_name in value:
                self.books.append(book_name)
                library.rented_books[self.username] = {book_name: days_to_return}
                value.remove(book_name)
                return f"{book_name} successfully rented for the next {days_to_return} days!"
        for k, v in library.rented_books.items():
            if book_name in v:
                return f"The book {book_name} is already rented and will be available in " \
                       f"{v[book_name]} days!"

    def return_book(self, author, book_name, library):
        for k,v in library.rented_books.items():
            if book_name in self.books and book_name in v:
                self.books.remove(book_name)
                del v[book_name]
            else:
                return f"{self.username} doesn't have this book in his/her records!"
        [v.append(book_name) for k,v in library.books_available.items()]

    def info(self):
        return f"{self.user_id}, {self.username}"
