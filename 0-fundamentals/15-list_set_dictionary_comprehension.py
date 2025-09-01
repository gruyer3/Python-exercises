# filtering with if in comprehension
# purpose: include only items meeting a condition
# the condition filters items before expression is evaluated
numbers = [1, 5, 6, 10, 2, 15]
even_numbers = [num for num in numbers if num % 2 == 0]
print (even_numbers)

# set comprehension uses {} and produces unique items
# dictionary comprehension uses {key: value ...}
# both evaluated eagerly like list comprehensions
numbers = [1, 2, 3, 4, 2, 1, 3]
unique_squares = {x * x for x in numbers}
print (unique_squares)

servers = ["web", "backend"]
server_ips = {server: f"192.168.1.{i}" for i, server in enumerate(servers, 10)}
print (server_ips)

# conditional expression (ternary operator)
# purpose: apply different expressions based on a condition within the comprehension
# places the ternary before the for clause
numbers = [1, 5, 6, 10, 2, 15]
categories = ["PASS" if num >= 8 else "FAIL" for num in numbers if num % 2 == 0] 
print (categories)