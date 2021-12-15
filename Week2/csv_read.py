import csv
import os

# with open('students.csv') as fp:
#     read_data = csv.reader(fp)  # csv reader object
#     students = list(read_data)
#     students = students[1:]

    # nicely formatted output of a .csv
    # fp.seek(0)
    # for row in read_data:
    #     print(f'{row[0]:10}{row[1]:10}{row[2]:10}{row[3]:10}')
    #     # for value in row:
    #     #     print(f'{value:10}', end='')
    #     # print()

'''
products = [[2, 'Paper', 5.29],
            [3, 'Backpack', 50.49],
            [4, 'Eraser', 11.55]]

with open('products.csv', 'w', newline='') as fp:
    write_data = csv.writer(fp, quotechar='"', quoting=csv.QUOTE_ALL)  # puts quotation delimiters around all
    write_data.writerow([1, 'All', 1.99])  # writerow() automatically adds \n; set newline='' in open() to avoid
    write_data = csv.writer(fp, quotechar='"', quoting=csv.QUOTE_MINIMAL)  # quotations around only delimited
    write_data.writerow([2, 'Minimal, using, delimiter', 2.99])
    write_data = csv.writer(fp, quotechar='"', quoting=csv.QUOTE_NONNUMERIC)  # quotations around nonnumerics only
    write_data.writerow([3, 'NonNumeric', 3.99])
    write_data = csv.writer(fp, quoting=csv.QUOTE_NONE)  # no quotations
    write_data.writerow([4, 'None', 4.99])

with open('products.csv') as fp:
    read_data = csv.reader(fp)
    for row in read_data:
        print(f'{row[0]:10}{row[1]:30}{row[2]:20}')
'''

if not os.path.isfile('products.csv'):
    with open('products.csv', 'w', newline='') as fp:
        writer = csv.writer(fp)
        writer.writerow(['ID', 'Name', 'Price'])

with open('products.csv', 'a', newline='') as fp:
    write_data = csv.writer(fp)
    write_data.writerow([1, 'Pen', 1.99])

with open('products.csv') as fp:
    data = csv.reader(fp)
    for row in data:
        print('{:3}{:-<10}{:$>5}'.format(*row))
