from functools import reduce

lst=[1,2,3,4]
ans_even=list(filter(lambda num:num%2==0,lst))#select only even numbers
ans_sq=list(map(lambda num:num**2,ans_even))#sqyare of each filterd number
ans_sum=reduce(lambda n1,n2:n1+n2,ans_sq)
print(ans_sum)