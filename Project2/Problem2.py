# Write a recursive function that for each number i from 1 to n computes the sum of i to the
# 5th power, if i is even, and -i cubed if i is odd.
# Running this function with n = 10 should return 140,375


# End condition
def sum_powers(n):
    if n == 1:
        return (-1) ** 3

    # Decrementing by 1 until n = 1
    if n % 2 == 0:
        power = n ** 5
    else:
        power = (-n) ** 3

    return power + sum_powers(n - 1)


def main():
    n = int(input('Enter a number: '))
    print(f'sum = {sum_powers(n):,}')


main()
