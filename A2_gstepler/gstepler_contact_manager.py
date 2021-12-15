# Griffin Stepler, CIS345, iCourse, A2
import os
from difflib import get_close_matches
import json

contacts = {}
file = 'contacts.json'
lcv = ''

# load contact information from contacts.json
try:
    with open(file) as fp:
        print('Loading Contacts...')
        contacts = json.load(fp)
        print(f'{"Name":<15} | {"Number":>15}')

        for k, v in contacts.items():
            print(f'{k:<15} - {v:>15}')

        input('Data Loaded. Press ENTER to continue...')

except FileNotFoundError as error:
    print(f'Missing File: {error}')

except IOError as error:
    print(f'IOError: {error}')

while lcv != 'e':
    # clear screen, display heading
    os.system('cls')
    print(f'{"Manage Contacts":^30}')

    # search functionality
    name = input('Enter a name to search for: ')
    search_results = get_close_matches(name, contacts, n=5, cutoff=0.5)
    # cases: contact found, multiple contacts found, no contacts found
    if name in contacts:
        print('Contact Found')
        print(f'{name:<15} - {contacts[name]:>15}')
    elif len(search_results) > 1:
        print('Contacts Found')
        for result in search_results:
            print(f'{result:<15} - {contacts[result]:>15}')
        name = input('Type the name you meant from the list, or a new name to add: ')
    else:
        print('Contact Not Found')
        print('Add New Contact')
    # end of search functionality

    # add or edit phone number
    number = input(f"Enter {name}'s phone number (###)###-#### or enter for no change: ")
    if len(number) == 13:
        contacts[name] = number

    os.system('cls')
    lcv = input('Press E to exit, or ENTER to continue: ').casefold()
    # end of while loop

# save contact information to contacts.json
try:
    with open(file, 'w') as fp:
        print('Saving Changes...')
        json.dump(contacts, fp)
        print('Changes Saved')
except FileNotFoundError as error:
    print(f'Missing File: {error}')
except IOError as error:
    print(f'IO Error: {error}')
