fruits = ["apples", "bananas", "blueberries", "dragonfruit"]

# This method can remove list elements
fruits.remove("dragonfruit")
print(fruits)

# To add element at the end of the list, use this method:
fruits.append("strawberries")
print(fruits)

# To add element to the specified position, use following method:
fruits.insert(1, "watermelon")
print (fruits)

# To remove element at the specified position, use:
fruits.pop(2)
print (fruits)
# When the number is not specified, the .pop() method removes the last element of the list
fruits.pop()
print (fruits)