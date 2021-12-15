# Griffin Stepler, CIS345, iCourse, PE7

# TODO: Student class
class Student:
    """ Student class """

    def __init__(self, fname=''):
        self.first_name = fname
        self.last_name = ''

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, new):
        if new.isalpha():
            self.__first_name = new.capitalize()
        else:
            self.__first_name = 'Unknown'

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, new):
        if new.isalpha():
            self.__last_name = new.capitalize()
        else:
            self.__last_name = 'Unknown'

    def __str__(self):
        return f'{self.__first_name} {self.__last_name}'


# TODO: GradStudent class
class GradStudent(Student):
    """ Extends Student class """

    def __init__(self, thesis, fname=''):
        """ Docstring for GradStudent extending Student __init__ """
        super().__init__(fname)
        self.thesis = thesis

    @property
    def thesis(self):
        return self.__thesis.upper()

    @thesis.setter
    def thesis(self, thesis):
        self.__thesis = f'Thesis: {thesis}'

    def __str__(self):
        return f'{self.__first_name} {self.__last_name}\n\t{self.__thesis}'


# TODO: PhDStudent class
class PhDStudent(Student):
    """ PhDStudent class extending Student class """

    def __init__(self, dissert, fname=''):
        super().__init__(fname)
        self.dissertation = dissert

    @property
    def dissertation(self):
        return self.__dissertation.upper()

    @dissertation.setter
    def dissertation(self, dissert):
        self.__dissertation = f'Dissertation: {dissert}'


def add_student(studentType):
    """Get student data and create an object to be returned"""
    student = None
    # Get first and last name here because all students need this data
    first = input('Enter first name: ')
    last = input('Enter last name: ')

    # TODO: Determine student type and construct an object and save in student

    # TODO: Assign last_name using our object's property then return student


# Main Function
def main():
    """Main program logic"""
    students = []
    entry = ''
    print("{:^50}".format('Student Management System'))

    while entry != 'X':
        studentTypes = ['S', 'G', 'P']
        # Get user entry and capitalize the entry
        entry = input(
            '\nEnter (S)tudent, (G)radStudent, (P)hDStudent or (X)exit: ')
        entry = entry.upper()

        # TODO: Is user entry one of studentTypes. Yes - add_student to list

    # TODO: print students and dissertation if the student is a PhD type
    print("\nThe following students were added...")


if __name__ == "__main__":
    # call and execute the main function
    main()
