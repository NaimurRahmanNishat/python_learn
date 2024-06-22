# comparisum / conditional operator (both same)

a=10 
b=5
if(a>b):     # The clon working at braket.
    print("Yes it is valid condition")    # This is a indent system (1 indent = 4 space)
print("finished our condition")  
# Output is: Yes it is valid condition \n finished our condition

if(10==5):
    print("Yes it is a valid condition")
else:
    print("No it is not a valid condition")
# Output is: No it is not a valid condition

age = int (input("Enter youtr age: "))     # 24
if(age>=18):
    print("Yes you can vote")
else:
    print("No You can't vote")
# Output is: Yes you can vote

age = int (input("Enter your age: "))   #24
if(age>=1 and age<13):
    print("child")
elif(age>=13 and age<20):
    print("Teenager")
elif(age>=20 and age<40):
    print("Young")
else:
    print("Old")
# Output is: Young

number = (input("Enter your number: "))     # you don't indicate data type, use int data type(object of type 'int' has no len())
if len(number)>11:
    print("Your number is too long")
elif len(number)<11:
    print("Your number is too short")
elif len(number)==11:
    print("Thank you,",number)   # 01568450889
# Output is: Thank you, 01568450889