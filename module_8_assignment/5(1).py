#Write a Python program to handle exceptions in a simple calculator (division by zero, invalid input).
try:
    print("1.Addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    
    n1=int(input("enter number1: "))
    n2=int(input("enter number2: "))
    ch=int(input("enter ur choice: "))

    match ch:
        case 1:
            print(n1+n2)
        case 2:
            print(n1-n2)
        case 3:
            print(n1*n2)
        case 4:
            print(n1/n2)
        case _:
            pass

except ZeroDivisionError:
    print("number cannot be divided by 0")
except ValueError:
    print("invalid choice")
except Exception as e:
    print(e)
    