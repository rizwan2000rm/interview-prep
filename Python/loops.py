# LOOPS IN PYTHON

# ! WHILE LOOP
print("--- WHILE LOOP ---")
count = 0
while (count < 3):
    count = count + 1
    print("Hello Geek")
print()

#! combining else with while
print("--- WHILE LOOP with else ---")
count = 0
while (count < 3):
    count = count + 1
    print("Hello Geek")
else:
    print("In Else Block")
print()

#! FOR LOOP
print("--- FOR LOOP ---")
n = 4
for i in range(0, n):
    print(i)
print()

#! FOR LOOP with else
print("--- FOR LOOP with else ---")
list = ["geeks", "for", "geeks"]
for index in range(len(list)):
    print(list[index])
else:
    print("Inside Else Block")

# Python program to illustrate
# Iterating over a list
print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)
print()

# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)
print()

# Iterating over a String
print("\nString Iteration")
s = "Geeks"
for i in s:
    print(i)
print()

# Iterating over dictionary
print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("%s  %d" % (i, d[i]))
print()

#! NESTED LOOPS
print("--- NESTED LOOPS ---")
for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()
