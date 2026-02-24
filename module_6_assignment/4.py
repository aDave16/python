'''# Program to find the greater and smaller number
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print(f"{num1} is greater than{num2}")
else:
    print(num2, "is greater than", num1)

# Program to calculate grades
marks = int(input("Enter your percentage: "))
if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print("Your grade is:", grade)'''

# Program to check blood donation eligibility
age = int(input("Enter your age: "))
weight = int(input("Enter your weight: "))

if age >= 18:
    if weight >= 50:
        print("You are eligible to donate blood")
    else:
        print("You are not eligible to donate blood due to low weight")
else:
    print("You are not eligible to donate blood due to age")


