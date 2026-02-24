name=input("enter name: ")
print(f"{name.capitalize()} - {name.upper()} - {name.lower()} - {name.title()}")
print(f"{len(name)}")
print(f"{name.count("a")}")#count occurence of char
print(f"{name.split()}")#split by char in list

lst=name.split()
print(f"{len(lst)}")#return no of words

city=['ahm','baroda','surat']
all="-".join(city)
print(all)
