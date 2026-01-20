#enter month name from user and dis days accordingly using match case with in opoerator
month = input("Enter month name: ")

match month:
    case m if m in ["january", "march", "may", "july", "august", "october", "december"]:
        print("31 days")

    case m if m in ["april", "june", "september", "november"]:
        print("30 days")

    case "february":
        print("28 or 29 days")

    case _:
        print("Invalid month name")
