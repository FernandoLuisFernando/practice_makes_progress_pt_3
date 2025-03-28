# Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.
def custom_lower(string):
    low_str = ""
    for char in string:
        if 'a' <= char <= 'z': 
            lower_str += chr(ord(char) + 32)
        else:
            lower_str += char
    return lower_str

input_string = "Hello, WORLD!"
output_string = custom_lower(input_string)
print("Original string:", repr(input_string))
print("Modified string:", repr(output_string))