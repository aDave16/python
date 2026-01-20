#Count no of strings which starts with letter 'M' from list [Use List comprehension]
str1=["hello"," world","motion"]
ans=len([i for i in str1 if i.startswith('m')])
print(ans)