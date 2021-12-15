# Griffin Stepler, CIS345, iCourse, PE6
import random
import os

courses = []


class Course:
    # class variables
    semester = 'Fall 2025'

    def __init__(self, name='', categories=None):
        """Create a course object. self refers to the object"""
        self.section = random.randint(10000, 100000)
        self.name = name
        self.student_count = 0
        self.class_roster = []
        # Instance variable categories will hold a description and total point value
        if categories == None:
            self.categories = dict()
            self.enter_categories()
        else:
            self.categories = categories

    @classmethod
    def change_semester(cls, semester):
        """Modify the text of the semester that all courses are being added to"""
        cls.semester = semester

    def enter_categories(self):
        while True:
            print(f'Enter grading categories for {self.name}')
            acronym = input('5 letter max Category name: ')
            self.categories[acronym] = input(f'Enter total points for a single {acronym}: ')
            lcv = input('Do you have more categories to enter (Y/N)? ').casefold()
            os.system('cls')
            if lcv == 'n':
                break

    def enroll_students(self, number):
        self.student_count += number
        for x in range(number):
            temp_student = Student(self.categories)
            temp_student.fullname = input('Enter student first and last name: ')
            temp_student.enter_scores()
            self.class_roster.append(temp_student)

    def __str__(self):
        message = f'Course {self.section} - {self.name} has {self.student_count} students: '
        for student in self.class_roster:
            message = message + f'\n{student} - '
            for category in self.categories:
                message = message + f' {category}: {student.scores[category]} / {self.categories[category]}, '
        return message


class Student:
    """ Student class """

    def __init__(self, categories=None, fname='Jane', lname='Doe'):
        self.first = fname
        self.last = lname
        self.scores = dict()
        for category in categories:
            self.scores[category] = 0

    @property
    def fullname(self):
        return f'{self.first}, {self.last}'

    @fullname.setter
    def fullname(self, name):
        try:
            self.first, self.last = name.split(' ')
        except ValueError:
            pass

    def __str__(self):
        return self.fullname

    def enter_scores(self):
        for category in self.scores:
            self.scores[category] = int(input(f'Enter earned points for {category}: '))


# Main Logic
print('{:*^30}'.format('University System'))
Course.change_semester(input('Enter semester and year for which you are creating courses: '))

enter_courses = 'y'
print("\nEntering course information")
while enter_courses == 'y':
    course_name = input('Enter course name: ').upper()
    new_course = Course(course_name)
    courses.append(new_course)
    enter_courses = input("\nAdd another course (Y/N)? ").casefold()

# Add students to each course using enroll_students()
os.system('cls')
for course in courses:
    print(f'\nAdd students to {course.name} course')
    count = int(input('How many students do you want to enroll? '))
    course.enroll_students(count)

# Print Course Roster using Override methods to quickly display necessary data
os.system('cls')
print("\nCourse Information for {}".format(Course.semester))
for course in courses:
    print(course)
