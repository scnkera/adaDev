# Part 1

# print("four".isnumeric()) 


# if "four".isnumeric() == "False":
#     print("sorry buck")

# else:
#     print("hello")

# Part 2

# # an example function that returns a value
# def greeting():
#     return "Hello"

# result = greeting()
# print(result) # "Hello"


# # an example function that prints Goodbye 
# # and returns None (implicit return)
# def farewell():
#     print("Goodbye")

# result = farewell() # prints "Goodbye"
# print(result) # None

# Part 3

# def compare(first, second):
#     if not isinstance(first, int) and not isinstance(second, int):
#         return None
#     elif first == second:
#         return False
#     elif first > second:
#         return True
#     elif first < second:
#         return False

# compare(3, 7)
# compare(7, 3)
# compare(7, 7)


# def compare(first, second):
#     if not isinstance(first, int) and not isinstance(second, int):
#         return None
#     else:
#         return first > second

# compare(3, 7)
# compare(7, 3)
# compare(7, 7)

# Part 4

def convert_mi_to_km(miles):
    if not isinstance(miles, int) and not isinstance(miles, float):
        return None
    else:
        km = miles*1.6
        return km
        
miles(1)
miles(0)
miles(3.5)