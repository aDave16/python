'''1
1 2
1 2 3
1 2 3 4
num =int(input("enter number: "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end=" ")#or star
    print()'''

'''1 2 3 4
1 2 3
1 2
1'''
num =int(input("enter number: "))
for i in range(num,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")#or star
    print()
'''
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
num =int(input("enter number: "))
for i in range(num,0,-1):
    for j in range(1,i+1):
        print(i,end=" ")#or star
    print()'''

'''1
2 2 
3 3 3
4 4 4 4
num =int(input("enter number: "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(i,end=" ")#or star
    print()'''

'''1 
3 3
5 5 5
7 7 7 7
9 9 9 9 9'''
num =int(input("enter number: "))
k=1
for i in range(num):
    for j in range(i+1):
        print(k,end=" ")#or star
        #k+=2
    k+=2
    print()
