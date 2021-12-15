class Person:
    """ Person class - holds info like name and DoB """

    def __init__(self, name='John Doe', dob='1/1/1900'):
        """
        Initializer for Person class
        :param name: name of the person - defaults John Doe
        :param dob: date of birth - defaults 1/1/1900
        """
        self.name = name
        self.date_of_birth = dob

    @property
    def name(self):
        return self.__name.capitalize()

    @name.setter
    def name(self, new):
        if new.isalpha() and len(new) >= 1:
            self.__name = new.capitalize()
        else:
            self.__name = 'John Doe'


    def __str__(self):
        return f'Name: {self.name}\tDate of birth: {self.date_of_birth}'


class Patient(Person):  # inherits from Person class
    """ Extend Person by adding patient data and methods """

    def __init__(self, ins_c, name='', dob=''):
        """ docstring for Patient __init__ """
        super().__init__(name, dob)
        self.insurance_carrier = ins_c


p1 = Person('Jack', '3/12/1991')
p2 = Patient('cigna', 'Jill', '3/25/1995')

people = [p1, p2]

for p in people:
    if isinstance(p, Patient):
        print(f'{p}' + f'\tInsurance: {p.insurance_carrier}')
    else:
        print(p)