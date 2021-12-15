class Vehicle:
    """ Class with a mutable instance argument to demonstrate the TRAP """

    def __init__(self, vin='0', miles=0.0, owners=None):  # NEVER DEFAULT A MUTABLE
        """
        Initialize Vehicle object
        Accesses properties (setters) rather than the name-mangled private variables
        """
        self.vin = vin
        self.miles_driven = miles
        if owners == None:
            self.owners = list()  # this avoids the mutable argument trap
        else:
            self.owners = owners

    # Properties - setters and getters
    @property
    def vin(self):
        return self.__vin

    @vin.setter
    def vin(self, vin):
        self.__vin = vin.zfill(12)

    @property
    def miles_driven(self):
        miles = str(f'{self.__miles_driven:.1f}')
        miles = miles.zfill(8)
        return miles

    @miles_driven.setter
    def miles_driven(self, miles):
        self.__miles_driven = miles

    # Instance methods
    def add_owners(self, new_owner):
        self.owners.append(new_owner)

    def display_owners(self):
        for o in self.owners:
            print(o)


v1 = Vehicle('1', '10000.1')
v1.add_owners('Jeff')
v1.add_owners('Lucy')

v2 = Vehicle('2', '20000.2')
v2.add_owners('Rachel')
v2.add_owners('Zach')

v3 = Vehicle('3', '30000.3', ['Allie', 'Albert'])

print('V1 Owners')
v1.display_owners()

print('\nV2 Owners')
v2.display_owners()

print('\nV3 Owners')
v3.display_owners()
