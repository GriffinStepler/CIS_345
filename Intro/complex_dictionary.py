# complex dictionary example
students = {'lLee1': {'ID': 100, 'Name': 'Lilly', 'GPA': 3.72, 'Password': '123qwe'},
            'jLee2': {'ID': 101, 'Name': 'James', 'GPA': 3.34, 'Password': '432fds'}}

student_data = ('ID', 'Name', 'GPA', 'Password')

# prompt for username
user = input('Enter username: ')
if user in students:
    current_account = students.get(user)
    password = input('Enter password: ')
    if password == current_account['Password']:
        print(f'{"Label": <8} {"Data": >10}')
        for k, v in current_account.items():
            print(f'{k: <8} {v: >10}')
    else:
        print('Invalid password')
else:
    students[user] = dict()
    for data in student_data:
        students[user][data] = input(f'Enter {data}: ')  # dictionary[key][innerKey]

print('\n\n')
for k, v in students.items():
    print(k, v)


# if the user exists, verify password then print data, else add new student

