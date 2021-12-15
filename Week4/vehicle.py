class Vehicle:
    """Docstring for class description"""

    # class variables - defined outside __init__
    business_name = 'untitled'

    # instance variables - defined inside __init__
    def __init__(self, vin='0', type='ground', miles=0.0):
        """Setup initial values of a vehicle"""
        # instance variables:
        self.vin = vin
        self.type = type
        self.__miles_driven = miles  # name mangling - when outside class, cannot access outside class

    @property  # getter
    def type(self):
        return self._type.upper()

    @type.setter  # setter
    def type(self, new_type):
        valid_types = ['ground', 'air', 'water']
        if new_type.casefold() in valid_types:
            self._type = new_type.upper()
        else:
            self._type = 'Unknown'

    @property
    def miles_driven(self):
        miles = str(f'{self.__miles_driven:.1f}')
        miles = miles.zfill(8)
        return miles

    @miles_driven.setter
    def miles_driven(self, new_miles):
        try:
            m = float(new_miles)
        except ValueError as err:
            print(err)
        else:
            self.__miles_driven = m

    @classmethod
    def change_business_name(cls, new_name):
        cls.business_name = new_name

    @classmethod
    def new_vehicle(cls, data):
        info = data.split(',')
        try:
            miles = float(info[2])
        except (ValueError, TypeError):
            miles = 0.0

        return cls(info[0], info[1], info[2])

    def __str__(self):  # override base class method
        return f'VIN: {self.vin}, Type: {self.type}, Miles: {self.miles_driven}'

    def __add__(self, other_vehicle):
        self.__miles_driven += other_vehicle.__miles_driven


v1 = Vehicle('1111', 'h', 1500.8)  # creates an object of the class vehicle, this calls the constructor/initializer
v2 = Vehicle('2222', 'air', 10)

# to use a setter:
v1.type = 'ground'  # treat the property as a variable
v1.miles_driven = '50000.9'

# print(v1.vin, v1.type, v1.miles_driven)  # this statement doesn't directly access variables, it accesses property getters
print(v1)
print(v2)
v1 + v2
print(v1)
