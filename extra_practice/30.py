#Check whether given number is prime or not
no=int(input("enter number: "))
count=1
for i in range(2,no):
    if no%i==0:
        count=1
        print("not prime")
        break
    else:
        count=0
        break
if count==0:
    print(" prime")
