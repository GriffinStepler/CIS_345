stu_admitted = True
name = 'Clark Kent'
balance_due = 2925.48
passed_classes = 'CIS340'

# can you register
if stu_admitted:
    print(f'Registering {name} now: ')
    if balance_due > 0 or passed_classes != 'CIS340':
        print('You owe a balance or have not passed the prereq CIS340')
    else:
        print('Registered!')
else:
    print('Student not admitted')
