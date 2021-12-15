# CRUD
# Create or Declare a dictionary
data1 = {'key': 'value', 'a': 1, 'b': 2, 'c': 3}
data2 = {0: 30, 1:29, 2: 21}
data3 = {}  # or dict()
'''
print(data1)
print(data2)
print(data3)
'''

# Create or Add keys and values to a dictionary
data3['ID'] = 100
data3['Name'] = 'Lilly'
data3['GPA'] = 3.72
data2[3] = 30
'''
print(data3)
print(data2)
'''

# Read or Get values form a dictionary
v = data3.get('GPA')
'''
print(v)
print(data3['Name'])
print(data1['a'])
print(data2[1])
'''

# Update values in a dictionary
'''
data3['Name'] = 'Jeff'
data2[2] = 30
# print(data3, data2)
print(data3, data1)
data3.update(Name = 'Sue')
# data2.update(0 = 1)  # keys should be strings for the update method
data1.update(a = 4, b = 5, c =6)
print(data3, data1)
'''

# Delete key or key/value pair
'''
print(data1)
del(data1['key'])
print(data1.popitem())
print(data1)
'''

# delete an old key and add a new one (renaming a key)
data1['A'] = data1.pop('a')  # this line 'pops' key 'a' and assigns value 1 to 'A'
# print(data1)  # key value pairs are always added to the end


# using for loop to go through a dictionary

for key in data3:
    print(key)

for values in data3.values():
    print(values)


for k, v in data3.items():
    print(k, v)

dictionaries = [data1, data2, data3]
for d in dictionaries:
    for value in d.values():
        print(f'{value: <6}', end='')
    print()
