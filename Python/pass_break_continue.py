# https://www.geeksforgeeks.org/break-continue-and-pass-in-python/

#! demonstrate break statement
s = 'geeksforgeeks'
# Using for loop
for letter in s:
    print(letter)
    # break the loop as soon it sees 'e'
    # or 's'
    if letter == 'e' or letter == 's':
        break

print("Out of for loop")
print()

#! demonstrate continue statement

# loop from 1 to 10
for i in range(1, 11):
    # If i is equals to 6,
    # continue to next iteration
    # without printing
    if i == 6:
        continue
    else:
        # otherwise print the value
        # of i
        print(i, end=" ")
print()

#! pass statement - pass statement simply does nothing
# pass statement in Python is used when a statement is required syntactically but you do not want any command or code to execute
s = "geeks"

# Empty loop
for i in s:
    # No error will be raised
    pass


def fun():
    # Empty function
    pass


# No error will be raised
fun()

# Pass statement
for i in s:
    if i == 'k':
        print('Pass executed')
        pass
    print(i)
