#create list ask user input and check
list=["sleeping","eating","shopping"]
task=input("enter your task: ")

print(f"{task in list}")
print(f"{task not in list}")