# Griffin Stepler, CIS345, iCourse, PE4
from gstepler_utilities import *


def divide(numerator, denominator):
    """
    returns a float answer of numerator / denominator
    """
    answer = 0
    try:
        answer = numerator / denominator
    except ZeroDivisionError as error:
        print(f"Error: {error}. Can't divide by zero.")
        return 0
    else:
        return answer


def average(*values):
    """
    returns float average after totaling all value and dividing by len(values)
    """
    print(what_type(values))
    total = 0

    for value in values:
        total += value

    return total / len(values)


# TODO: step through this function to understand self-recursion
def factorial(number):
    """
    Computes the factorial of any number passed.
    Factorial will multiply the number supplied by every value less than it
    until reaching 1
    """
    if number == 1:
        return 1

    return factorial(number - 1) * number


def employee_profile(**kwargs):
    """
    prints an employee profile using tabular format
    """
    print(what_type(kwargs))
    header('Profile')

    for k, v in kwargs.items():
        print(f'{k:<15} | {v:>15}')

    return None


if __name__ == "__main__":
    header('Divide Function')
    print(f'10 / 5 is: {divide(10, 5)}')
    print(f'10 / 0 is: {divide(10, 0)}')
    print()

    header('Average Function')
    print(f'Average of 1-10: {average(1, 2, 3, 4, 5, 6, 7, 8, 9, 10):.2f}')
    print()

    # the directions indicate to provide factorial() "with three arguments"...
    # I don't understand what this is implying. factorial() can only accept 1 argument,
    # unless the directions mean that it should receive 3 calls with different arguments?
    header('Factorial Function')
    print(f'Factorial 5! = {factorial(5)}')
    print()

    print('Call Employee Profile')
    employee_profile(Name='Michael Crow', Position='President', Status='Active', Salary='$1,351,903.72')
