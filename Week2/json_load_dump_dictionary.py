import json
# javascript object notation

# serialization encodes python into json item
# web developers use json as a standard

'''
titles = ['Name Partner', 'Sr. Partner', 'Jr. Partner', 'Lawyer', 'Paralegal']

workers = {'1': {'Name': 'Jenn Burns', 'Pay': 50.78, 'Hours': 3},
           '2': {'Name': 'Louis Lit', 'Pay': 68.31, 'Hours': 40}}

print(type(titles), type(workers))

file = open('titles.json', 'w')
json.dump(titles, file)
file.close()

with open('workers.json', 'w') as fp:
    json.dump(workers, fp)
'''

# deserialization decodes the file from json to python

# 1. open your program and read data from a file into the program
# 2. process the data
# 3. close write data to the file - save

with open('workers.json', 'r') as fp:
    workers = json.load(fp)

print(type(workers))
# print(workers)
for k, v in workers.items():
    print(f'{k}: ', end='')
    for value in v.values():
        print(f'{value}\t', end='')
    gross = workers[k]['Pay'] * workers[k]['Hours']
    net = round(gross - 34.04, 2)
    print(f'Net: {net: >,.2f}')

# with open('titles.json') as fp:
#     titles = json.load(fp)
#     for t in titles:
#         print(t)
