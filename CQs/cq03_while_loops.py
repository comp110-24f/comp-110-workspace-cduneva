"""Challenge question 3"""

__author__ = "730653037"


def num_instance(phrase=str, search_char=str) -> int:
    count = 0
    index = 0
    # created 2 local variables count and index,
    while index < len(phrase):
        # checks to see if every letter of the phrase had been checked
        if phrase[index] == search_char:
            count += 1
            # increases the count to check different letters in each character slot
        index += 1
        # changes which character slot is being checked
    return count
