def decorator(func):
    """outer function"""
    def wrapper(*args, **kwargs):  # using *args, **kwargs allows you to pass a function with ANY number of parameters
        print('wrapper start')
        func(*args, **kwargs)
        print('wrapper end')
    return wrapper


@decorator  # any time you call title1(), Python executes decorator(title1)
def title1():
    print(f"{'Welcome':*^30}")


@decorator
def title2(msg, name=''):
    print(f"{msg:*^30}")


# display_title1 = decorator(title1)  # pass the reference to title1
# print(display_title1.__name__)
# display_title1()  # the parentheses execute the function; no parentheses references it

title1()  # this now executes the same as line 14 + 16
title2('My Bank')   # title2 is decorated --> holds reference to wrapper(), which does not accept arguments
                    # to pass an argument, wrapper() needs to define a parameter
