def am_i_speeding(speed, speed_limit):

    # speed and speed limit validation
    if not is_valid_num(speed) or not is_valid_num(speed_limit):
        print('None')
        return None
    
    # 1) convert speed and 2) compare speed and speed limit
    converted_mph = convert_km_to_mi(speed)
    return converted_mph > speed_limit
    # if converted_mph <= speed_limit:
    #     print('False')
    #     return False
    # elif converted_mph > speed_limit:
    #     print('True')
    #     return True

def convert_km_to_mi(num):
    return num * 0.62137

def is_valid_num(num):
    return isinstance(num, int) or isinstance(num, float)
    
am_i_speeding(100, 55)
am_i_speeding(80, 55)
am_i_speeding("hello", 55)
am_i_speeding(100, "hello")