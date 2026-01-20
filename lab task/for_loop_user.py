#ask range from user using for loop
start = int(input("enter start index: "))
end = int(input("enter end index: "))
step = int (input("enter increment or decrement value"))
if start<end:
    for a in range(start,end,step):
        print(a)
else:
    print("start index must be greater")
