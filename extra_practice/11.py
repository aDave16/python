#Print no of digits and letters in String.Accept String from user. E.g string="H1Visa" Digits = 1 and letters=5
str=input("enter alphanumeric string: ")
a=0
n=0
for i in str:
    if i.isdigit():
        n+=1
    else:
        a+=1
print(f"digits are: {n}")
print(f"Alphabts are: {a}")