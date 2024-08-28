def find_index_of_item(item, list_of_items):
    if item in list_of_items:
        index = list_of_items.index(item)
        print(index)
        return index
    else:
        print(-1)
        return -1
        
find_index_of_item(3, [1, 4, 5, 6, 2, 3, 9])
find_index_of_item("cow", ["dog", "cow", "goat", "pig"])
find_index_of_item("chocolate", [])
find_index_of_item(-93, [1, 30, -93, 99, -3, -93, 25, 16])