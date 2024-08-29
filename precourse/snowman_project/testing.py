# Constant variable that references the hidden word 
SNOWMAN_WORD = "broccoli"

def get_letter_from_user():
    valid_input = False
    user_input_string = None

    while not valid_input:
        user_input_string = input("Guess a letter: ")
        if not user_input_string.isalpha():
            print("Invalid letter, please enter a letter.")
        elif len(user_input_string) > 1:
            print("Invalid letter, you can on enter 1 letter.")
        else:
            valid_input = True
            
    return user_input_string
    
def snowman():
    waiting_for_correct_guess = True

    while waiting_for_correct_guess:
        user_input = get_letter_from_user()

        if user_input in SNOWMAN_WORD:
            waiting_for_correct_guess = False
            print("You guessed a letter that's in the word!")
            return True
        else:
            print(f'The letter {user_input} is not in the word')
            return False

snowman()


