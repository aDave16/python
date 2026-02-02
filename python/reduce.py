from functools import reduce
def add(n1,n2):
    return n1+n2
lst=[52,4,2,34,]
ans=reduce(add,lst)
print(ans)