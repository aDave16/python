#Write a Python program to update a value in a dictionary.
# Write a Python program to merge two lists into one dictionary using a loop
d={1: 'one', 2: 'one', 3: 'one'}
d.update({2:"two"})
print(d)

l1=[1,2,3]
l2=["one","two","three"]
d1={}
for i in range(len(l1)):
    d1[l1[i]]=l2[i]
print(d1)




