#fibbonacci series
a=0
b=1
no=int(input("enter number: "))
next=a+b
print("0 ")
for i in range(0,no):
    a=b
    b=next
    next=a+b
    print(next) 
