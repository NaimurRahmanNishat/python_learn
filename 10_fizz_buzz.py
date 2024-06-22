# FIZZ  &  BUZZ
# Fizz means  number % 3 = 0 This is Fizz
# Buzz means  number % 5 = 0 This is Buzz

number = 10
if(number % 3 == 0):
    print(number,"This is Fizz")
elif(number % 5 == 0):
    print(number,"This is Buzz")
elif(number % 3 ==0 and number % 5 == 0):
    print(number,"This is Fizz and Buzz")
print("Finished")
# Output is: 10 This is Buzz \n Finished     
 
number = 15
if(number % 3 == 0):
    print(number,"This is Fizz")
elif(number % 5 == 0):
    print(number,"This is Buzz")
elif number % 3 == 0 and number % 5 == 0:
    print(number,"This is Fizz and Buzz")
print("Finished")   
# Output is: 15 This is Fizz \n Finished      # python is a interpreter language python print line by line 

number = 15
if number % 3 == 0 and number % 5 == 0:
    print(number,"This is Fizz and Buzz")
elif(number % 5 == 0):
    print(number,"This is Buzz")
elif(number % 3 == 0):
    print(number,"This is Fizz")
print("Finished") 
# Output is: 15 This is Fizz and Buzz \n Finished 

# This is nested condition system.
number = 15
if number % 3 == 0:
    if number % 5 == 0:
        print(number,"This is Fizz and Buzz")
elif(number % 5 == 0):
    print(number,"This is Buzz")
elif(number % 3 == 0):
    print(number,"This is Fizz")
print("Finished")
# Output is: 15 This is Fizz and Buzz \n Finished 
