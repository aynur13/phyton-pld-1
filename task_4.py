def replace(input_string):
    vowels = "aeiou"
    new_string = ""

    for char in input_string:
        if char.lower() in vowels:
            new_string += char.upper()
        else:
            new_string += char
    
    return new_string

input_string = input("Enter a string: ")
output_string = replace(input_string)
print("Modified string:", output_string)
