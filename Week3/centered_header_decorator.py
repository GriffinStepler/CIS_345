from functools import wraps

def centered_header(func):
    """outer function"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        """wrapper function"""
        title = func(*args, **kwargs)
        print(f'{title:*^30}')
    return wrapper


@centered_header
def title1():
    """centered welcome message"""
    return 'Welcome'


@centered_header
def title2(msg):
    """centered variable message"""
    return f'{msg} Application'


title1()
title2('My Bank')
print(title1.__name__)
print(title2.__doc__)
print(title2.__name__)
print(title2.__doc__)
