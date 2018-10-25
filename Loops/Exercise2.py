# Read in two numbers from the user.
# Print all of the EVEN numbers in that range.


# def main():
    # i = 0
    # j = 10
    #
    # while i < j:
    #     print('i = ', i)
    #     i += 1

    # () tells you if something is a function
    # for is used for a set number
    # while is used when we don't know how many times the user will input numbers


    # Returns a list of numbers
    # 'i' gets set as the first element
    # container of numbers
    # range only returns ints
#     for i in range(10, 20):
#         print('i = ', i)
#
#
# main()

def print_evens(start, end):
    for i in range(start, end + 1):
        if i % 2 == 0:
            print(i)


def main():

    min = int(input('Enter starting value: '))
    max = int(input('Enter ending value: '))
    print_evens(min, max)


main()
