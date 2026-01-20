#Write a Python program to check multiple keys exists in a dictionary
dic={"name":"ami","age":21}
key=["name","age"]
if all(i in dic for i in key):
    print("all keys are there")
else:
     print("all keys are not there")
