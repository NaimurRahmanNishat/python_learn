file = open("21_data.txt", "r")
print(file.read())
# Output is: 21_data.txt

file = open("new_data.txt", "a")
file.write("I am a student")
# read
file = open("new_data.txt", "r")
print(file.read())
file.close()

file = open("new_data.txt", "w")
file.write("Nishat! \nI am a student")
# write
file = open("new_data.txt", "r")
print(file.read())
file.close()
# Output is: Nishat! \nI am a student


# remove file
import os
os.remove('new_data.txt')






