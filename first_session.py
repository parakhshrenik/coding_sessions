# Lambda functions

x = lambda a : a + 10
print(x(5))

# Use cases of lambda functions:
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Syntax for filter: filter(function, iterable)
# Iterable in an object that one can iterate over.

filter(lambda x: x % 2 == 0, l1)



