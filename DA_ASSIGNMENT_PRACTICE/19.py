#Write a Python program to count the occurrences of each word 
str="hello python hello java"
word={}
for i in str.split():
    if i in word:
        word[i]+=1
    else:
        word[i]=1
for j,k in word.items():
    print(j,k)
