#Write a Python program to find the highest 2 values in a dictionary
d={"a":10,"b":34,"c":23,"d":67}
value=list(d.values())
value.sort(reverse=True)

for i in range(2):
    print(value[i])
