list = []

print("======.append()======\n")
list.append("Append Me")
print(list)
print()

print("======.extend()======\n")
iterable = ["apple", "beans"]
list.extend(iterable)
print(list)
print()

print("======.insert()======\n")
list.insert(0, "first")
print(list)
print()

print("======.remove()======\n")
# raises a ValueError if there is no such item
list.remove("Append Me")
print(list)
print()

print("======.pop()======\n")
# removes and returns the last item in the list
print(list.pop())
# removes and returns the item
print(list.pop(0))
print(list)
print()

print("======.clear()======\n")
# Remove all items from the list
list.clear()
print(list)
print()

print("======.count()======\n")
iterable2 = ["Count Me", "Count Me"]
list.extend(iterable2)
print(list.count("Count Me"))
print()

print("======.sort()======\n")
unsortedList = [1,63,-35,145,-230]
unsortedList.sort()
print(unsortedList)
unsortedList.sort(reverse=True) # list.reverse()
print(unsortedList)
print()

print("======.copy()======\n")
print(list.copy()) # Equivalent to a[:]  
print()
