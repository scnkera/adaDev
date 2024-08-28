def count_item_in_list(item, list_of_items):
    num_of_appearances = 0
    
    for i in list_of_items:
        if i == item:
            num_of_appearances += 1
            
    print(num_of_appearances)
    return num_of_appearances

count_item_in_list(3, [1, 3, 3, 6, 2, 3, 9])
count_item_in_list("cat", ["dog", "cow", "goat", "pig"])
count_item_in_list(38, [])
count_item_in_list("dog", ["dog", "cat", "cow", "goat", "pig"])