# Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.
def custom_isupper(string):
    for char in string:
        if "a" <= char <= "z":
            return False
    return True if string else False

input_string = "HELLO WORLD"
output = custom_isupper(input_string)
print("Original string:", repr(input_string))
print("Is uppercase:", output)