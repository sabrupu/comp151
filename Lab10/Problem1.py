# Write a function that will accept two integers a, and b. Your function will then create an
# axb multiplication table stored in a 2D list. Write additional functions to do the
# following:
# ● Print the entire table
# ● Print a specific row in the table
# ● Print a specific column in the table


def multiplication_table():
    nrow = 0
    ncol = 0
    table = nrow * [ncol * [0]]

    row = int(input('Enter a number: '))
    col = int(input('Enter a number: '))

    for row in range(nrow):
        print(f'{row}:10,', end='')
        for col in range(ncol):
            prod = row * col
            print(f'{prod}:10', end='')
    print(table)


def main():
    multiplication_table()


main()

