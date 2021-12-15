
# for each loops - used if you know number of iterations
for i in range(5):
    print(i)

names = ['Al', 'Sue', 'Liv']
for name in names:
    print(f'Hello {name}')

# for loop used with dictionaries
data = {'a':1, 'b':2, 'c':3}
for key in data.keys():  # the keys() (data.keys()) method returns only the keys in a dictionary; not required
    print(key)
for values in data.values():
    print(values)
for k, v in data.items():  # items method returns both the key, and the value, in correct order
    print(k, v)

# while loops - used if the body can be skipped (pre-test)
answer = 'water'
entry = str()

while entry != answer:
    entry = input('What is H2O? ').casefold()

i = 0
while i < 10:
    i += 1
    if i == 5:
        continue  # skips printing 5
    print(i)
    if i == 8:
        break  # stops before printing 9
