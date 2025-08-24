# Numbers - int & float
# int = whole numbers
# float = numbers with decimals
int = 1024
print(type(int))
float = 2.137
print(type(float))

# Arithmetic operations
# +, -, *, /
print ("2 + 2 =", 2 + 2)
print ("4 - 1 =", 4 - 1)
print ("3 * 8 =", 3 * 8)
# / -> true division (float)
print ("8 / 4 =", 8 / 4)
# // -> floor division (int or float)
print ("8 // 4 =", 8 // 4)
# % -> modulo (reminder)
print ("48 % 13 =", 48 % 13)
# ** -> power
print ("3 ** 2 =", 3 ** 2)


# When comparing floats directly, we may run into precision issues:
print ("0.1 * 3 == 0.3:", 0.1 * 3 == 0.3)
# To tackle this, we can use the math.isclose() function:
import math
print ("math.isclose(0.1 * 3, 0.3):", math.isclose(0.1 * 3, 0.3))