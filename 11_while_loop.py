initial_value = 1
while initial_value <= 10:
    print(initial_value)
    initial_value += 1
print("Finished")
# Output is: 1 \n 2 \n 3 \n 4 \n 5 \n 6 \n 7 \n 8 \n 9 \n 10 \n Finished


# Guessing Game using while loop.
secret_number = 33       # You set up this secreet number
guess_count = 0          # Your secreet number starting point
guess_limit = 2          # Your secreet number ending point
while guess_count <= guess_limit:       # Your starting secreet number <= Your secreet ending number
    user_guess_number = int(input("Guess number:> "))       # guess your secreet number
    guess_count += 1     # You type secreet number upper limit
    if secret_number == user_guess_number:          # Your secreet number and Your guess number if both number is same then you are win otherwise you lose.
        print("You win!!")
        break    # You win the game then program is break otherwise continue the condition as long as you lose.
else:
    print("You lose...")


# Light on off project
"""
> help      # Your speck voice.
1. on - to switch on the light
2. off - to switch off the light
3. sleep - to exit the program

other input - I don't understand your command

> on
light truned on

> off
light truned off
"""

check = ""
light_on = False
while (check != 'sleep'):
    check = input(">> ").lower()
    if check == 'on':
        if light_on:
            print("light is already in on mode")
        else:
            light_on = True
            print("light truned on mode")
    elif check == 'off':
        if not light_on:
            print("light is already in off mode")
        else:
            light_on = False
            print("light truned off mode")
    elif check == 'sleep':
        break
    elif check == 'help':
        print('''
            1. on - light on
            2. off - light off
            3. help - exit program
            ''')
    else:
        print("I don't understand your command.....")