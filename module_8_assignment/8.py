#Write Python programs to demonstrate method overloading and method overriding.
class Calculator:
    def add(self, a=10, b=20):
        return a+b
    def add(self, a=10, b=20,c=50):
        return a+b+c
obj = Calculator()
print("Addition of 2 numbers:", obj.add())
print("Addition of 3 numbers:", obj.add())

#method overrriding
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):#Overriding parent method
        print("Dog barks")


a = Animal()
d = Dog()
a.sound()
d.sound()