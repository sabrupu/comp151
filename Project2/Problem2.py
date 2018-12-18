# Write a recursive function that for each number i from 1 to n computes the sum of i to the
# 5th power, if i is even, and -i cubed if i is odd.
# Running this function with n = 10 should return 140,375


def sum_powers(n):
    # Check for end condition
    if n == 1:
        return (-1) ** 3

    if n % 2 == 0:
        power = n ** 5
    else:
        power = (-n) ** 3

    return power + sum_powers(n - 1)


def main():
    print('Project 2, Problem 2\n')

    n = int(input('Enter a number: '))
    print(f'sum = {sum_powers(n):,}')


main()
