import random

RANGE_LOW = 0
RANGE_HIGH = 100

def get_number_from_user():
    attempting_valid_input = True
    user_input = None

    while attempting_valid_input:
        user_input_string = input("Guess the number: ")

        if user_input_string.isnumeric():
            user_input = int(user_input_string)
            attempting_valid_input = False
        else:
            print("You must input a number!")

    return user_input

def guess_the_number():
    random_number = random.randint(RANGE_LOW, RANGE_HIGH)

    waiting_for_correct_guess = True
    num_guesses = 0
    MAX_GUESSES = 5

    while (waiting_for_correct_guess and num_guesses < MAX_GUESSES):

        user_input = get_number_from_user()

        if user_input == random_number:
            num_guesses += 1
            waiting_for_correct_guess = False
            print("You guessed the number! Good job!")
            print(f'Guess # {num_guesses}')
        elif user_input < RANGE_LOW or user_input > RANGE_HIGH:
            print("Your guess is out of bounds.")
            print(f"It must be between {RANGE_LOW} and {RANGE_HIGH}")
        elif user_input > random_number:
            num_guesses += 1
            print("Your guess is too high")
            print(f'Guess # {num_guesses}')
        elif user_input < random_number:
            num_guesses += 1
            print("Your guess is too low")
            print(f'Guess # {num_guesses}')

    if waiting_for_correct_guess:
        print(f"You ran out of guesses! The correct answer was {random_number}.")

guess_the_number()
