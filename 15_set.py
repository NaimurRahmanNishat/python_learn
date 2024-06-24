# set indicate system is {This is set}. Set is second braket.

number = [1,2,3,2,3,1,4,5,6,4]          # This is a list.
unique_number = []                      # First of all unique is blank.
for num in number:                      # number store in num.
    if num not in unique_number:        # If num and unique both not same then go to next line.
        unique_number.append(num)       # Then unique_number store the number. append function means store the value.
    else:
        continue                        # If condition is false none the less condition is continue.
print(unique_number)                    # print the unique_number.
# Output is: [1, 2, 3, 4, 5, 6]

number = [1,2,3,2,3,1,4,5,6,4] 
print(set(number))
# Output is: {1, 2, 3, 4, 5, 6}

# Set disadvantage is set has no index number. for example
number = {1, 2, 3, 4, 5, 6, 3, 2}
print(number[3])
# Output is: 'set' object is not subscriptable

number = {1, 2, 3, 4, 5, 6, 3, 2}
number.add(33)
print(number)
# Output is: {1, 2, 3, 4, 5, 6, 33}

number = {1, 2, 3, 4, 5, 6, 3, 2}
number.update([33,32,11])                # Update time use [Third braket] you must be minded.
print(number)
# Output is: {1, 2, 3, 4, 5, 6, 11, 32, 33}



