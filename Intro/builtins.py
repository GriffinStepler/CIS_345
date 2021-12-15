# range(start=0, stop, step=1)
# step is increment/decrement value used
print(range(10))  # prints a range object as a list
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(10):
    print(i)

print('')

for i in range(1, 11, 2):
    print(i)

print('')

for i in range(20, 0, -5):
    print(i)
