try:
    file=open("ass.txt",'r')
    print(file.read())
except FileNotFoundError:
    print("file not available")
except Exception as e:
    print(e)
finally:
    file.close()
    print("finally will always executes")
