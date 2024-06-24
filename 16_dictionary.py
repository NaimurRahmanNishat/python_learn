# dictionary indicate system is {This is dictionary. A dictionary has two part one is key and another one is value for example: "name" : "nishat". This name is key and nishat is value}. Dictionary is second braket. python dictionary and javascript object both same.

dictonary ={
    "Name" : "Nishat",
    "Age" : 24,
    "Phone_number" : "88+01568450889" 
}
print(dictonary)
# Output is: {'Name': 'Nishat', 'Age': 24, 'Phone_number': '88+01568450889'}

dictonary ={
    "Name" : "Nishat",
    "Age" : 24,
    "Phone_number" : "88+01568450889" 
}
print(dictonary["Name"])
# Output is: Nishat

dictonary ={
    "Name" : "Nishat",
    "Age" : 24,
    "Phone_number" : "88+01568450889" 
}
print(dictonary.get("Name"))
# Output is: Nishat

dictonary ={
    "Name" : "Nishat",
    "Age" : 24,
    "Phone_number" : "88+01568450889" 
}
print(dictonary.get("Height"))
# Output is: None 

dictonary ={
    "Name" : "Nishat",
    "Age" : 24,
    "Phone_number" : "88+01568450889" 
}
print(dictonary.get("Height", "You entered an Invalid value"))
# Output is: You entered an Invalid value

# Practice integer number convert string number.
number ={
    '0' : 'zero',
    '1' : 'one',
    '2' : 'two',
    '3' : 'three',
    '4' : 'four',
    '5' : 'five',
    '6' : 'six',
    '7' : 'seven',
    '8' : 'eight',
    '9' : 'nine'
}
user_number = input("=>")                  # 01568450889
for i in user_number:
    print(number.get(i,"(!)"), end=" ")
# Output is: zero one five six eight four five zero eight eight nine 