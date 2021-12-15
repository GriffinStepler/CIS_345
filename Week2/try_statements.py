import sys


def function1(x):
    try:
        return int(x)
    # except ValueError as excp:
    #     print(excp)
    #     print(excp.args)   # shows arguments - parameters, variable names
    #     print(type(excp))  # prints data type exception that allows you to add an exception for that type of item
    # except TypeError as excp:
    #     print(excp)
    except (ValueError, TypeError) as excp:  # this catches two types of exceptions, though this lacks precision
        print(f'Error of value or type occurred: {excp}')
        return 1



print(function1('124'))
print(function1('poggers'))
print(function1(['test', 'list']))
