#Print list of prime numbers from given range
no=int(input("enter range: "))
for j in range(2,no):
    count=0
    for i in range(2,j):
        if j%i==0:
            count=1
            break
        else:
             count=0
if count==0:
        print(j)
