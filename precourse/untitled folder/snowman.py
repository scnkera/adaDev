# Constant variable that references the hidden word 
SNOWMAN_WORD = "broccoli"

def get_letter_from_user():
    user_input_string = input("Guess a letter: ")

    if user_input_string.isalpha():
        if len(user_input_string) == 1:
            return user_input_string
        else:
            print("Invalid letter please enter a single character.")
    else:
        print("Invalid letter please enter a single character.")
        return user_input_string
    
def snowman():
    user_input = get_letter_from_user()

    if user_input in SNOWMAN_WORD:
        print("You guessed a letter that's in the word!")
        return True
    else:
        print(f'The letter {user_input} is not in the word')
        return False

snowman()

def get_letter_from_user():
    user_input_string = input("Guess a letter: ")

    if user_input_string.isalpha() and len(user_input_string) == 1:
        user_input = user_input_string

        if user_input in SNOWMAN_WORD:
            print("You guessed a letter that's in the word!")
        else:
            print(f'The letter {user_input} is not in the word')

        return user_input
    else:
        print("Invalid letter please enter a single character.")
        return user_input_string

get_letter_from_user()
