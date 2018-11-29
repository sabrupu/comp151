# Write a function that will accept a list of numbers and calculate the median.
# Input: [20, 10, 5, 15]
# Output: The median is 12.5.
# Input: [20, 10, 5, 15, 30]
# Output: The median is 15


def median(list):
    sort_list = sorted(list)
    length = len(list)
    middle = length // 2

    if length == 1:
        return sort_list
    elif length % 2 == 0:
        return sum(sort_list[middle - 1 : middle + 1]) / 2
    else:
        return sort_list[middle]


def main():
    list = [20, 10, 5, 15]
    print(f'The median is {median(list)}.')
    list = [20, 10, 5, 15, 30]
    print(f'The median is {median(list)}.')


main()
