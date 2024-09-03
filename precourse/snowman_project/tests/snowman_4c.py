import random
from wonderwords import RandomWord
# https://pypi.org/project/wonderwords/


# Constant variable that references the hidden word 
SNOWMAN_WRONG_GUESSES = 7
SNOWMAN_MAX_WORD_LENGTH = 8
SNOWMAN_MIN_WORD_LENGTH = 5



def get_letter_from_user(wrong_guesses_list, correct_guesses_list):
    valid_input = False
    user_input_string = None

    while not valid_input:
        user_input_string = input("Guess a letter: ")
        if not user_input_string.isalpha():
            print("Invalid letter, please enter a letter.")
        elif len(user_input_string) > 1:
            print("Invalid letter, you can on enter 1 letter.")
        elif user_input_string in wrong_guesses_list or user_input_string in correct_guesses_list:
            print("You have already guessed that letter!")
        else:
            valid_input = True
            
    return user_input_string

def print_snowman(wrong_guesses_count):
    SNOWMAN_GRAPHIC = [
        '*   *   *  ',
        ' *   _ *   ',
        '   _[_]_ * ',
        '  * (")    ',
        '  \\( : )/ *',
        '* (_ : _)  ',
        '-----------'
    ]
    
    for i in range(SNOWMAN_WRONG_GUESSES - wrong_guesses_count, SNOWMAN_WRONG_GUESSES):
        print(SNOWMAN_GRAPHIC[i])

def snowman():
    r = RandomWord()
    snowman_word = r.word(
        word_min_length=SNOWMAN_MIN_WORD_LENGTH, 
        word_max_length=SNOWMAN_MAX_WORD_LENGTH)
    
    print(snowman_word)

    correct_guesses_list = []
    wrong_guesses_list = []
   
    while len(wrong_guesses_list) < SNOWMAN_WRONG_GUESSES:
        user_input = get_letter_from_user(wrong_guesses_list, correct_guesses_list) 

        if user_input in snowman_word:
            print(f'Great Job! The letter {user_input} is in the word')
            correct_guesses_list.append(user_input)
        else:
            print(f'Sorry! The letter {user_input} is not in the word')
            wrong_guesses_list.append(user_input)

    print_snowman(len(wrong_guesses_list))
    
    print(f"Wrong guesses: {wrong_guesses_list}")
    print(f"Correct guesses: {correct_guesses_list}")

snowman()
