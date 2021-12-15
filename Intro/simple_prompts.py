total_points = 30

earned_points = input(f'Enter score out of {total_points}: ')

# type conversion, string to numeric types
# type classes: int(), float(), str(), bool(), dict(), list(), set(), tuple(), etc.
# convertedData = ClassNameOfNewDataType(dataToConvert)
num_earned_points = int(earned_points)
print(num_earned_points)

grade = num_earned_points / total_points
print(f'Grade: {grade:.1%}')
