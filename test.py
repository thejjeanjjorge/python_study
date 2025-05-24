class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # title property
    @property
    def title(self):
        return self._title
        # TODO: return title


    @title.setter
    def title(self, value):
        # TODO: check if value is not empty
        if value:
            self._title = value
        else:
            raise ValueError("Title cannot be empty")

    # author property
    @property
    def author(self):
        return self._author
        # TODO: return author


    @author.setter
    def author(self, value):
        # TODO: check if value is not empty
        if value:
            self._author = value
        else:
            raise ValueError("Author cannot be empty")

    # pages property
    @property
    def pages(self):
        # TODO: return pages
        return self._pages
        

    @pages.setter
    def pages(self, value):
        # TODO: check if value is a positive integer
        if value > 0: 
            self._pages = value
        else:
            raise ValueError("Pages need to be a positive integer")
        

    def summary(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"
        # TODO: return formatted string
        

title = input("Enter the title of the book ").strip()
author = input("Enter the name of the author ").strip()


while True:
    try:
        pages = int(input("Enter the number of pages "))
        break
    except ValueError:
        print("Pleas enter a valid number")



pages = int(pages)

book = Book(title, author, pages)
print(book.summary())