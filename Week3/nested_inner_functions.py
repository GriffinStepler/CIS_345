# Python allows you to define a function within a function
def outer(msg):
    """outer function"""
    text = 'Outer'
    # inner() only exists within outer(); it cannot be called from outside the outer() function
    def inner():
        print(f'{text} {msg}')
    return inner


x = outer('function')
x()  # inner(): text - 'Outer'   msg - 'function'
s = outer('space')
s()
l = outer('Layer')
l()
