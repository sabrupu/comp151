# Write a function that will accept a list of numbers and calculate the mean.
# Input: [20, 10, 5, 15]
# Output: The mean is 12.5.


def ave(list):
    return sum(list) / len(list)


def main():
    list = [20, 10, 5, 15]
    average = ave(list)
    print(f'The mean of the list is {average}.')


main()
