def extract(input_string):
    length = len(input_string)

    if length % 2 != 0:
        middle_index = length // 2
        return input_string[middle_index]
        
    else:
        middle_index1 = length // 2 - 1
        middle_index2 = length // 2
        return input_string[middle_index1]+input_string[middle_index2]

input_string = input("Enter a string: ")
output = extract(input_string)
print(output)
