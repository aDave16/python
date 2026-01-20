#Write a program to count the number of words that start with a vowel in a given sentence 
str='An apple a day keeps the doctor away'
count=0
vowel='aeiou'

for i in str.split():
    if i[0] in vowel:
        count+=1
        print(tuple(i))
print(count)
