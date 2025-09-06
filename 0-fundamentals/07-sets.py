# Sets are unordered, mutable, unique items only (duplicates removed)
# The items of a set must be immutable
# Use cases: membership testing, removing duplicates, set operations (union, intersection, difference)
unique_ports = set([80, 443, 22, 80, 8080, 443])
print (unique_ports)
# Sets can also be created using curly brackets
servers = {"web01", "web02"}
print (servers)

# To check membership in a set use:
print (22 in unique_ports) 
print (22 in servers)
# Result will provide a Boolean value

# To add an item to set, use:
unique_ports.add(3000)
print (unique_ports)

# To remove an item, use:
unique_ports.remove(80)
print (unique_ports)
# Trying to remove an item that doesn't exist will throw an error
# If you're not sure if the item exist within a set, use:
unique_ports.discard(80)
print (unique_ports)