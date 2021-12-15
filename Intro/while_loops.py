import os

# prompt user for answer until correct answer is entered
answer = 'sparky'
entry = ''
points = 10

while True:
    entry = input('Who is the ASU mascot? ').casefold()
    os.system('cls')

    if entry == answer:
        break
    elif entry == 'sundevil':
        print('Close. Enter a more formal name!')
        continue
    else:
        print('Incorrect answer, try again!')
        points -= 1

print(f'That is the correct answer! Earned {points} pts')
