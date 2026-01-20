#Write a Python program to create a calculator using functions
def add(n1,n2):
    ans=n1+n2
    return ans
def sub(n1,n2):
    ans=n1-n2
    return ans
def mul(n1,n2):
    ans=n1*n2
    return ans
def div(n1,n2):
    ans=n1/n2
    return ans
print(f"1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
ch=int(input("enter your choice: "))
match ch:
    case 1:
        ans=add(10,20)
        print(f"Addition is:{ans}")
    case 2:
        ans=sub(10,20)
        print(f"Subtraction is:{ans}")
    case 3:
        ans=mul(10,20)
        print(f"multiplication is:{ans}")
    case 4:
        ans=div(10,20)
        print(f"Division is:{ans}")
    case _:
        print("invalid choice")