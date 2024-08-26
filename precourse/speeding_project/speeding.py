def am_i_speeding(speed, speed_limit):

    if not is_valid_num(speed) or not is_valid_num(speed_limit):
        return None
    
    converted_speed = convert_km_to_mi(speed)
    if converted_speed <= speed_limit:
        return False
    elif converted_speed > speed_limit:
        return True

def convert_km_to_mi(num):
    return num * 0.62137

def is_valid_num(num):
    return isinstance(num, int) or isinstance(num, float)
    
am_i_speeding(100, 55)
am_i_speeding(80, 55)
am_i_speeding("hello", 55)
am_i_speeding(100, "hello")