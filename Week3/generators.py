# generator function uses yield in place of return
# adding one yield function turns it into a generator
'''
def count_down(start):
    c = start
    while c > 0:
        yield c  # if return was used, the next line would not run; yield results in it running
        c -= 1


counter = count_down(10)  # generator object
print(counter)
for n in counter:
    print(n)

counter = count_down(5)  # make sure you don't construct generator objects in a loop
for n in counter:
    print(n)
'''


def square_numbers(*nums):
    for n in nums:
        yield n * n


'''
squares = square_numbers(1, 2, 3, 4, 5, 6)
print('\nCall Square Numbers generator to yield one value at a time')
for n in squares:
    print(n)
'''

# List comprehension
squares = [n * n for n in range(1, 10)]
# Generator comprehension
squares = (n * n for n in range(1, 10))  # parentheses are a generator comprehension
print(squares)
for n in squares:
    print(f'{n} ', end='')
print()