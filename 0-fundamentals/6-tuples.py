# Tuples are ordered, immutable sequences defined with parentheses. Once created, their contents cannot be changed.
# Items maintain their positions, they're useful for fixed records like coordinates, version numbers or as dictionary keys.
host_port = ("192.168.1.16", "127.0.0.1", 3000)
rgb_red = (255, 0, 0)
print (type(host_port))
# When creating single value tuple, add comma at the end of it, otherwise it will be recognized as one of standard data types
single_value_tuple = ("the-only-value",)
print (type(single_value_tuple))

# Tuples can be sliced the same way as lists
print (rgb_red[-2:])

# Simple exercise
# 1. Create a tuple called service_endpoint with hostname and port values
# 2. Print the hostname and port
# 3. Attempt to modify an element (commented out to avoid error)
service_endpoint = ("srv-01.dev.local", 80)
print (f"Hostname: {service_endpoint[0]}")
print (f"Port: {service_endpoint[1]}")
# service_endpoint[1] = 443