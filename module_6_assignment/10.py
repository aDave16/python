#Write a Python program to apply the map() function to square a list of numbers.
lst=[1,2,3,4,5]
sq=[]
sq=map(lambda x:x**2,lst)
print(list(sq))
