class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def write_book(self, title):
        book = Book(title, self)
        self.books.append(book)


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


# Create some Author objects and have them write some books
a1 = Author("Alice")
a1.write_book("The Adventures of Alice")
a1.write_book("Through the Looking-Glass")

a2 = Author("Bob")
a2.write_book("The Bob Chronicles")

# Print the books written by each author
print(a1.name, "has written the following books:")
for book in a1.books:
    print(book.title)

print(a2.name, "has written the following books:")
for book in a2.books:
    print(book.title)

# Print the author of each book
print("The author of", a1.books[0].title, "is", a1.books[0].author.name)
print("The author of", a2.books[0].title, "is", a2.books[0].author.name)