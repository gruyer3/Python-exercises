# creating large lists for loops is memory-intensive
# range() stores only start, stop and step values, not all numbers
# numbers are generated one at a time during iteration, reducing memory usage
# ideal for loops needing a fixed number of iterations without large allocations
numbers_list = list(range(1_000_000))
numbers_range = range(1_000_000)
# prints all the numbers within a range as a list
print(numbers_list[:20])
# prints the range object
print(numbers_range[:20])
# prints numbers between 0 - 19
for number in numbers_range[:20]:
    print(number)

# inspect differences in memory used to store the objects
import sys

list_mb = sys.getsizeof(numbers_list) / (1024**2)
print(list_mb)

range_mb = sys.getsizeof(numbers_range) / (1024**2)
print(range_mb)

print(f"List uses {(list_mb / range_mb):.2f} more memory!")
# the difference will increase with more list objects
# size of memory used by range stays pretty much the same as it only stores start, stop and step values


# range(stop): iterate from 0 up to (but not including) stop
for i in range(5):
    print(f"Retry #{i}")
# range(start, stop): iterate from start up to stop
for year in range(2020,2024):
    print(f"Processing logs for {year}")
# range(start, stop, step): iterate with a custom step increment
for server_id in range(10, 30, 5):
    print(f"Checking server {server_id}")