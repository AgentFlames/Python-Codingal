class book: 
    def __init__(self, title, author, is_borrowed = False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def borrow(self): 
        self.is_borrowed = True

    def return_book(self): 
        self.is_borrowed = False
        print(f"{self.title} successfuly returned")

def book_availablity(book1,book2,book3):
    my_list = [book1,book2,book3]
    for i in my_list : 
        if i.is_borrowed == False: 
            print(f"{i.title} is Available for borrow")

        else: 
            print(f"{i.title} is unavailable for borrow")

    return 0

book1 = book("Thinking Fast and Slow", "Daniel Kaheman")
book2 = book("Atomic Habits", "James Clear",)
book3 = book("Laws of Human Nature", "Robert Greene",)

print()

book1.borrow()
book2.borrow()
book3.borrow()

book_availablity(book1,book2,book3)

print()

book1.return_book()
book2.return_book()
book3.return_book()

print()