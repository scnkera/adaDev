SNOWMAN_WORD = "broccoli"

def get_letter_from_user():
    user_input_string = input("Guess a letter: ")

    if len(user_input_string) > 1 or not user_input_string.isalpha():
        print("Invalid letter, please enter a single character.")

    return user_input_string
    
def snowman():
    waiting_for_correct_guess = True

    while waiting_for_correct_guess:
        user_input = None
        while not user_input:
            user_input = get_letter_from_user()
        
        if user_input not in SNOWMAN_WORD:
            print(f'The letter {user_input} is not in the word')
        else:
            waiting_for_correct_guess = False
            print("You guessed a letter that's in the word!")
            return True

snowman()