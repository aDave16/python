class ageexception(Exception):
    pass
try:
    age=int(input("enter ur age: "))
    if age<18:
        raise ageexception
    print("you are eligible")
except ageexception:
    print("age should be above 18")