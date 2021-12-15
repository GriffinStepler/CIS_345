# Griffin Stepler, CIS345, iCourse, PE6
import random
import statistics

courses = []


class Course:
    """ Course class """

    dept = 'CIS'

    # mutable argument trap present in init
    def __init__(self, num='', grades=dict()):
        """ init method for Course class, class number, name, and grades """
        self._number = num
        self._name = self.dept + num
        self.grades = grades

    @property
    def name(self):
        return self._name

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, num):
        self._number = num
        self._name = self._name[:2] + num

    @name.setter
    def name(self, new):
        self._name = new.upper()
        self._name = self._name + self._number[-3:]

    @classmethod
    def change_department(cls, dept):
        """ Class method to modify variable dept """
        cls.dept = dept

    def display_class_average(self):
        for k, v in self.grades.items():
            avg = statistics.mean(v)
            print(f'{k} avg is {avg:.1f} - {v}')


# main program logic
print('Entering course information...')

while True:
    course_num = input(f'Enter course number: {Course.dept}')
    new_course = Course(course_num)

    new_course.grades['Exam'] = [random.randint(1, 100),
                                 random.randint(1, 100),
                                 random.randint(1, 100)]
    new_course.grades['Quiz'] = [random.randint(1, 100),
                                 random.randint(1, 100),
                                 random.randint(1, 100)]
    new_course.grades['Assignment'] = [random.randint(1, 100),
                                       random.randint(1, 100),
                                       random.randint(1, 100)]

    courses.append(new_course)

    if input('\nAdd another course (Y/N)? ').casefold() == 'n':
        break

    department = input('Enter a three letter department name: ').upper()
    Course.change_department(department)

print('\nPrinting Courses...')
for course in courses:
    print()
    print(course.name)
    print(course.display_class_average())
