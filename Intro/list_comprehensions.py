# comprehensions - list uses [] and {} is a set or dictionary comprehension
data1 = {'a': 1, 'b': 2, 'c': 3}
keys = {x for x in data1}
values = {x for x in data1.values()}
items = {k: v for k, v in data1.items()}
# for k in data1:
#     keys.append(k)

print(keys)
print(values)
print(items)

numbers = [x for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]
odds = [x for x in range(10) if x % 2 != 0]
print(numbers)
print(evens)
print(odds)

cubes = [x ** 3 for x in range(10)]
print(cubes)

values = [1.0, 1.4, 2.56, 3.0, 4.0, 5.1]
integers = [i for i in values if i.is_integer()]
print(integers)

entries = ['1', '3', '5', '1.1.1', 'dog', '1-1']
nums = [int(x) for x in entries if x.isdecimal()]
print(nums)

word = 'battle'
letters = {x: x.upper() for x in word}
print(letters)

# what about comparing values to each other
# compare all combinations without duplicates
data = '1234'
combos = [(data[a], data[b])
          for a in range(len(data)) for b in range(a, len(data))]
print(combos)
