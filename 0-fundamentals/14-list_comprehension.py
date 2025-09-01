# simple for loops to create lists can be verbose
# we can leverage list comprehensions to define the list contents directly within square brackets, obtaining a more compact syntax

# example: double items using a for loop
old_items = [1, 2, 3, 4]
doubled_items = []

for item in old_items:
    doubled_items.append(item * 2)
print (doubled_items)

# example: double items using list comprehension
doubled_items_with_comprehension = [item * 2 for item in old_items]
print (doubled_items_with_comprehension)

# another example
servers = ["web", "db", "backend"]
uppercase_servers = [server.upper() for server in servers]
print (uppercase_servers)