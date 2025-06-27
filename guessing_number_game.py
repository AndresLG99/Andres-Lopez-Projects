# Ask for user's name
# Gives an intro to the game
# Starts with 8 attempts
# Range between 1 and 100
# Select a random number in the range
# Asks user to input a number in the range
# Handles numbers out of range, doesn't affect remaining attempts
# If the inputed number is lower than the chosen number
    # Update range
    # Print message stating the inputed number is lower
# If the inputed number is higher than the chosen number
    # Update range
    # Print message stating the inputed number is higher
# If the inputed number is correct
    # Print winning message
    # Attempts taken
# Loop until user wins or attempts are equal to 0

# IMPORTS
from random import randint

# INITIAL DATA STRUCTURES AND VARIABLES
attempts = 8
start_range = 1
end_range = 100
secret_num = randint(start_range, end_range)
on_off = True
options = ["yes", "no"]
previous_attempts = []

# GAME
name = input("What is your name?\n")
while not name.isalpha():
    name = input("What is your name? ")

print(f"Hi {name.capitalize()}.\n")
print("Welcome to NUMBER GUESSING GAME.\n")
print(f"There's a secret number between {start_range} and {end_range}.\n")
print(f"You'll have '{attempts}' attempts to try and guess the number.\n")
print("After every wrong guess the range will shorten.\n")
print("But you'll have lost an attempt.\n")

first_choice = input("Would you like to play again? (Yes/No)\n").lower()
while first_choice not in options:
    first_choice = input("Would you like to play? (Yes/No)\n")

if first_choice == options[0]:
    print("Great! Let's start.\n")

    while on_off:
        print(f"You have '{attempts}' attempts left.\n")
        num_choice = input(f"Enter a number between {start_range} and {end_range}\n")

        while not num_choice.isnumeric():
            num_choice = input(f"Enter a number between {start_range} and {end_range}\n")

        while int(num_choice) not in range(start_range, end_range + 1):
            num_choice = input(f"Enter a number between {start_range} and {end_range}\n")

        num_choice = int(num_choice)

        if attempts == 1:
            print("Oops! You lose.\n")
            print(f"The secret number was {secret_num}.")
            on_off = False

        else:
            if num_choice == secret_num:
                print("Good job! You guessed the secret number.\n")
                print(f"It took you '{9 - attempts}' attempts.\n")
                on_off = False

            elif num_choice < secret_num:
                if num_choice in previous_attempts:
                    pass
                else:
                    print("Too low. Try again.\n")
                    start_range = num_choice + 1
                    attempts -= 1
                    previous_attempts.append(num_choice)

            elif num_choice > secret_num:
                if num_choice in previous_attempts:
                    pass
                else:
                    print("Too high. Try again.\n")
                    end_range = num_choice - 1
                    attempts -= 1
                    previous_attempts.append(num_choice)

else:
    print("Okay, bye bye.")