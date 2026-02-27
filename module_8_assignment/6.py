class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

# Create object
s1 = Student("Ami", 20, "BCA")

# Access properties using object
print("Accessing properties directly:")
print(s1.name)
print(s1.age)
print(s1.course)

print("\nUsing method:")
s1.display()
