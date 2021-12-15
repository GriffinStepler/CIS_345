def welcome():
    """This is the welcome function docstring"""
    return f'{"Welcome":*^20}'


def display(func):
    print(func())  # print(welcome()) --> print(f'{"Welcome":*^20}')
                   # this allows us to treat a function like an object, assigning its function to a


x = welcome
# print(x())
display(x)  # display(welcome)
# functions can be treated like objects: 
print(x.__name__)  # displays the name of the function that is running
print(x.__doc__)  # displays the docstring
print(x.__module__)  # displays the module you're executing the function from
