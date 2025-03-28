# Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.

def custom_lstrip(string):
    return string[next((i for i, c in enumerate(string) if c != ' '), len(string)):]

input_string = "      hello, world!"
output_string = custom_lstrip(input_string)
print("orignal string", repr(input_string))
print("Modified string", repr(output_string))
