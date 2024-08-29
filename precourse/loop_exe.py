# Example 1: while loop
counter = 0
while counter < 10:
    counter = counter + 2
    print(f"The value of counter is {counter}")

# Example 2: while loop with flag
keep_running = True
counter = 0
while keep_running:
    counter = counter + 3
    if counter > 10 :
        keep_running = False
    print(f"The value of counter is {counter}")

# Example 3: another while loop with flag
ask_for_input = True 
while ask_for_input: 
    user_input = input("Do you want to keep running? Enter 'y' or 'n': ") 
    ask_for_input = (user_input == 'y')

# Example 4: for loop using range with implicit start
for number in range(3):
    print(f"The value of num is {number}")

# Example 5: for loop using range with explicit start and stop
for number in range(2, 5):
    print(f"The value of num is {number}")

# Example 6: for-in loop over a collection
a_string = "Hello, World!"
for letter in a_string:
    print(f"The current letter is {letter}")

# Example 6: for-in loop over a collection with intervals

for number in range(2, 11, 2):
    print(f"The value of number is {number}")

def print_ten(word):
    for num in range (1,11):
        print(f'{num} {word} ')

word = input("Insert any input: ")       
print_ten(word)

# Example 7: word/num

def print_ten(word):
    for num in range (1,11):
        print(f'{num} {word} ')

print_ten('snow')
print_ten('')
print_ten('123')