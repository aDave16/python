#Print half of String in Uppercase
str="hello world"
half= len(str)//2#use floor division 
print(str[:half].upper() + str[half:])