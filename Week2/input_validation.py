# Create your own exception that accepts an error message
class myException(Exception):  # inherit from Exception
    def __init__(self, msg):   # dunder/magic method; double underline
        self.msg = msg


# Validation loop using exception handling
selection = 0
validMenuSelections = [1, 2, 3]  # or vms = range(1,4)
print('Menu: \n1. A\n2. B\n3. C')

while True:
    try:
        # selection = int(input('Enter menu selection: '))
        selection = input('\nEnter menu selection: ')
        if selection.isnumeric():
            selection = int(selection)

        # can be in its own try statement, or left here
        if selection not in validMenuSelections:
            raise myException('Selection must be 1, 2, or 3. Try again.')
    except ValueError:
        print('Invalid selection. Try again.')
    except myException as excp:
        print(excp)
    else:
        print('Thanks for your valid menu selection!')
        break  # the finally block ALWAYS executes, even with this break statement
    finally:
        print('Processing...')

print(f'\nProcessing complete. You selected {selection}')
