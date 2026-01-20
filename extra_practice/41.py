#Write a program to count number of vowel and consonant in given string : E.g "Hello" Vowels - 2 and consonants - 3
str="hello world"
v=0
c=0
for i in str:
    if i in 'aeiou':
         v+=1
    else:
        c+=1
print(f"consonant are: {c}")
print(f"vowels are: {v}")