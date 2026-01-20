#Write a Python program to unzip a list of tuples into individual lists.
lst=[(1,2,3),(4,5,6),(7,8)]
lst1,lst2,lst3=zip(lst)
print(list(lst1))
print(list(lst2))
print(list(lst3))