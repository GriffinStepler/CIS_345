
total_points = 100

# get data from user
user_entry = input(f'Enter score out of {total_points}: ')

if len(user_entry) > 0:
    # convert string to float
    earned_points = float(user_entry)

    # calculate grade percentage
    grade = earned_points / total_points

    # determine letter grade
    letter_grade = ''

    if grade >= .90:
        letter_grade = 'A'
    elif grade >= .80:
        letter_grade = 'B'
    elif grade >= .70:
        letter_grade = 'C'
    elif grade >= .60:
        letter_grade = 'D'
    else:
        letter_grade = 'E'

    print(f'Grade: {grade:.1%}')
    print(f'\tLetter Grade is {letter_grade}')
