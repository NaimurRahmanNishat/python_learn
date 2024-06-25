class phone:                        # parent class / supper class
    def call(self):
        print("you can call")
    
    def massage(self):
        print("you can massage")

class samsung(phone):               # phone (call massage)    # child class / sub class
    def photo(self):
        print("You can take photo")
        
s = samsung()
s.massage()
s.call()
s.photo()
# Output is:
# you can massage
# you can call
# You can take photo


# Method overridding system in inheritance
class Phone:
    def __init__(self) -> None:
        print("I am in phone class")

class Samsung(Phone):
    def __init__(self):
        print("I am in Sumsung class")

s = Samsung()
# Output is: I am in Sumsung class

class Phone:
    def __init__(self):
        print("I am in phone class")

class Samsung(Phone):
    def __init__(self):
        super().__init__()                # call parent class
        print("I am in Sumsung class")

s = Samsung()
# Output is:
# I am in phone class
# I am in Sumsung class



# Problem practice

class Shape:
    def __init__(self, base, height) -> None:
        self.base = base
        self.height = height
    
    def area(self):
        print("I am a area mathod of Shape class")
        
class Triangle(Shape):
    def area(self):
        area = 0.5 * self.base * self.height
        print("Area of Triangle: ", area)

t = Triangle(20, 30)
t.area()
# Output is: Area of Triangle:  300.0

class Shape:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        print("I am a area mathod of Shape class")
        
class Triangle(Shape):
    def area(self):
        area = 0.5 * self.base * self.height
        print("Area of Triangle: ", area)

class Rectangle(Shape):
    def area(self):
        area = self.base * self.height
        print("Area of Rectangle: ", area)

t = Triangle(20, 30)
t.area()
r = Rectangle(20, 30)
r.area()
# Output is:
# Area of Triangle:  300.0
# Area of Rectangle:  600


# Types of inheritance. There are three types of inheritance. (i) Hierachical Inheritance   (ii)Multi-Level Inheritance   (iii) Multiple Inheritance

# (i) Hierachical Inheritance 
class Shape:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        print("I am a area mathod of Shape class")
        
class Triangle(Shape):
    def area(self):
        area = 0.5 * self.base * self.height
        print("Area of Triangle: ", area)

class Rectangle(Shape):
    def area(self):
        area = self.base * self.height
        print("Area of Rectangle: ", area)

t = Triangle(20, 30)
t.area()
r = Rectangle(20, 30)
r.area()
# Output is:
# Area of Triangle:  300.0
# Area of Rectangle:  600


# (ii)Multi-Level Inheritance  
class A:
    def display1(self):
        print("I am Inside A class")

class B(A):
    # Added display1()
    def display2(self):
        print("I am Inside B class")

class C(B):
    # Added display1() and display2()
    def display3(self):
        print("I am Inside C class")

obj1 = C()
obj1.display1()
obj1.display2()
obj1.display3()
# Output is:
# I am Inside A class
# I am Inside B class
# I am Inside C class

# Another system is:
class A:
    def display1(self):
        print("I am Inside A class")

class B(A):
    # Added display1()
    def display2(self):
        print("I am Inside B class")

class C(B):
    # Added display1() and display2()
    def display3(self):
        super().display1()
        super().display2()
        print("I am Inside C class")

obj1 = C()
obj1.display3()
# Output is: 
# I am Inside A class
# I am Inside B class
# I am Inside C class


# (iii) Multiple Inheritance
class A:
    def display(self):
        print("I am Inside A class")

class B():
    # Added display1()
    def display(self):
        print("I am Inside B class")

class C(A,B):
    # Added display1() and display2()
    def display(self):
        print("I am Inside C class")

obj1 = C()
obj1.display() 
# Output is: I am Inside C class

# Another system is:
class A:
    def display(self):
        print("I am Inside A class")

class B():
    # Added display1()
    def display(self):
        print("I am Inside B class")

class C(A,B):
    # Added display1() and display2()
    pass

obj1 = C()
obj1.display() 
# Output is: I am Inside A class