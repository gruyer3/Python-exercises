# Dictionaries are mutable, insertion-ordered collections of key-value pairs
# Keys must be unique and immutable, values can be of any type
my_dictionary = {
    'a': 1,
    'b': 2,
    'c': 3
}
print (my_dictionary)

# length function treats keys and values as one item
print (f"Length: {len(my_dictionary)}")

# keys, values and items
print (f"Keys: {my_dictionary.keys()}")
print (f"Values: {my_dictionary.values()}")
print (f"Items: {my_dictionary.items()}")
# items method returns tuples
for item in my_dictionary.items():
    print (type(item))

for key, value in my_dictionary.items():
    print (f"- {key}: {value}")

# membership test
print (f"is 'b' in my disctionary? {"b" in my_dictionary}")
print (f"is 'd' in my disctionary? {"d" in my_dictionary}")
# above comparsion happens at the key level
print (f"is 1 in my disctionary? {1 in my_dictionary}")
# to retrieve the values, use
print (f"is 1 in values of my_dictionary? {1 in set(my_dictionary.values())}")
# uniqueness is only required at the key level, we may have multiple same values

# accessing elements
print ("'b':", my_dictionary["b"])
print ("'b':", my_dictionary.get("b"))
# if the key is not present, we'll get None
print ("'e':", my_dictionary.get("e"))
# in case the key doesn't exist we may provide default value
print ("'e':", my_dictionary.get("e", -1))
# we're gonna get an error if we try to access non-existing key without get function
# print ("'e':", my_dictionary["e"])

# adding dictionary items
my_dictionary.setdefault("d", 4)
print (my_dictionary)

# remove item
removed = my_dictionary.pop("a")
print (removed) # returns the value
removed = my_dictionary.popitem() # removes the last dictionary item
print (removed)