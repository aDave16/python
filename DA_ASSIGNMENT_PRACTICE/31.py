#Write a Python program to count the number of strings where the string
#length is 2 or more and the first and last character 
# are same from a given list of strings.
str_list=["hello","3hello123","test","ama"]
count=0
for i in str_list:
    if len(i)>2 and i[len(i)-1]==i[0]:
        count+=1

print(count)