import random
# from random import randint
from difflib import get_close_matches


def look_up(search_word, collection, list_size, percent_match=0.6):
    """
    Find search_word in collection and
    return matches of list_size matching with a
    percent of percent_match
    """
    return get_close_matches(search_word, collection, n=list_size, cutoff=percent_match)


if __name__ == "__main__":
    words = ['care', 'caretaker', 'cat', 'caring', 'cake', 'car', 'carrot', 'cart', 'carve', 'carry', 'Timothy']
    find = input('Enter a search word: ')
    results = look_up(find, words, 5, .4)
    print(results)
