import os

'''
# String Formatting

age = 28
wallet = 50.75

# prompt user for name
name = input('Enter name: ')
input('Thanks for your name. Press ENTER to continue... ')

# clear screen and show results
os.system('cls')  # this is the cmd input you use to clear the screen, input as a string

# using Java style placeholder %type
print("Hi, %s \nAge: %i \tWallet: %.2f" % (name, age, wallet))

# using C# style placeholders {} and .format()
print("Hi, {} \nAge: {} \tWallet: {:.2f}".format(name, age, wallet))

# using an f string --> Python's best choice
# :<fill><align><spaces>.<decimalpoints><type>
    # alignment is either <left ^center >right
    # strings are default left, numbers default right
print(f'{name:*^30}')
print(f'{name:*<30}')
print(f'{wallet:_>10.2f}')
print(f"Hi {name} \nAge: {28} \tWallet: {wallet}")
'''

'''
# String Methods

name = input('Enter name: ')
p_id = input('Enter ID: ')

print(type(p_id))
print(id(p_id))
print(p_id)

p_id = p_id.zfill(5)  # zfill() fills leading zeroes to the specified total length, if longer, no zeroes added

print(type(p_id))
print(id(p_id))
print(p_id)
'''


data1 = '0123456789'
word1 = 'Sun Devils Rule'
space = '\t    Hi    \n'
comma = 'Kelly,Lee,008,3.2'
com = 'Kelly,Lee'

# String Splicing
# stringObject[start:end]
print(word1[0])  # slices allow retrieval of indexed string positions
print(word1[0:2])  # slices are inclusive on lower bound, exclusive on upper bound
print(word1[-4:])  # slices from the fourth to last index, to the end

# strip()
stripped_version = space.strip()  # Removes blanks from either side, including /t and /n
print(stripped_version)
print(data1)

# split()
new_data = comma.split(',')
print(new_data)

first, last = com.split(',')
print(first)
print(last)
