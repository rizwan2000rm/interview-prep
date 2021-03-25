from math import pi
# [(expression) (for loop)]

print("============ List Comprehensions ============")
print()

# squares = []
# for x in range(10):
# squares.append(x**2)
squares = [x**2 for x in range(10)]
print(squares)
print()

# combs = []
# for x in [1,2,3]:
# for y in [3,1,4]:
# if x != y:
# combs.append((x, y))
combinations = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(combinations)
print()

roundedPI = [str(round(pi, i)) for i in range(1, 6)]
print(roundedPI)
print()

print("============ Nested List Comprehensions ============")
print()

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# The following list comprehension will transpose rows and columns:
transposeMatrix = [[row[i] for row in matrix] for i in range(4)]
print(transposeMatrix)
print()
