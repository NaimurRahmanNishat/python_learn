#follow codecademy (https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-strings/cheatsheet)

courseName = "We are learning python"
print(len(courseName))
# Output is: 22  Another system below.

courseName = "We are learning python"
textNumber = len(courseName)
print(textNumber)
# Output is: 22

courseName = "We are learning python"
print(courseName.upper())
# Output is: WE ARE LEARNING PYTHON     // upper(uppercase) is a built in fucntion. 

courseName = "We are learning python"
print(courseName.title())
# Output is: We Are Learning Python     // first letter is capitailize in this title function.

courseName = "We are learning python"
print(courseName.format())
# Output is: We are learning python     // only first letter is capitailize.

courseName = "We are learning python"
print(courseName.strip())
# Output is: We are learning python     // format and strip function both same.

courseName = "We are learning python"
print(courseName.split())
# Output is: ['We', 'are', 'learning', 'python']     // every word is separate and group in tuple.

courseName = "We are learning python"
print(courseName.find("l"))
# Output is: 7  number index    // find() takes at least 1 argument (0 given)

courseName = "We are learning python"
textEdit = "-".join(["We", "are", "learning", "python"])     # join function added every element. And this element obiesly indicate this tuple. 
print(textEdit)
# Output is: We-are-learning-python   

courseName = "We are learning python"
print(courseName[3])       # index number 
print(courseName.find("r"))      # index value
# Output is: a \n 4 

courseName = "We are learning python"
print(courseName.replace("are", "ware"))     # repalce ware
# Output is: We ware learning python 

courseName = "We are learning python"
print(courseName.endswith("n"))         # boolean value return 
# Output is: True      // This is boolean

courseName = "Wearelearningpython"
sliceName = courseName[0:2]          # 0 is index number and 2 in index value (index value is: 1-w, 2-e,  we)
print(sliceName)
# Output is: we

courseName = "Wearelearningpython"
sliceName = courseName[1:-2] 
print(sliceName)
# Output is: earelearningpyth


# Practice and problm solving
firstName = input("Write your first name: ")
secondName = input("Write your second name: ")
fullName = f"{firstName} {secondName}"       # separate word
print("Your full name is:",fullName)
print("Title format:",fullName.title())
print("Upper case format:",fullName.upper())
replaceSecondName = input("Replace your second name:")
replaceFullName = fullName.replace(secondName,replaceSecondName)
print(fullName,"Your new full name is:",replaceFullName)


# in operator
animal = "cat parrot dog lion tiger"
print("cat lion" in animal)        # Output return boolean type. This is case sensitive formate mind it.
# Output is: Ture
