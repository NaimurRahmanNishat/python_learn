for i in 'programming':
    print(i)
# Output is: p \n r \n o \n g \n r \n a \n m \n m \n i \n n \n g 

for i in range (1, 5):      # 1 is initial value and 5 is condition value. This loop is continue.
    print(i)
# Output is: 1 \n 2 \n 3 \n 4

for i in range (1, 10, 2):        # 1 is initial value 10 is condition value and 2 is increment value.
    print(i)
# Output is: 1 \n 3 \n 5 \n 7 \n 9

for i in range (1, 5):
    print(i)
print(5)
# Output is: 1 \n 2 \n 3 \n 4 \n 5

for i in range (1, 18):
    if i % 4 == 0:
        print(i)
# Output is: 4 \n 8 \n 12 \n 16

for name in ['naimur', 'rahman', 'nishat']:
    print(name)
# Output is: naimur \n rahman \n nishat

for name in ['naimur', 'rahman', 'nishat']:
    print("I love",name.title())
# Output is: I love Naimur \n I love Rahman \n I love Nishat

for i in range (1, 5):
    print("*"*i)
# Output is:
# *
# **
# ***
# ****

for i in range (5, 0, -1):
    print("*"*i)
# Output is: 
# *****
# ****
# ***
# **
# *

for i in range (1, 5):
    print("*",*i)     # don't use comma otherwise output is worng.
# Output is: TypeError: Value after * must be an iterable, not int

# for nested loop.
for i in range (0, 2):
    for j in range (1, 3):
        print(f"{i}, {j}")        # f is format. format is writting system.
# Output is: 
# 0, 1
# 0, 2
# 1, 1
# 1, 2

for i in [5,3,1,4]:
    print("*"*i)
# Output is:
# *****
# ***
# *
# ****