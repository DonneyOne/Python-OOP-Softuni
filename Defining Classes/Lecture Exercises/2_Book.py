class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages
p = Book("james", "Hartiq", 200)
print(p.name)
print(p.author)
print(p.pages)