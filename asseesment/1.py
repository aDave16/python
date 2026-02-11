rentals=[]
books = [
    "Python Basics",
    "Data Science",
    "Machine Learning",
    "Web Development",
    "AI Fundamentals"
]

def booking():
    print("\nAvailable Books:")
    for b in books:
        print(b)

    book_name=input("enter book name: ")
    if book_name not in books:
         print("book is not available in library")
         return

    name=input("enter your name: ")
    rent_on=int(input("enter rent on date: "))
    returned_date=int(input("enter return date: "))

        #dict for key value
    rental={
            "name":name,
            "book_name":book_name,
            "rent_on":rent_on,
            "returned_date":returned_date,
            "is_return":False
        }
    rentals.append(rental)#add dict details to list
    books.remove(book_name)# remove book from available list
    print("book issued successfully")

def return_book():
      book_name=input("enter book name to return: ")
      for i in rentals:
        if i["book_name"]==book_name and not i["is_return"]:
            actual_return_date=int(input("enter your return date: "))
            late_day=actual_return_date - i["returned_date"]
            #calculates late fees as per day
            if late_day > 0:
             late_fee = late_day * 10 #fixed panelty
            else:
                late_fee = 0

            i["is_return"]=True
            books.append(book_name)# add back to library

            print("\n your receipt")
            print("Customer:", i["name"])
            print("Book:", i["book_name"])
            print("Late Days:", late_day)
            print("Late Fee:", late_fee)
print("Book not found or already returned")

def rental_summary():
    if not rentals:
        print("No rentals found")
        return

    print("\nRental Summary")
    for i in rentals:
        if i["is_return"]:
            status = "Returned"
        else:
            status = "Not Returned"

        print("Customer:", i["name"])
        print("Book:", i["book_name"])
        print("Status:", status)
        print()

while True:
    print("RentTrack Menu")
    print("1. Rent a Book")
    print("2. Return a Book")
    print("3. Rental Summary")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        booking()
    elif choice == "2":
        return_book()
    elif choice == "3":
        rental_summary()
    elif choice == "4":
        break
    else:
        print("\nInvalid choice. Try again.\n")