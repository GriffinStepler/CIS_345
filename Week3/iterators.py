s = {1, 2, 3}
l = [4, 5, 6]
t = (7, 8, 9)

print(s)
iterator = iter(s)
print(type(iterator))
for value in s:  # for loop does the same thing as iter(s) + next(iterator)
    print(value)

"""
print(next(iterator))
print(next(iterator))
print(next(iterator))
iterator = iter(l)
print(next(iterator))
print(next(iterator))
print(next(iterator))
iterator = iter(t)
print(next(iterator))
print(next(iterator))
print(next(iterator))
"""
