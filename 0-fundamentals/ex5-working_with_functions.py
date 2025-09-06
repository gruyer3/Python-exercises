# define a function greet_users(names) that takes a list of user names and prints a personalized greeting for each
def greet_users(names):
    for name in names:
        print (f"Hello, {name}!")

greet_users(["Alice", "Bob", "Charlie"])

# define a function sum_even(numbers) that takes a list of integers and returs the sum of all even numbers
def sum_even(numbers):
    return sum(x for x in numbers if x % 2 ==0)

print(sum_even([1, 2, 3, 4, 5, 6]))

# define a function fibonacci(n) that returns a list of the first n Fibonacci numbers
def fibonacci(n):
    seq = [0, 1]
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

print(fibonacci(11))