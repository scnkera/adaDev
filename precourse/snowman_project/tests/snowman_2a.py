# Constant variable that references the hidden word 
SNOWMAN_WORD = "broccoli"
SNOWMAN_WRONG_GUESSES = 7

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
    correct_guesses = 0
    wrong_guesses = 0
    
    while correct_guesses < 7 and wrong_guesses < SNOWMAN_WRONG_GUESSES:
        user_input = get_letter_from_user() 

        if user_input in SNOWMAN_WORD:
            print(f'Great Job! The letter {user_input} is in the word')
            correct_guesses += 1
        else:
            print(f'Sorry! The letter {user_input} is not in the word')
            wrong_guesses += 1

    print(f"You made {correct_guesses} correct and {wrong_guesses} incorrect guesses")  

snowman()