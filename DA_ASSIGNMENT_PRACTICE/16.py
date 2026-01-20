#Write a Python program to count the number of characters(character frequency) in a string
str="hello python"
freq={}
for i in str:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

for j,k in freq.items():
    print(j,k)