class Library:
    def __init__(self):
        self.noofBooks=0
        self.books=[]
    def addBook(self,book):
        self.books.append(book)
        self.noofBooks=len(self.books)

    def display_books(self):
        print(f'Total {self.noofBooks} books in the library')


a=Library()
a.addBook('HarryPotter')
a.addBook('Rich dad, poor dad')
a.display_books()



