lst=[2,4,5]
ans=[]
def far_to_cel(lst):
    return (lst - 32) * 5 / 9
ans=list(map(far_to_cel,lst))
print(ans)