#Count no of string which contains perticular letter or not with List and List Comprehension
str=["grapes","mango","banana","kiwi"]
letter='a'
count=0
for i in str:
    if letter in i:#compare and count fromn single string 
        count+=1
print(count)