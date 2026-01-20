#Write a program to find all perfect numbers from given range (Perfect number is positive integer that is equal to the sum of its proper divisors, excluding the number itself.) e.g 6 (divisor is 1,2,3, and sum is 6) 28 (divisors are 1,2,4,7,14 and sum of all divisors are 28)
for i in range(1,100):
    sum=0
    for j in range(1,i):
        if i%j==0:
            sum=sum+j
    if sum==i:
        print(i)