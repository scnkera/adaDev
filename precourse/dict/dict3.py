def build_a_dictionary(keys, values):
    output = {}
    index = 0

    if len(keys) == len(values):
        for key in keys:
            output[key] = values[index]
            index += 1
                
        print(output)
        return output
    else:
        print("None")
        return None

build_a_dictionary(["dog", "cat", "bird", "mouse"], [1, 2, 3, 4])
build_a_dictionary([1, 2, 3, 4], ["dog", "cat", "bird", "mouse"])
build_a_dictionary([1, 2,], ["dog", "cat", "bird", "mouse"])
build_a_dictionary(["dog", "cat", "bird", "mouse"], [])