# Griffin Stepler, CIS345, iCourse, PE3
# os allows us to clear the screen in a actual console or terminal
import os
# TODO x Part 2: Add imports for json
import json
# end of Add imports for json

# TODO x Part 2:  Read customers data file into accounts
''' use the open command to open the file
# read the file and load the data structure in using json.loads()
# close the file when done
# Read File without using 'with' keyword
# Replace the below test data and assign accounts data from file
'''
fileHandle = open('customers.json')
accounts = json.load(fileHandle)
fileHandle.close()
# end Read customers data file into accounts

# TODO x Part 1: Create data structure use dictionary
# Test your dictionary in part by initializing with test data
# key = pin, value = account data dictionary
# accounts = {'9999': {'Name': 'John Doe', 'C': 1.00, 'S': 25.50}}
# end of Create a data structure use dictionary - commented out to prevent overwrite
# following json load

# FIXME x Part 1: Replace names with the data structure above
# comment 2 lines below, but rename account to accounts first
# accounts = 1000.00
# pin = '9999'
# end of Replace names with the data structure above

# Allow 3 invalid pin entries
tries = 1
maxTries = 3

while tries <= maxTries:
    # Print bank title and menu
    print(f'{"Cactus Bank":^30}\n')
    selection = input('Enter pin or x to exit application: ').casefold()

    # determine exit, pin not found, or correct pin found
    if selection == 'x':
        break
    # FIXME x Part 1: Verify entered pin in selection is a key in accounts
    elif selection not in accounts.keys():
        # end of Verify entered pin in selection is a key in accounts
        # clear screen - cls for windows and clear for linux or os x
        os.system('cls')

        print(f'Invalid pin. Attempt {tries} of {maxTries}. Please Try again')
        if tries == maxTries:
            print('Locked out!  Exiting program')
        # increment tries
        tries += 1
    else:
        # Upgrade: successful pin entry. reset tries and save pin
        tries = 1
        pin = selection

        # clear screen
        os.system('cls')

        # TODO x Part 1: Welcome customer
        # Display Welcome <Customer Name>
        # accounts[pin] holds a dictionary where 'Name' is the key
        # to the customer's name value
        print(f'Welcome {accounts[pin]["Name"]}')
        # end of Welcome customer

        # TODO x Part 1: Add prompt for Checking or Savings
        # Entry must be C or S to use as a key for the account balances
        # Use a loop and exception handling to ensure input is good
        # reuse selection name to store input to avoid scope issues
        while True:
            try:
                selection = input('Enter C for Checking or S for Savings: ').upper()
                if selection != 'C' and selection != 'S':
                    raise ValueError('Incorrect selection. Must enter C or S')
            except ValueError as ex:
                print(ex)
            else:
                os.system('cls')
                print(f'Opening {selection} Account...\n')
                break
        # end of Add prompt for Checking or Savings

        # Upgrade: Removed slicing and w/d entry - New Instructions
        print('Transaction instructions:')
        print(' - Withdrawal enter a negative dollar amount: -20.00.')
        print(' - Deposit enter a positive dollar amount: 10.50')

        # Upgrade: removed for loop only 1 transaction per pin input

        # FIXME x Part 1: All references to account need to be fixed
        # accounts is the new dictionary that needs to be indexed
        # using the entered pin and the selection account type
        # FIXME x Part 2: Modify formatting to include commas for thousands
        print(f'\nBalance:  ${accounts[pin][selection]: ,.2f}')

        # TODO x Part 1: Add exception handling for user entry of amount
        # Good input - convert to float and store in amount
        # Exception - Print Bad Amount and set amount to zero
        # FIXME x Part 2: Catch appropriate exceptions not Exception and
        # print better error message details using exception object
        try:
            amount = float(input(f'Enter transaction amount: '))
        except ValueError as ex:
            print(f'Invalid value: {ex}')
            amount = 0
        except TypeError as ex:
            print(f'Please input a numeric type: {ex}')
            amount = 0
        # end Add exception handling for user entry of amount
        # end Catch appropriate exceptions not Exception and
        # print better error message details using exception object

        # Upgrade: Verify enough funds in account
        # FIXME x Part 1: All references to account need to be fixed
        # add indices for pin and selection holding account type
        if (amount + accounts[pin][selection]) >= 0:
            # FIXME x Part 2: round() new account balance to 2 decimal places
            # Do this step last after running your program.
            accounts[pin][selection] = round((accounts[pin][selection] + amount), 2)
            # end round() new account balance to 2 decimal places
            # FIXME x Part 2: Modify formatting to add commas for thousands
            print(f'Transaction complete. New balance is {accounts[pin][selection]: ,.2f}')
            # end Modify formatting to add commas for thousands
        else:
            print('Insufficient Funds. Transaction Cancelled.')
        # end of All references to account need to be fixed

# end of application loop

print('\n\nSaving data...')
# TODO Part 2: Write accounts data structure to file
# We can write accounts to our data file here because
# this is after we exit our application loop when
# the user typed x to exit.
with open('customers.json', 'w') as fileHandle:
    json.dump(accounts, fileHandle)
# end Write accounts data structure to file

print('\nData Saved.\nExiting...')
