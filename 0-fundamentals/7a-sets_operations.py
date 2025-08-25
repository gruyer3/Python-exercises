# Sets must contain immutable type, so for example, creating a set of lists is not possible
# set_of_lists = set([[1,2],[3,4]]) # this line throws TypeError
# set_of_sets = {{1,2},{3,4}} # this line throws TypeError
set_of_tuples = {(1,2),(3,4)} # this line works since tuples are immutable

# We can also check if the tuple is present in the set of tuple
print ((1,2) in set_of_tuples)

# Set operations
developers = set(["alice", "bob", "charlie"])
admins = set (["alice", "david"])
print("alice" in developers)
print("alice" in admins)

print("Union:", developers.union(admins))
print("Intersection:", developers.intersection(admins))
print("Difference:", developers.difference(admins))
print("Difference:", admins.difference(developers))
# Same result can be achieved with different syntax as well
print("Union:", developers | admins)
print("Intersection:", developers & admins)
print("Difference:", developers - admins)
print("Difference:", admins - developers)