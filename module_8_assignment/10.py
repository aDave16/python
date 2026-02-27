#Write a Python program to search for a word in a string using re.search().
#Write a Python program to match a word in a string using re.match()
import re
msg="ahmedabad is mega city ahmedabad"
#Checks for a match only at the beginning of the string.(1st word)
s=re.search("ahmedabad",msg)
print(s)

#Searches the entire string Returns match if found anywhere
s1=re.match("ahmedabad",msg)
print(s1)