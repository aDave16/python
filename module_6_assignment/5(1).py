lst=['mango','apple','banana']
search='mango'
flag=False
for i in lst:
    print(i)
    print(f"length of each string: {len(i)}")

for j in lst:
    flag=True
    break
if j==search:
    print(f"find {search}")
else:
    print(f"not find {search}")

for k in range(5):
    for l in range(k+1):
        print(" * ",end="")
    print()