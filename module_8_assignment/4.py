#Write a Python program to read the contents of a file and print them on the console.
file=open("D:\\python\\extra_practice\\12.py")
print(file.read())
file.close()

#Write a Python program to write multiple strings into a file.
file1=open("write.txt","w")
while True:
    data=input("enter string ")
    if not data:
        break
    file1.write(data + '\n')
file1.close()

    