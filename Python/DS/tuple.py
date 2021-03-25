# Tuples are immutable
print("============ tuples ============")
print()

tuples = (12345, 54321, 'hello!')

print(tuples)

u = tuples, (1, 2, 3, 4, 5)
print(u)

# The statement t = 12345, 54321, 'hello!' is an example of tuple packing:
# the values 12345, 54321 and 'hello!'
# are packed together in a tuple. The reverse operation is also possible
x, y, z = tuples
print(x, y, z)
