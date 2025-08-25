# Lists are ordered, mutable sequences defined with square brackets.
# Items maintain their position within a list what makes them ideal for storing sequences where order matters and contents change.
fruits = ["apples", "bananas", "blueberries", "dragonfruit"]
print (fruits)

# We can access single elements within a list using following syntax:
print (fruits [0])
# We can also use negative indices for the last item:
print (fruits [-1])

# Similar to strings, lists can be sliced:
print (fruits [0:2]) # will print only elements at indexes 0 and 1
print (fruits [:2]) # this line will have the same result as the one above
print (fruits [-2:]) # will print only the second to last and last elements
# Slicing does not alter the original list
print (fruits)

# Lists can contain different data types, for example:
example_list = ["string", 5, 2.2, True]
for item in example_list:
    print(type(item))

