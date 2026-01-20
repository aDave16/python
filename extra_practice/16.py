#Print even numbers fall between 2 given numbers E.g user enter 10 20  output 12,14,16,18
end=int(input("enter end digit "))
for i in range(2,end+1):
    if i%2==0:
        print(i)