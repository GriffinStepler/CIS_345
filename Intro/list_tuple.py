# lists are better arrays lmao
# lists are mutable data types; can be modified while holding the same memory address
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
blank_list = []
colors = ['green', 'red', 'tan']
colors[0] = 'dark green'  # this mutates the list
colors.insert(0, 'blue')  # inefficient; inserts at the beginning, but 1 by 1 increases indices
colors.append('yellow')   # append just adds to the end

removed = colors.pop(3)  # removes element from list, returns this element
print(removed)

for color in colors:
    print(f'{color} ', end='')

print('')
print(colors.count('blue'))  # prints the quantity of the arguments in the list


print('\n\nTuple Example:')
# tuples are immutable lists - items cannot be modified; they are static
values = (1, 2, 3, 4, 5, 6, 'cat')

print(values.count(1))
print(values.index('cat'))
print(type(values))


if 1 in values:
    print('1 is in values')

if 'blue' in colors:
    print('Blue is in colors')
