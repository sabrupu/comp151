# Problem 2


def print_pyramid(n):
    if n < 1:
        print('Invalid number.')

    width = (n - 1) * 2 + 1  # pyramid width

    print(f'{1:^{width}}')  # first row differs from pattern
    for row in range(1, n):
        row_str = ''

        # Loop through ascending numbers
        for col in range(0, row + 1):
            row_str += str((row + col) % 10)

        # Loop through descending numbers
        for col in range(row - 1, -1, -1):
            row_str += str((row + col) % 10)

        # Print row with spacing
        print(f'{row_str:^{width}}')


def main():
    print('\nPyramid\n')

    n = int(input('Enter number of rows: '))
    print()
    print_pyramid(n)
    print()


main()
