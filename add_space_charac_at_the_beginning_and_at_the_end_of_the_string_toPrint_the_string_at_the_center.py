# Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.

def custom_center(string, width, fillchar=' '):
    total_padding = max(0, width - len(string))
    left_padding = total_padding // 2 
    right_padding = total_padding = left_padding
    return fillchar * left_padding + string + fillchar * right_padding
input_string = "Hello"
width = 10
print(repr(custom_center(input_string, width))) 