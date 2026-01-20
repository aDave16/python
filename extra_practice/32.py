#armstrong number
#153 = 1³ + 5³ + 3³ = 153
no=int(input("enter no: "))
org=no
sum=0
while(no!=0):
    rev=no%10
    no=no//10
    sum = sum + rev * rev * rev
if sum==org:
    print(f"{org} is armstrong")
else:
    print(f"{org} is not armstrong")