class Library:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.books = []
    
    def addBooks(self, books):
        for book in books:
            if type(book) is Book:
                self.books.append(book)
            else:
                raise Exception("Not a book")

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.library = None

    def __repr__(self):
        return f"{self.title} by {self.author}"
    
if __name__ == "__main__":
    dpl = Library("Denver Public Library", "Denver")
    lotr = Book("Lord of The Rings", "JRR Tolkein", "Fantasy")
    lotr.library = dpl
    hp = Book("Harry Potter", "Rowling","Fantasy")
    dictionary = Book("Websters Dictionary", "Webster", "Non Fiction")
    dpl.addBooks([lotr, hp, dictionary])
    print(dpl.books)
    print(lotr.library)
        