#Write a program to remove duplicate characters from String E.g String "Hello" output : "Heo"
str="hello"
ch=""
#print(tuple(set(str)))
for i in str:
    if i not in ch:
        ch+=i
print(ch)
    
            