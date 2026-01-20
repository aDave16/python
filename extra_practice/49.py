#Find a longest word in given string E.g "it is another string" output "another"
str="it is another string" 
word=""
for i in str.split():
    if len(i)>len(word):
        word=i
print(word)