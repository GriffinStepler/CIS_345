# Griffin Stepler, CIS 345, iCourse, A1 - Grade Calculator
import os

# declaration of dictionary and variable(s)
grades = {'Exercises': {'Pts Earned': 0.0, 'Total Pts': 160, 'Weight': .03, 'Grade': 0.0},
          'Assignments': {'Pts Earned': 0.0, 'Total Pts': 210, 'Weight': .1, 'Grade': 0.0},
          'Projects': {'Pts Earned': 0.0, 'Total Pts': 100, 'Weight': .17, 'Grade': 0.0},
          'Quizzes': {'Pts Earned': 0.0, 'Total Pts': 80, 'Weight': .25, 'Grade': 0.0},
          'Exams': {'Pts Earned': 0.0, 'Total Pts': 200, 'Weight': .36, 'Grade': 0.0},
          'Finals': {'Pts Earned': 0.0, 'Total Pts': 100, 'Weight': .09, 'Grade': 0.0}}
final_grade = 0.0

print('Add up all points earned for each grade category')
print('*(Do not add your lowest score in the 3 categories with a dropped score)*\n')
# get input for Points Earned value in each sub-dictionary
for key in grades:
    grades[key]['Pts Earned'] = float(input(f'Enter your total points for {key}: '))
    grades[key]['Grade'] = (grades[key]['Pts Earned'] / grades[key]['Total Pts']) * grades[key]['Weight']
os.system('cls')

# calculate final_grade by looping through dictionary and iterating final_grade66
for key in grades:
    final_grade += grades[key]['Grade']

print('Grade Information:\n')
print(f'{"Category": <15} | {"Pts Earned": ^10} | {"Total Pts": ^10} | {"Weight": ^10} | {"Grade": ^10} |')
print('-' * 69)
for key in grades:
    print(f'{key: <15} | {grades[key]["Pts Earned"]: >10} | {grades[key]["Total Pts"]: >10} | '
          f'{grades[key]["Weight"]: >10.0%} | {grades[key]["Grade"]: >10.2%} |')
print(f'\nFinal Grade: {final_grade: .2%}')
