# Write a program that will read a number n from the user then print and sum all even
# numbers from 1-n.
# Enter a number: 12
# 2 + 4 + 6 + 8 + 10 + 12 = 42


def main():
    # Enter user input
    n = int(input('Enter a number: '))

    # Loop through even natural numbers up to n
    sum = 0
    str = ''
    for i in range(2, n+1, 2):
        sum += i
        str += f'{i} + '

    # Complete and print output string
    str = str[:-3] + f' = {sum}'
    print(str)


main()
