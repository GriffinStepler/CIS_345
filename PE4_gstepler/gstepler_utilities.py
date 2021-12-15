# Griffin Stepler, CIS345, iCourse, PE4


def header(title):
    """
    prints title format of input
    """
    print(f'{title:*^30}')


def what_type(item):
    """
    returns the class type of item
    """
    return str(type(item))


if __name__ == "__main__":
    header('Sample Header')
    string_type = str()
    list_type = list()
    print(what_type(string_type))
    print(what_type(list_type))
