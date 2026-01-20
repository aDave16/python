#Print no. of days in given list of Months e.g ['April','February','May'] output April - 30 Days February - 28 or 29 days,May 31 Days
month=['april','feb','may']
m=input("enter month nme to see days ")
match m:
    case 'april':
        print("30 days")
    case 'feb':
        print("28 or 29 days")
    case 'may':
        print("31 days")
    case _:
        print("invalid month")