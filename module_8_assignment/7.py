#single inheritance
class Parent:
    def show_parent(self):
        print("This is Parent class")

class Child(Parent):
    def show_child(self):
        print("This is Child class")

obj = Child()
obj.show_parent()
obj.show_child()

#multilevel
class Grandparent:
    def show_grandparent(self):
        print("This is Grandparent class")

class Parent(Grandparent):
    def show_parent(self):
        print("This is Parent class")

class Child(Parent):
    def show_child(self):
        print("This is Child class")

obj = Child()
obj.show_grandparent()
obj.show_parent()
obj.show_child()

#multiple
class Father:
    def show_father(self):
        print("This is Father class")

class Mother:
    def show_mother(self):
        print("This is Mother class")

class Child(Father, Mother):
    def show_child(self):
        print("This is Child class")

obj = Child()
obj.show_father()
obj.show_mother()
obj.show_child()

#hierarchical
class Parent:
    def show_parent(self):
        print("This is Parent class")

class Child1(Parent):
    def show_child1(self):
        print("This is Child1 class")

class Child2(Parent):
    def show_child2(self):
        print("This is Child2 class")

obj1 = Child1()
obj2 = Child2()

obj1.show_parent()
obj1.show_child1()

obj2.show_parent()
obj2.show_child2()

#hybrid
class A:
    def show_A(self):
        print("Class A")

class B(A):
    def show_B(self):
        print("Class B")

class C(A):
    def show_C(self):
        print("Class C")

class D(B, C):
    def show_D(self):
        print("Class D")

obj = D()
obj.show_A()
obj.show_B()
obj.show_C()
obj.show_D()
