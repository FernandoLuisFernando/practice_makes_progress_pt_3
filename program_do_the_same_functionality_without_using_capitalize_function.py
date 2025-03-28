# Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.

def custom_capitalize(string):
    if not string:
        return "" 
    first_char = string[0].upper() if 'a' <= string[0] <= 'z' else string[0]
    rest_of_string = "".join(c.lower() if 'A' <= c <= 'Z' else c for c in string[1:])
    return first_char + rest_of_string

input_string = "hELLO, wORLD!"
print(custom_capitalize(input_string))