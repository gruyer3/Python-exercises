# Strings are ordered, immutable sequences of characters.
# Use single or double quotes consistently; triple quotes for multi-line strings or docstrings.
example_str = "This is an example of double quoted string."
example_str2 = 'This is an example of single quoted string.'
# Both examples provides the same result:
print (example_str)
print (example_str2)
# Strings can also be defined in triple-line strings
example_command = """
Not indented line
    Indented line
"""
print(example_command)

# f-strings allow extended formatting, for example:
example_division = 24 / 7
print (f"Result: {example_division}")
# f-strings can also be used directly, like below:
print (f"Result: {24 / 7}")
# Both examples provides the same results.

# strip() method removes any leading and trailing whitespaces
example_string = "     This is a string example.     "
# strip removes all whitespaces
print (example_string.strip())
# lstrip removes whitespaces at the beginning of the string
print (example_string.lstrip())
# rstrip removes whitespaces at the end of the string
print (example_string.rstrip())

# upper() method prints whole string in uppercase
print (example_string.upper())
# lower() method prints whole string in lowercase
print (example_string.lower())

# startswith() method returns True if the string starts with the specified value
example_file = "filename.yaml"
print (example_file.startswith("file"))
# endswith() method works the same way, but if the string ends with the specified value
print (example_file.endswith("yaml"))

# We can split a string into a list where each word is a list item
path = "/usr/local/bin"
print (path.split("/"))
# or join all items in a tuple into a string, using specified character as operator
path_items = path.split("/")
print ("#".join(path_items))

# strings can also be concatenated, like below:
print (path + "/python")
# we can access individual characters in our string by using square brackets:
print (path[2])
# Python counts from 0, this is why character [2] in string "/usr/local/bin" is "s" and not "u"

# It is possible to extract characters between specified range:
print (path[3:11])
# If we provide only the first character, print() result will be ranged from the specified character to the end of the string.
print (path[3:])
# Or the other way around:
print (path[:11])

# len() function counts the number of characters in a string:
print (len(path))