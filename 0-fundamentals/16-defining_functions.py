# use def name(parameters): followed by an indented block.
# optional """docstring""" explains purpose, parameters and return value
def greet_user(name):
    """Greets the user by name
    Args:
        name(str): The user to greet

    Returns:
        None: Function does not return any value
    """
    print (f"Hello, {name}!")

greet_user("Alice")

# calling a function, invoked vie name(args) and controls jump into the function body and optionally returns a value back
import random
def random_number(min_val, max_val):
    """Generates an int between min_val and max_val
    Args:
        min_val(int): The lower boundary of the interval
        max_val(int): The upper boundary of the interval
    
    Returns:
        int: The generated random number
    """
    return random.randint(min_val, max_val)

generated_number = random_number(0, 10)
print (f"Generated number: {generated_number}")