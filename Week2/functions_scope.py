from imports_and_string_search import look_up

def average(args):
    """Add all the arguments to a total and count the args
    return the average of args passed in"""
    count = 0
    total = 0
    for val in args:
        count += 1
        total += val
        val = 0
    return total / count


# print(average(1, 2, 45, 4))
list_nums = [1, 2, 45, 4]
tuple_nums = (1, 2, 45, 4)
print(average(list_nums))
print(list_nums)
# print(average(tuple_nums))

look_up()
