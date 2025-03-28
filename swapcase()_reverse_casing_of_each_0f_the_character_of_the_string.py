# Prog08. swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.

def custom_swapcase(string):
    result = ""
    for char in string:
        if 'a' <= char <= "z":
            result += chr(ord(char) - 32)
        elif 'A' <= char <+ 'Z':
            result += (chr(ord(char) + 32)) 
        else: 
            result += char 
    return result

input_string = "Hello, WoRLd!"
print(custom_swapcase(input_string))