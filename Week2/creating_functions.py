# methods are defined within a class
# functions are methods defined outside of a class
'''
def function(params,...):
    function body or code block


class MyClass:
    def method(params,...):
        method body or code block
'''


# function names should be snake_case
'''
def function_1():
    """
    This is a docstring: function documentation
    """
    print('function_1 was called')
    return None  # this line is implied; not necessary to write; this is why print(function_1) prints 'None'


def function_2(message, b, c):
    print(f'function_2, the message is {message} {b} {c}')


print(function_1())
function_2('Hello there', 1, 'h')
print(function_1.__doc__)
print()
print(type.__doc__)
'''


def max_number(a, b, c):  # this function has "required parameters"; each of them are required for the function to run
    max = a
    if b > max:
        max = b

    if c > max:
        max = c

    return max

# default parameters MUST be assigned to the right of nondefault parameters
def pos_number(a, b=0):  # this function has an "optional parameter"; b has a default parameter
    sign = 'zero'
    if a > b:
        sign = 'positive'

    if a < b:
        sign = 'negative'

    return sign


def calculate_tip(amount, tax, tip_percent=0.2):
    """
    Determines bill plus tax and tip.
    Optional: tip will default to 20%
    """
    total_plus_tip = (1 + tax + tip_percent) * amount
    return f'$ {total_plus_tip:_>6,.2f}'


# *args - variable arguments; you can input one, many, or none when calling the function
def total_up(*args):
    total = 0
    for val in args:
        total += val

    return total


# **kwargs - a dictionary built based on the variable arguments passed into the function
def x(**kwargs):
    print(kwargs)


# this function takes ANY number of arguments or keyword arguments
def y(*args, **kwargs):
    print(kwargs)


x(name='Chris', id=1, eye_color='blue')
print(total_up())
# print(total_up(3, 7, 5, 10, 5))
# print(calculate_tip(20, .1))
# print(calculate_tip(tip_percent=.2, amount=20, tax=.1))  # this returns the same answer; we specified parameters for each argument
