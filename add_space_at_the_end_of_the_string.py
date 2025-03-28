# Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.

def custom_ljust(string, width, fillchar=' '):
    return string + fillchar * (width - len(string)) if len(string) < width else string

input_string = "Hello"
width = 10
print(repr(custom_ljust(input_string, width)))