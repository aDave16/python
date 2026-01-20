#Write a Python program to count occurrences of a substring in a string.
str="pythonpython"
substr="py"
count=str.count(substr)
'''
for i in str:
    if substr in i:
        count+=1
else:
    print("Substring not found")'''
print(count)