import random
from wonderwords import RandomWord
# https://pypi.org/project/wonderwords/


# Constant variable that references the hidden word 
SNOWMAN_MAX_WRONG_GUESSES = 7
SNOWMAN_MAX_WORD_LENGTH = 8
SNOWMAN_MIN_WORD_LENGTH = 5



def get_letter_from_user(snowman_word_dict, wrong_guesses_list):
    valid_input = False
    user_input_string = None

    while not valid_input:
        user_input_string = input("Guess a letter: ")
        if not user_input_string.isalpha():
            print("Invalid letter, please enter a letter.")
        elif len(user_input_string) > 1:
            print("Invalid letter, you can only enter 1 letter.")
        elif user_input_string in wrong_guesses_list:
            print("You have already guessed that letter, and it's not in the word!")
        elif user_input_string in snowman_word_dict and snowman_word_dict[user_input_string]:
            print("You have already guessed that letter, and it is in the word!")
        else:
            valid_input = True
            
    return user_input_string

def print_snowman_graphic(num_wrong_guesses):
    SNOWMAN_GRAPHIC = [
        '*   *   *  ',
        ' *   _ *   ',
        '   _[_]_ * ',
        '  * (")    ',
        '  \\( : )/ *',
        '* (_ : _)  ',
        '-----------'
    ]
    
    # Loop from 0 up to the minimum of num_wrong_guesses and SNOWMAN_WRONG_GUESSES
    for i in range(min(num_wrong_guesses, SNOWMAN_MAX_WRONG_GUESSES)):
        print(SNOWMAN_GRAPHIC[i])


def snowman():
    r = RandomWord()
    snowman_word = r.word(
        word_min_length=SNOWMAN_MIN_WORD_LENGTH, 
        word_max_length=SNOWMAN_MAX_WORD_LENGTH)
    
    print(snowman_word)

    snowman_word_dict = build_word_dict(snowman_word)
    wrong_guesses_list = []
    wrong_guesses_str = ""

    while len(wrong_guesses_list) < SNOWMAN_MAX_WRONG_GUESSES:
        all_letters_guessed = get_word_progress(snowman_word, snowman_word_dict) 
         
        if all_letters_guessed:
            print("Congratulations, you win!")
            break

        user_input = get_letter_from_user(snowman_word_dict, wrong_guesses_list) 

        if user_input in snowman_word_dict:
            print(f'You guessed a letter that is in the word!')
            snowman_word_dict[user_input] = True
        else:
            print(f'The letter {user_input} is not in the word')
            wrong_guesses_list.append(user_input)
            wrong_guesses_str += f'{user_input} '

        print_snowman_graphic(len(wrong_guesses_list))
        print_word_progress_string(snowman_word, snowman_word_dict)
        # print(f"Wrong guesses: {wrong_guesses_list}")
        print(f"Wrong guesses: {wrong_guesses_str}")
        # print(snowman_word_dict)
        # print(f'all_letters_guessed: {all_letters_guessed}')

    if len(wrong_guesses_list) >= SNOWMAN_MAX_WRONG_GUESSES:
        print(f"Game Over! You're out of guesses!")

def build_word_dict(snowman_word):
    snowman_word_dict = {}
    # print(snowman_word)
    for letter in snowman_word:
        if letter not in snowman_word_dict:
            snowman_word_dict[letter] = False
    # print(snowman_word_dict)
    return snowman_word_dict

def print_word_progress_string(snowman_word, snowman_word_dict):
    output_str = ""

    for letter in snowman_word:
        if snowman_word_dict[letter]:
            output_str += f'{letter} '
        else:
            output_str += f'_ '
    output_str = output_str[:-1]
    print(output_str)

def get_word_progress(snowman_word, snowman_word_dict):

    for letter in snowman_word:
        if not snowman_word_dict[letter]:
            return False
    return True
  


snowman()