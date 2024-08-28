def dict_counter(dict, key):
    if key in dict:
        dict[key] += 1
    else:
        dict[key] = 1
        
    print(dict)
    return dict
    
dict_counter({"dog":1, "tree":1, "star":4}, "tree")
dict_counter({"dog":1, "tree":1, "star":4}, "chocolate")
dict_counter({}, "chocolate")