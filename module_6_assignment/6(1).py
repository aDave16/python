#Write a generator function that generates the first 10 even numbers.
def gen():
    for i in range(1,11):
        yield i
g=gen()
for j in g:
    print(j)