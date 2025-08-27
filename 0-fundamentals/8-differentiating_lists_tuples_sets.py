# Lists
servers = ["web01", "db01", "web01"]
# Ordered: respects the insertion order
# Mutable: items can be added, removed or modified
# Allow duplicate items: equal numbers, strings or objects can belong to the same list

# Tuples
redis_cfg = ('10.0.5.1', 6379)
# Ordered: respects the insertion order
# Immutable: after creation, cannot be modified
# Allows duplicate items: equal numbers, strings or objects can belong to the same tuple

# Sets
allowed_ports = {22, 80, 443}
# Unordered: contents may be returned out of order
# Mutable: items can be added, removed or modified
# Does not allow duplicates: equal items will be dropped