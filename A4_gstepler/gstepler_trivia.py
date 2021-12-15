# Griffin Stepler, CIS345, iCourse, A4
import difflib
from functools import wraps


def question_decorator(func):
    """
    Decorator: creates a generator object that is used by wrapper function
    to wrap the input function
    """
    number = func()

    @wraps(func)
    def wrapper(*args, **kwargs):  # why are these arguments present? get_questions isn't decorated
        """Wrapper: formats f-string with number and movie character"""
        return f'Question {next(number)} {character}'

    return wrapper


@question_decorator
def question_number():
    """Generator: yields numbers from 1 to infinity"""
    number = 1
    while True:
        yield number
        number += 1


def get_questions(path):
    """
    Generator: yields lines from file (path = argument)
    Lines are stripped of excess whitespace
    """
    with open(path) as fp:
        for line in fp:
            output = line.strip()
            yield output


def grade_question(u_answer, r_answer):
    """
    Compares string arguments:
    returns 1 if >= 70% match, otherwise returns 0
    """
    # string.casefold() is optional here, but I feel capitalization is overrated
    ratio = difflib.SequenceMatcher(None, u_answer.casefold(), r_answer.casefold()).ratio()
    if ratio > 0.7:
        return 1
    else:
        return 0


# Beginning of program logic
point_total = 0
print(f'{"Movie Trivia":*^30}')
print('\nYou will be given a character. Respond with their movie:')

# variables used to display score at the end
counter = 0
score = 0

# create generator object to iterate line by line in questions.txt
question_getter = get_questions('questions.txt')
# measure the line length of the opened file, acts as LCV for line 69 while loop
line_length = len(open('questions.txt').readlines())

while counter < line_length:
    read_line = next(question_getter)
    split_line = read_line.split(',')
    character = split_line[0]
    input_answer = input(f'{question_number()}: ')
    score += grade_question(input_answer, split_line[1])
    counter += 1

print(f'\nYou scored {score} out of {counter} questions')
# end of program logic
