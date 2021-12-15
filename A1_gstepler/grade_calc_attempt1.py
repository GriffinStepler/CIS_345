# Griffin Stepler, CIS 345, iCourse, A1 - Grade Calculator
import os

# declaration of variables, including dictionaries
points_earned = {'Exercises': 0, 'Assignments': 0, 'Projects': 0,
                 'Quizzes': 0, 'Exams': 0, 'Finals': 0}
points_possible = {'Exercises': 160, 'Assignments': 210, 'Projects': 100,
                   'Quizzes': 80, 'Exams': 200, 'Finals': 100}
weights = {'Exercises': .03, 'Assignments': .1, 'Projects': .17,
           'Quizzes': .25, 'Exams': .36, 'Finals': .09}
grade_per_category = {}
final_grade = 0.0

# user input for total points in each category
print('Add up all points earned for each grade topic')
print('(do not add your lowest score for the 3 topics with a dropped score)\n')
# prints "enter total points earned" prompt for each category
for key in points_earned:
    points_earned[key] = float(input(f'Enter your total points earned for {key}: '))
# creates whitespace, clear screen after inputting total points
print('\n\n')
os.system('cls')

# calculates weighted grade per category via comprehension
grade_per_category = {g: (points_earned[g] / points_possible[g]) * weights[g] for g in points_earned}
final_grade = sum(grade_per_category.values())

# prints out grade information heading and formatted table
print('Grade Information:\n')
print(f'{"Category": <15} | {"Pts Earned": ^10} | {"Total Pts": ^10} | {"Weight": ^10} | {"Grade": ^10} |')
print('-' * 70)
# loops through each dictionary to print each table line
for g in points_earned:
    print(f'{g: <15} | {points_earned[g]: >10} | {points_possible[g]: >10} | {weights[g]: >10.0%} | '
          f'{grade_per_category[g]: >10.2%} |')
print(f'\nFinal Grade: {final_grade: .2%}')

# end of program
