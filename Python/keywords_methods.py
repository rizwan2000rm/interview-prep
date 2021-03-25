# len()
print("============ len() ============")
list = [1, 2, 3, 4, 5]
print(len(list))
print()

# iter()
print("============ iter() ============")
tuple = ("apple", "banana", "cherry")
iterableObj = iter(tuple)
print(next(iterableObj))
print(next(iterableObj))
print(next(iterableObj))
print()

# in
print("============ in ============")
for x in tuple:
    print(x)
print()

# del
print("============ del x ============")
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]
print(a)
print()
