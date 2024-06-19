sum = 5+4
sub = 6-3
mul = 3*2
reminder = 7%3
div = 7/3   # print floating point number.
divi = 7//3  # don't show float number. give integer number.
print(sum)
print(sub)
print(mul)
print(reminder)
print(div)
print(divi)
# Output is: 9 \n 3 \n 6  \n 1  \n 2.33  \n 2 ( \n means new line)


# Project name: What did you lived in this earth in days.
print("What is your name: ")
name = input()  # user input
print(name, "How old are you?")
# age = input()  # This user input is string data type. This data type convert integer.
age = int (input())  # convert integer data type.

days = age * 365
hours = age * 8760     # 365 *24
minutes = age * 525600     # 365 * 24 * 60
seconds = age * 31536000     # 365 * 24 * 60 * 60 
print(name, 'You has lived for',days,'days',hours,'hours',minutes,'minutes',seconds,'seconds')

# Maximum and minimum 
a = 5
b = 3
print('The maximum number is:',max(a,b))  # max is a build in function.
print('The minimum number is:',min(a,b))  # min is a build in function.