# for is used for a set number
# while is used when we don't know how many times the user will input numbers

# Write a function that will read in numbers
# from the user and add them together.
# If the user enters -1, stop and print the sum

# while i < j:
#     print('i = ', i)
#     i += 1


def get_numbers_sum():
    sum = 0
    user_input = int(input('Enter a number: '))

    while user_input != -1:
        sum += user_input
        user_input = int(input('Enter a number: '))

    return sum

def main():
    get_numbers_sum()


main()
