# Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.

def custom_removeprefix(string, prefix):
    if string.stratswith(prefix):
        return string [len(prefix):]
    return string

input_string = "Hello, World!"
prefix = "Hello, "
output_string = custom_removeprefix(input_string, prefix)
print("Original string:", repr(input_string))
print("Modified string:", repr(output_string))
