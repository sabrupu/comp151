# Write a program that will read a number n from the user then print all values from 1-n.
# Example:
# Enter a number: 6
# 1 2 3 4 5 6


def main():

    n = int(input('Enter a number: '))

    for i in range(1, n + 1):
        print(i, end=' ')


main()
