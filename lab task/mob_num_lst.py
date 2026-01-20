#check list contains valid mobile numbers or not 
lst = ['test1234',1234567890,9090909090,4567890,9876543211,45654,'3345testwe']
for i in lst:
    if i.isdigit() and len(i)==10:
        print(i)