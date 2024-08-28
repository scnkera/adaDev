def icecream_sundae(flavors, toppings):
    output_list = []
    
    if flavors != [] or toppings != []:
        for flavor in flavors:
            for topping in toppings:
                output_item = f'{flavor} with {topping}'
                output_list.append(output_item)

    print(output_list)
    return output_list

icecream_sundae(["vanilla", "chocolate", "strawberry"], ["whipped cream", "nuts", "a cherry"])
icecream_sundae(["a", "b"], ["c", "d", "e"])
icecream_sundae(["vanilla", "strawberry"], [])
icecream_sundae([], ["chocolate sauce", "caramel sauce"])