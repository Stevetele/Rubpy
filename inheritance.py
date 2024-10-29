# parent class
class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author

    def __int__(self):
        return f"The Title {self.title}, Author {self.author}"
    def display(self):
        return f"Title {self.title} Author {self.author}"
# child class
class LibraryBook(Book):
    def __init__(self,title,author,isbn,copies_available):
        super().__init__(title,author)
        self.isbn=isbn
        self.copies_available=copies_available
    def borrow_book(self):
        if self.copies_available >0:
            self.copies_available -=1
            return f"{self.title} borrowed. Copies left: {self.copies_available}"
        else:
            return f"Number of copies of {self.title} unavailable"
    def return_book(self):
        self.copies_available +=1
        return f"{self.title} returned, Copies left: {self.copies_available}"

# usage    example
book1=LibraryBook("Pyschology of Money","Morgan Housel",8990_8990,20)
book1.display()
print(book1.borrow_book())
print(book1.return_book())
print(f"{book1.display()} is there")





