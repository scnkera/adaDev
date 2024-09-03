import random
from wonderwords import RandomWord
# https://pypi.org/project/wonderwords/


# Constant variable that references the hidden word 
SNOWMAN_WRONG_GUESSES = 7
SNOWMAN_MAX_WORD_LENGTH = 8
SNOWMAN_MIN_WORD_LENGTH = 5



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

def print_snowman(wrong_guesses_count):
    SNOWMAN_0 = '*   *   *  '
    SNOWMAN_1 = ' *   _ *   '
    SNOWMAN_2 = '   _[_]_ * '
    SNOWMAN_3 = '  * (")    '
    SNOWMAN_4 = '  \\( : )/ *'
    SNOWMAN_5 = '* (_ : _)  '
    SNOWMAN_6 = '-----------'
    
    for index in range(SNOWMAN_WRONG_GUESSES - wrong_guesses_count, SNOWMAN_WRONG_GUESSES):
        if index == 0:
            print(SNOWMAN_0)
        elif index == 1:
            print(SNOWMAN_1)
        elif index == 2:
            print(SNOWMAN_2)
        elif index == 3:
            print(SNOWMAN_3)
        elif index == 4:
            print(SNOWMAN_4)
        elif index == 5:
            print(SNOWMAN_5)
        elif index == 6:
            print(SNOWMAN_6)

def snowman():
    r = RandomWord()
    snowman_word = r.word(
        word_min_length=SNOWMAN_MIN_WORD_LENGTH, 
        word_max_length=SNOWMAN_MAX_WORD_LENGTH)
    
    print(snowman_word)

    wrong_guesses_list = []
    
    
    while len(wrong_guesses_list) < SNOWMAN_WRONG_GUESSES:
        user_input = get_letter_from_user() 

        if user_input in snowman_word:
            print(f'Great Job! The letter {user_input} is in the word')
        else:
            print(f'Sorry! The letter {user_input} is not in the word')
            wrong_guesses_list.append(user_input)

    print_snowman(len(wrong_guesses_list))
    
    print(f"Wrong guesses: {wrong_guesses_list}")

snowman()
