import math
import statistics


def circumference(radius):
    return 2 * math.pi * radius


radii = [1, 2, 3, 4, 5, 10]
circumferences = list()

for r in radii:
    c = circumference(r)
    circumferences.append(c)

print('Circumferences appended to list from for loop')
print(circumferences)

# map(function, list) - applies the function to each value in the list; this replaces lines 12-14
perims = map(circumference, radii)
print(next(perims))
for p in perims:
    print(p)

AzTemps = [('Phx', 31), ('Tempe', 28), ('Yuma', 32)]

cel_to_fahrn = lambda info: (info[0], (9/5) * info[1] + 32)
temp_data = list(map(cel_to_fahrn, AzTemps))
print(temp_data)

# statistics module below
vals = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
# statistics module has an avg function that returns the mean of a data structure
avg = statistics.mean(vals)
print(avg)

# filter applies a function to all values in a list removing those that return false
above_avg = list(filter(lambda x: x > avg, vals))
print(above_avg)

# using filter to remove blank strings or zero numbers
names = ['ted', '', 'sue', 'bill', '', 'jen', 'emily', '', 'stu']
miles = [12, 0, 4, 1, 0, 38, 43]
names = list(filter(None, names))
miles = list(filter(None, miles))

print(names)
print(miles)

runs = list(zip(names, miles))
print(runs)
