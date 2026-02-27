file=open("ass1.txt",'w')
print(f"intial postion {file.tell()}")
file.write("hello world")
print(file.tell())#returns current position