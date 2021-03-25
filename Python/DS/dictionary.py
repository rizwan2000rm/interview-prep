# to create an empty set you have to use {}

print("============ dictionary ============")
print()

tel = {'jack': 4098, 'sape': 4139}

tel['guido'] = 4127
print(tel)

del tel['sape']
print(tel)

print(list(tel))

print(sorted(tel))

print('guido' in tel)

# dict comprehensions
d = {x: x**2 for x in (2, 4, 6)}
print(d)

# looping
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# To loop over two or more sequences at the same time,
# the entries can be paired with the zip() function
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
