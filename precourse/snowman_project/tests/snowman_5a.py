import random
from wonderwords import RandomWord
# https://pypi.org/project/wonderwords/


# Constant variable that references the hidden word 
SNOWMAN_WRONG_GUESSES = 7
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
    
    for i in range(SNOWMAN_WRONG_GUESSES - num_wrong_guesses, SNOWMAN_WRONG_GUESSES):
        print(SNOWMAN_GRAPHIC[i])

def snowman():
    r = RandomWord()
    snowman_word = r.word(
        word_min_length=SNOWMAN_MIN_WORD_LENGTH, 
        word_max_length=SNOWMAN_MAX_WORD_LENGTH)
    
    print(snowman_word)

    snowman_word_dict = build_word_dict(snowman_word)
    wrong_guesses_list = []

   
    while len(wrong_guesses_list) < SNOWMAN_WRONG_GUESSES:
        user_input = get_letter_from_user(snowman_word_dict, wrong_guesses_list) 

        if user_input in snowman_word_dict:
            print(f'Great Job! The letter {user_input} is in the word')
            snowman_word_dict[user_input] = True
        else:
            print(f'The letter {user_input} is not in the word')
            wrong_guesses_list.append(user_input)

        print_snowman_graphic(len(wrong_guesses_list))

    # print_snowman_graphic(len(wrong_guesses_list))
    
    print(f"Wrong guesses: {wrong_guesses_list}")
    print(f"Correct guesses: {snowman_word_dict}")


def build_word_dict(snowman_word):
    # snowman_word = "party"
    snowman_word_dict = {}
    # print(snowman_word)
    for letter in snowman_word:
        # print(letter)
        if letter not in snowman_word_dict:
            snowman_word_dict[letter] = False
    print(snowman_word_dict)
    return snowman_word_dict

# def print_word_progress_string(snowman_word, snowman_word_dict):
#     # snowman_word = "lookout"
#     output_str = ""
#     # snowman_word_dict = {'l': True, 'o': False, 'k': True, 'u': False, 't': False}
#     # new_string = ""
#     for letter in snowman_word:
#         if snowman_word_dict[letter]:
#             output_str.append(letter)
#         else:
#             output_str.append("_")
#     output_str = output_str[:-1]
#     print(output_str)

# # print_word_progress_string(snowman_word, snowman_word_dict)

# def get_word_progress(snowman_word, snowman_word_dict):
#     # word="lookout"
#     # snowman_word_dict = {'l': True, 'o': True, 'k': True, 'u': False, 't': False}
#     for letter in snowman_word:
#         if not snowman_word_dict[letter]:
#             return False
#     return True

# get_word_progress()   


snowman()