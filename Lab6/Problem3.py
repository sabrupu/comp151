# Write a function that will return a random item from a list. Return this item to main and
# display it.
#  Input: [5, 10, 15, 20, 25]
#  Output: 5 OR 10 OR 15 OR 20 OR 25


import random


def rand_item(item_list):
    n = len(item_list)
    i = random.randint(1, n)
    return item_list[i - 1]


def main():
    input = [1, 2, 3, 4, 5]
    output = rand_item(input)

    print(input)
    print(output)


main()
