age = int (input("Age:=> "))          # input: naim
print(age)
# Output is: ValueError: invalid literal for int() with base 10: 'naim' (valueError)

try:
    age = int (input("Age:=> "))          # input: naim
    print(age)
except ValueError:
    print("Invalid value")
# Output is: Invalid value

try:
    age = 24
    day = age / 0
    print(age)
except ValueError:
    print("Invalid value")
# Output is: ZeroDivisionError: division by zero

try:
    age = 24
    day = age / 0
    print(age)
except ZeroDivisionError:
    print("You can't divide age by 0")
except ValueError:
    print("Invalid value")
# Output is: You can't divide age by 0

try:
    age = 24
    day = age / 0
    print(age)
except Exception:
    print("You can't divide age by 0")
finally:
    print("This is final code")
# Output is:
# You can't divide age by 0
# This is final code


