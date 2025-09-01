# loops are main way to repeat actions
# for loops (for iterating over known sequences)
# while loops (for repeating as long as condition is True)
# these are essential for automating repetitive tasks such as processing lists, retrying operations or polling for status changes

# for loop: iterates through each item in a known sequence (list, tuple, string, dictionary items, range, file lines)
# best when you know the items to process

servers = ["web01", "web02", "web03"]
for server in servers:
    print ("Pinging server:", server)

for char in "SUCCESS":
    print (char)

for index in range(10):
    print ("Pinging server:", index)

# while loop: repeats as long as the condition remains True
# best when the number of repetitions isn't known beforehand, but a stopping condition is

connection_attempt = 0
max_attempts = 5
connected = False

while not connected and connection_attempt < max_attempts:
    print (f"Attempting to reach server: {connection_attempt + 1}")
    connection_attempt += 1

if not connected:
    print ("Failed to connect after maximum attempts.")

