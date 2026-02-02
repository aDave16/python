'''25. ""Library Management:"" Dictionary with book titles as keys and availability (`True/False`) as values. Functions to:
* Borrow a book
* Return a book
* Show available books'''
library = {"Python": True,"Java": True,"C++": True,"Data Science": True}
def borrow_book(book):
    if book in library:
        if library[book]:
            library[book]=False
            print("you have borrowed ",book)
        else:
            print("book is already borrowed")
    else:
        print("book not found")

def return_book(book):
    if book in library:
        if library[book]:
            library[book]=True
            print("you have returned ",book)
        else:
            print("book is not borrowed")
    else:
        print("book not found")

def show_available_books():
    for i,j in library.items():
        print(i , j)

while True:
    print("\n1. Borrow Book")
    print("2. Return Book")
    print("3. Show Available Books")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            for i in library.keys():
                print(i)
            book = input("Enter book name to borrow: ")
            borrow_book(book)
        case 2:
            book = input("Enter book name to return: ")
            return_book(book)
        case 3:
            show_available_books()
        case 4:
            break
        case _:
            print("Invalid choice")
