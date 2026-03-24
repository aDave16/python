# List to store all rental records
rentals = []

#currently available books
books = [
    "Python Basics",
    "Data Science",
    "Machine Learning",
    "Web Development",
    "AI Fundamentals"
]

# Function to rent a book
def booking():
    print("\nAvailable Books:")
    for b in books:
        print(b)

    book_name = input("Enter book name: ")

    # Check if book exists
    if book_name not in books:
        print("Book is not available in library")
        return

    # Take customer details
    name = input("Enter your name: ")
    rent_on = int(input("Enter rent on date: "))
    returned_date = int(input("Enter return date: "))

    # Create dictionary to store rental info
    rental = {
        "name": name,
        "book_name": book_name,
        "rent_on": rent_on,
        "returned_date": returned_date,
        "is_return": False
    }

    # Add rental record to list
    rentals.append(rental)

    # Remove book from available list
    books.remove(book_name)

    print("Book issued successfully")

# Function to return a book
def return_book():
    book_name = input("Enter book name to return: ")

    # Search rental records
    for i in rentals:
        if i["book_name"] == book_name and not i["is_return"]:

            actual_return_date = int(input("Enter your return date: "))

            # Calculate late days
            late_day = actual_return_date - i["returned_date"]

            # Late fee calculation
            if late_day > 0:
                late_fee = late_day * 10   # ₹10 per late day
            else:
                late_fee = 0

            # Mark book as returned
            i["is_return"] = True

            # Add book back to library
            books.append(book_name)

            # Print receipt
            print("\nYour Receipt")
            print("Customer:", i["name"])
            print("Book:", i["book_name"])
            print("Late Days:", late_day)
            print("Late Fee:", late_fee)
            return

    # If book not found
    print("Book not found or already returned")

# Function to display summary
def rental_summary():
    if not rentals:
        print("No rentals found")
        return

    print("\nRental Summary")

    # Show all rental records
    for i in rentals:
        if i["is_return"]:
            status = "Returned"
        else:
            status = "Not Returned"

        print("Customer:", i["name"])
        print("Book:", i["book_name"])
        print("Status:", status)
        print()

# Main Menu Loop
while True:
    print("\nRentTrack Menu")
    print("1. Rent a Book")
    print("2. Return a Book")
    print("3. Rental Summary")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")
    
    match choice:
        case "1":
            booking()
        case "2":
            return_book()
        case "3":
            rental_summary()
        case "4":
            print("Exiting program...")
            break
        case _:
            print("Invalid choice")
