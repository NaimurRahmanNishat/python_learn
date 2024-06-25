class student:
    def __init__(self, roll, cgpa):      # __init__ This is constructor.
        self.roll = roll
        self.cgpa = cgpa

    def display(self):
        print(f"Roll : {self.roll} CGPA: {self.cgpa}")

rahim = student(101, 3.7)
rahim.display()

karim = student(102, 3.5)
karim.display()
# Output is:
# Roll : 101 CGPA: 3.7
# Roll : 102 CGPA: 3.5



# Practice problem : define class is Triangle. Calculate the constructor base,height calculate area. when t1(10, 20) and t2(20, 30)
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def calculate_area(self):
        area = 0.5 * self.base * self.height
        print("Area: ", area)

t1 = Triangle(10, 20)
t1.calculate_area()

t2 = Triangle(20, 30)
t2.calculate_area()
# Output is: 
# Area:  100.0
# Area:  300.0


