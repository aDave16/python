total = 0
while True:
    print("\n---- MENU ----")
    print("1. Pizza     - Rs. 120")
    print("2. Burger    - Rs. 60")
    print("3. Sandwich  - Rs. 70")
    print("4. Pasta     - Rs. 150")

    choice = int(input("Enter your choice: "))
    price = 0

    match choice:
        case 1:
            print("You have selected: Pizza")
            q = int(input("Enter quantity: "))
            price = 120 * q

        case 2:
            print("You have selected: Burger")
            q = int(input("Enter quantity: "))
            price = 60 * q

        case 3:
            print("You have selected: Sandwich")
            q = int(input("Enter quantity: "))
            price = 70 * q

        case 4:
            print("You have selected: Pasta")
            q = int(input("Enter quantity: "))
            price = 150 * q

        case _:
            print("Not in menu")

    if price > 0:
        print(f"Total amount: Rs. {price}")
        total += price

    sel = input("Do you want to order more? (Y/N): ")

    if sel != 'y':
        break

print(f"\nYour total bill is: Rs. {total}")
