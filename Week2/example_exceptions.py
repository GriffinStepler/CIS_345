# Exceptions

# ValueError - raised when a value cannot be parsed
x = float('a')

# TypeError - using the wrong data type for a function
x = int((1, 2))

# StopIteration
number = (n for n in range(0))
# for n in number:  # will handle it for you
next(number)  # causes StopIteration because there is nothing present in the data structure

# NameError - undefined variable or out of scope
print(students)

# IndexError - the list index is out of range of the list
data = [0, 1, 2]
print(data[3]) 
