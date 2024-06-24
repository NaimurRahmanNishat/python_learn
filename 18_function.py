# Basic function.
def myFunction():
    print("I am myFunction")
myFunction()
# Output is: I am myFunction

#function with parameters
def myFunction(name):
    print(f"{name}, I am myFunction")
myFunction("Intel")
# Output is: Intel, I am myFunction

# return value function
def add(a, b):
    return a+b
result = add(5,3)
print(result)
# Output is: 8

# default parameters functioin
def myFunction(name="Nishat"):
    print(f"Hello, {name}")
myFunction()
# Output is: Hello, Nishat

# Docstrings function
def myFunction(a,b):
    return a+b
result = myFunction(5, 3)
print(result)
# Output is: 8

# Variable Scope function
global_var = 10
def myFunction():
    local_var = 5
    print(global_var + local_var)
myFunction()
# Output is: 15

# Recursion function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n = int(input("=> "))                       # input is 5, the output should be 120 since 5! = 5 * 4 * 3 * 2 * 1 = 120.
result = factorial(n)
print(f"The factorial of {n} is {result}")
# Output is: The factorial of 5 is 120

# lamda function
double = lambda x : x * 2      # Define the lambda function
result = double (3)            # Use the lambda function to double the number 3
print(result)
# Output is: 6

# Function Decorators
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper
@my_decorator
def say_hello():
    print("Hello!")
say_hello()
# Output is: 
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.

# Advanced function
def apply(func, x):
    return func(x)
def squre(x):
    return x**2
result = apply(squre, 5)
print(result)
# Output is: 25                # input here 5 Output is 25.

# Map function.....
import math
def area (r):
    return math.pi * (r ** 2)
radius = [2,3,3.7,2.9]
areas = []
for r in radius:
    areas.append(area(r))
print(areas)
# Output is: [12.566370614359172, 28.274333882308138, 43.008403427644275, 26.42079421669016]

# using map function
import math
def area (r):
    return math.pi * (r ** 2)
radius = [2,3,3.7,2.9]
result = list(map(area,radius))
print(result)
# Output is: [12.566370614359172, 28.274333882308138, 43.008403427644275, 26.42079421669016]

