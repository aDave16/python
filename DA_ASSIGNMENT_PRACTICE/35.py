#Write a Python program to generate and print a list of first and last 5
#elements where the values are square of numbers between 1 and 30
lst=[i**2 for i in range(1,31)]
print(f"first 5 elements: {lst[:5]} \n last five: {lst[-5:]}")