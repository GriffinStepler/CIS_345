# set is an unordered list, no duplicates
# can convert lists to sets to remove duplicates
numbers = [1, 2, 3, 4, 1, 6, 8, 2, 3]
unique_numbers = set(numbers)

print(numbers)
print(unique_numbers)
print(type(unique_numbers))

word = set('hello')
print(word)
print(type(word))
print(id(word))

# frozenset is an unordered tuple, no duplicates
# can convert tuples to frozensets to remove duplicates
hello = 'hello'
word = frozenset(hello)
print(word)
print(id(word))

movies = ['Avatar', 'Avengers', 'Star Wars', 'Avatar', 'Avatar']
unique_movies = frozenset(movies)
print(len(unique_movies))
for m in unique_movies:
    print(m)

print(type(unique_movies))