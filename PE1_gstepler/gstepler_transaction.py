# Griffin Stepler, CIS 345, iCourse, PE1
import os

# create objects for test data
account = 1000.00  # float value for user accessible money
pin = '9999'       # string for user login pin
tries = 1          # int for pin attempts initiated
maxTries = 3       # limiting int for max pin attempts allowed

while tries <= maxTries:
    # print bank title and menu
    print(f'{"Cactus Bank": ^30}\n')

    # prompt user for input
    selection = input('Enter pin or x to exit application: ').casefold()

    # selection decision logic
    if selection == 'x':
        break
    elif selection != pin:
        # clear screen
        os.system('cls')

        # inform user of remaining tries
        print(f'Invalid pin. Attempt {tries} of {maxTries}. Please try again.')
        # test if any remaining tries; if none, exits
        if tries == maxTries:
            print('Locked out. Exiting program.')
        # increment tries
        tries += 1
    else:
        # clear screen
        os.system('cls')

        # user instructions
        print('Transaction instructions: ')
        print('Enter w for Withdrawal or d Deposit followed by dollar amount.')
        print('Example withdrawal of $10.50 you would enter w10.50')
        print('All dollar amounts must be positive')

        # for loop: prints account balance, gets and parses selection,
        for i in range(1, 5):
            print(f'\nBalance: ${account:.2f}')
            selection = input(f'Enter transaction {i}: ')
            transaction = selection[0:1]
            amount = float(selection[1:])

            print(f'Starting balance is {account:.2f}')
            if transaction == 'd' and amount >= 0:
                account += amount
                print(f'After Deposit new balance is {account:.2f}')
            elif transaction == 'w' and amount >= 0:
                account -= amount
                print(f'After Withdrawal, new balance is {account:.2f}')
            else:
                print('Invalid entry. Please try again.')
    # end of transaction loop
# end of application loop
