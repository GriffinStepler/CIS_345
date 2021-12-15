# Griffin Stepler, CIS 345, iCourse, PE5
import random
import statistics

categories = ['Food', 'Quality', 'Value', 'Service', 'Staff', 'Ambiance']
entries = list()


def count_up(end):
    """Counts up from 1 to end argument"""
    n = 1
    while n <= end:
        yield n
        n += 1


def generate_surveys(number):
    """Simulate and generate x number of surveys"""
    for s in range(number):
        ratings = list()
        for category in categories:
            ratings.append(random.randint(0, 5))
        score = list(zip(categories, ratings))
        filtered_score = (s for s in score if s[1] > 0)
        yield filtered_score


# allow additional categories
amount = input('How many categories do you want rated for your restaurant? ')
count = count_up(int(amount))
print()
for n in count:
    categories.append(input(f'Category {n}: '))
# filter out blank entries
filtered_categories = filter(None, categories)

# get ratings for each category
print('On a scale of (low) 1 to 5 (high)\nrate your service in the following categories: ')
for c in categories:
    entries.append(input(f'Enter a rating for {c}: '))

# convert all entries' items to integers
rating = map(int, entries)
# create structure that pairs categories and ratings
restaurant_score = list(zip(categories, rating))
# filter out bad ratings
restaurant_filtered_score = [d for d in restaurant_score if 0 < d[1] < 6]
# simulate 100 surveys, store as dictionaries in results
surveys = generate_surveys(100)
results = map(lambda x: dict(x), surveys)

sums = {c: 0 for c in categories}
lengths = {c: 0 for c in categories}

for survey in results:
    print('Avg rating: {}'.format(statistics.mean(survey.values())))
    for cat in categories:
        try:
            sums[cat] += survey[cat]
            lengths[cat] += 1
        except KeyError:
            pass

print(f'\n{"Average Rating Per Category":^40}')
for cat in categories:
    print(f'{cat}: {sums[cat] / lengths[cat]:.4f}')
