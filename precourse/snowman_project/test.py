# def build_word_dict():
#     snowman_word = "soccer"
#     word_dict = {}
#     print(snowman_word)
#     for i in snowman_word:
#         print(i)
#         word_dict[i] = False
#     print(word_dict)
    

# build_word_dict()

# def build_word_dict():
#     snowman_word = "soccer"
#     word_dict = {}
#     print(snowman_word)
#     for letter in snowman_word:
#         print(letter)
#         if letter not in word_dict:
#             word_dict[letter] = False
#     print(word_dict)       
#     return word_dict

    

# build_word_dict()

# def generate_word_progress_string(word, word_dict):
#     output_str = ""

#     for letter in word:
#         if word_dict[letter]:
#             output_str += f'{letter} '
#         else:
#             output_str += "_ "
#     output_str = output_str[:-1]
#     print(output_str)
#     # return(output_str)

# generate_word_progress_string()


# def print_word_progress_string():
#     snowman_word = "swamp"
#     output_str = ""
#     snowman_word_dict = {"a":True, "m": True, "p": True, "s": True, "w": True}
#     # new_string = ""
#     for letter in snowman_word:
#         if snowman_word_dict[letter]:
#             output_str += letter
#         else:
#             output_str += "_"
#     print(output_str)

# print_word_progress_string()

# def get_word_progress():
#     word="lookout"
#     word_dict = {'l': False, 'o': True, 'k': True, 'u': True, 't': True}
#     for letter in word:
#         if not word_dict[letter]:
#             print("False")
#             return False
#     print("True")
#     return True

# get_word_progress()    

def get_word_progress():
    snowman_word="stream"
    snowman_word_dict = {'s': True, 't': True, 'r': True, 'e': True, 'a': True, 'm': True}
    for letter in snowman_word:
        if not snowman_word_dict[letter]:
            print('False')
            return False
    print('True')
    return True

get_word_progress()  
