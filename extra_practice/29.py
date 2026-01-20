#factorial series
no=int(input("enter number: "))
fact=1
for i in range(2,no+1):
    fact*=i
print(fact)