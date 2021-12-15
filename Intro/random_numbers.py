import random

# for i in range(8):
#     print(random.randint(1, 10))  # latter is inclusive
#     print(random.random())
#     print(random.uniform(1, 10))

cards = list(range(52))
# print(cards)
# print(random.choice(cards))
# deal = random.choices(cards, k=5)  # this can give two of the same card though
# deal = random.sample(cards, k=5)     # random.sample() cannot give duplicates
# print(deal)

colors = ['red', 'black', 'green']
spin = random.choices(colors, weights=[18, 18, 2], k=10)
print(spin)
