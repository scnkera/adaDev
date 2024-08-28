def get_value_from_dictionary(dict, key):
    if key in dict:
        value = dict[key]
        print(value)
        return value
    else:
        print("None")
        return None
        
get_value_from_dictionary({"dog":"cat", "tree":"bush", "star":"planet"}, "tree")
get_value_from_dictionary({"dog":"cat", "tree":"bush", "star":"planet"}, "chocolate")
get_value_from_dictionary({"dog":"cat", "tree":"bush", "star":"planet"}, "cat")