#Write a Python program to open a file in write mode, write some text, and then #close it.
file=open("ass.txt","w")
data="hello good morning"
file.write(data)
print("data written succesfully")
file.close()