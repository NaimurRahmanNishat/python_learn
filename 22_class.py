class student:
    roll = ""
    cgpa = ""
    
rahim = student()
print(isinstance(rahim,student))
# Output is: True                 # Checking this is class true. 

class student:
    roll = ""
    cgpa = ""
    
rahim = student()
rahim.roll = 101
rahim.cgpa = 3.7
print(f"Roll : {rahim.roll} CGPA: {rahim.cgpa}")

karim = student()
karim.roll = 102
karim.cgpa = 3.75
print(f"Roll : {karim.roll} CGPA: {karim.cgpa}")
# Output is: 
# Roll : 101 CGPA: 3.7
# Roll : 102 CGPA: 3.75

# function mathod class
class student:
    roll = ""
    cgpa = ""
    def display(self):
        print(f"Roll : {self.roll} CGPA: {self.cgpa}")

rahim = student()
rahim.roll = 101
rahim.cgpa = 3.7
rahim.display()

karim = student()
karim.roll = 102
karim.cgpa = 3.75
karim.display()
# Output is:
# Roll : 101 CGPA: 3.7
# Roll : 102 CGPA: 3.75


class student:
    roll = ""
    cgpa = ""
    def set_value(self, roll, cgpa):
        self.roll = roll
        self.cgpa = cgpa
    def display(self):
        print(f"Roll : {self.roll} CGPA: {self.cgpa}")

rahim = student()
rahim.set_value(101, 3.7)
rahim.display()

karim = student()
karim.set_value(102, 3.75)
karim.display()
# Output is: 
# Roll : 101 CGPA: 3.7
# Roll : 102 CGPA: 3.75

class student:
    def set_value(self, roll, cgpa):
        self.roll = roll
        self.cgpa = cgpa
    def display(self):
        print(f"Roll : {self.roll} CGPA: {self.cgpa}")

rahim = student()
rahim.set_value(101, 3.7)
rahim.display()

karim = student()
karim.set_value(102, 3.75)
karim.display()
# Output is: 
# Roll : 101 CGPA: 3.7
# Roll : 102 CGPA: 3.75

