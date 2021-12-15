# Griffin Stepler, CIS 345, iCourse, PE2
import os
import random

# containers
operators = ('+', '-', '*', '/')
correct = list()

# variables
answer = 0.0
pointsEarned = 0
pointsTotal = 0
runApp = 'y'

# math trainer loop
while runApp == 'y':
    os.system('cls')
    # creating equation
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    sign = random.choice(operators)
    # incrementing total points
    pointsTotal += 1

    # calculating answer
    if sign == '+':
        answer = number1 + number2
    elif sign == '-':
        answer = number1 - number2
    elif sign == '*':
        answer = number1 * number2
    else:
        answer = number1 / number2
        answer = round(answer, 3)

    # displaying application title
    print(f'\n{"### Math Trainer ###": ^30}')
    # displaying problem
    userAnswer = input(f'Problem {pointsTotal}: {number1} {sign} {number2} = ')

    # checking if correct or incorrect
    if userAnswer == str(answer):
        pointsEarned += 1
        correct.append(userAnswer)

    # printing answer and points information
    print(f'Answer: {answer}')
    average = (pointsEarned / pointsTotal) * 100
    print(f'\nPoints Earned: {pointsEarned} out of {pointsTotal} \tAverage: {average: .2f}%')

    runApp = input('\nDo you want another question (y/n)? ').casefold()
    # end of while loop

# printing results
os.system('cls')
print(f'\nYou scored {pointsEarned} of {pointsTotal} and got the following right:')
for i in correct:
    print(i)

# end of application
