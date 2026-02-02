#if number is evem then only find their square
lst=[1,2,32,45,656]
def checkEven(num):
    if num%2==0:
        return num

def sq(num):
    return num*num

ans_even=list(filter(checkEven,lst))#it only returns true data
ans=list(map(sq,ans_even))
print(ans)

