# Write a function that will accept a list of numbers and calculate the mode.
# Input: [20, 10, 5, 15, 15, 10, 10, 5, 20, 5]
# Output: The mode is 5.

import statistics


def main():
    list = [20, 10, 5, 15, 15, 10, 10, 5, 20, 5]
    mode = statistics.mode([list])
    print(f'The mode of the list is {mode}.')


main()
