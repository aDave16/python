#Write a program to check if a string is an anagram of another string Eg string 1 = listen string 2 = silent output yes 
str1=input("enter 1st string ")
str2=input("enter 2nd string ")
if sorted(str1) == sorted(str2):
    print("yes")
else:
    print("no")