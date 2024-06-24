x, y = map(int, input("=> ").split())
print(x,y)       # input : 5 6
#Output is: 5 6

# list map
number = list(map(int, input("Provide number: ").split()))
print(number)
# Output is: [1, 2, 3, 4, 5]

number = list(map(int, input("Provide number: ").split()))
print(*number)
# Output is: 1, 2, 3, 4, 5