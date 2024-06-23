# python list is a one kind of array. python list and array almost similar.

animal_list = ["tiger", "lion", "cat", "dog", "rabbit"]
print(animal_list)
# Outpurt is: ['tiger', 'lion', 'cat', 'dog', 'rabbit']

animal_list = ["tiger", "lion", "cat", "dog", "rabbit"]
print(animal_list[2])
# Output is: cat

animal_list = ["tiger", "lion", "cat", "dog", "rabbit"]
print(animal_list[1:4])
# Output is: ['lion', 'cat', 'dog']

animal_list = ["tiger", "lion", "cat", "dog", "rabbit"]
print(animal_list[-4])
# Output is: lion

animal_list = ["tiger", "lion", "cat", "dog", "rabbit"]
animal_list[1] = "cow"
print(animal_list)
# Output is: ['tiger', 'cow', 'cat', 'dog', 'rabbit']

animal_list = ["tiger", "lion", "cat", "dog", "rabbit"]
animal_list.insert(3,"snake")
print(animal_list)
# Output is: ['tiger', 'lion', 'cat', 'snake', 'dog', 'rabbit']

animal_list = ["tiger", "lion", "cat", "dog", "rabbit"]
animal_list.remove("cat")
print(animal_list)
#Output is: ['tiger', 'lion', 'dog', 'rabbit']

animal_list = ["tiger", "lion", "cat", "dog", "rabbit"]
del animal_list [1]
print(animal_list)
# Output is: ['tiger', 'cat', 'dog', 'rabbit']

animal_list = ["tiger", "lion", "cat", "dog", "rabbit"]
animal_list.append("rat")
print(animal_list)
# Output is: ['tiger', 'lion', 'cat', 'dog', 'rabbit', 'rat']

animal_list = ["tiger", "lion", "cat", "dog", "rabbit"]
animal_list.pop()     # pop remove the last value.
print(animal_list)
# Output is: ['tiger', 'lion', 'cat', 'dog']

animal_list = ["tiger", "lion", "cat", "dog", "rabbit"]
animal_list.clear()     # All element clear.
print(animal_list)
# Output is: []

animal_list = ["tiger", "lion", "cat", "dog", "rabbit"]
new_list = animal_list.copy()
print(new_list)
# Output is: ['tiger', 'lion', 'cat', 'dog', 'rabbit']

animal_list = ["tiger", "lion", "cat", "dog", "rabbit"]
for list in animal_list:
    print(list)
# Output is: tiger \n lionb \n cat \n dog \n rabbit 

number_list = [1, 2, 3]
new_number_list = [4, 5, 6]
number_list.extend(new_number_list)    # extend function add number.
print(number_list)
# Output is: [1, 2, 3, 4, 5, 6]

new_list = [4,6,2,7,11,41,23,12]
print(max(new_list))    # max is a built in function.
# Output is: 41

new_list = [4,6,2,7,11,41,23,12]
print(min(new_list))    # min is a built in function.
# Output is: 2

num_list = [4,6,2,7,11,41,23,12]
max = num_list[0]
for num in num_list:
    if num > max:
        max = num
print(max)
# Output is: 41

new_list = [2,4,7,3,6]
new_list.sort()
print(new_list)
# Output is: [2, 3, 4, 6, 7]

new_list = [2, 4, 7, 3, 6]
new_list.sort()
print(", ".join(map(str, new_list)))    # first of all join this comma and then added map function map function print string value added string mathod this mathod string to integer.
# Output is: 2, 3, 4, 6, 7

# added matrix.
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,90]
]
print(matrix[1][1])
# Output is: 5

number = [2,3,4,6,8,5,3,2,4,6]
print(number.count(3))            # count function is a number check mathod.
# Output is: 2