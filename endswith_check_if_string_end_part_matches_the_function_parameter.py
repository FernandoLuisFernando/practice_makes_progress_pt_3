def custom_endswith(string, suffix):
    return string[-len(suffix):] == suffix if len(suffix) <= len(string) else False

input_string = "Hello, World!"
suffix = "World!"
print(custom_endswith(input_string, suffix))