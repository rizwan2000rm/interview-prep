# Note: to create an empty set you have to use set(), not {}

print("============ set ============")
print()

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) # show that duplicates have been removed

print('orange' in basket)

# set comprehensions are also supported
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)