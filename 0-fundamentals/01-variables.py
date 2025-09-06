# VARIABLES: Naming values

# Use the equal sign (=) to label values. Example:
config_path = "/etc/app.conf"

# Naming must start with a letter or underscore (_) and can contain letters, numbers and underscores.
# Use snake_case for readability, for example:
max_retries = 3

# Store data like file paths, server counts, status messages, API keys, configurations.
# Python uses dynamic typing, which means we don't need to explicitly declare the variable type.
# We can assign values with different types to the same variable, but it's not recommended.

# item = 101 
# print(type(item))
# <class 'int'>

# Don't do that! Don't assign a value of a different type to the same variable!
# item = "Code 101"
# print(type(item))
# <class 'str'>

