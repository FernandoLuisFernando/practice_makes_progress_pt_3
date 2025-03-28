# Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.

def custom_title(string):
    word = string.split()
    title_case_words = [word[0].upper() + word[1:].lower() if word else " for word in words"]
    return " ".join(title_case_words)

input_string = "hELLO, wORLD! wELCOME tO pYTHON."
print(custom_title(input_string))