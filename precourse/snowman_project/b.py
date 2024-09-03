SNOWMAN_WRONG_GUESSES = 7
num_wrong_guesses = 6
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
    for i in range(min(num_wrong_guesses, SNOWMAN_WRONG_GUESSES)):
        print(SNOWMAN_GRAPHIC[i])

print_snowman_graphic(num_wrong_guesses)