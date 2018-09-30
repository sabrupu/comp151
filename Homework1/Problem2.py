# Write a simple calculator that performs Addition, Subtraction, Multiplication, and
# Division between 2 user-entered numbers. The operation performed should be dictated by
# the user


def calc_sum(a, b):
    return a + b


def calc_diff(a, b):
    return a - b


def calc_prod(a, b):
    return a * b


def calc_quot(a, b):
    return a / b


def main():
    print('Calculator:')

    # Get user input
    print('\nEnter two numbers:')
    a  = int(input('\ta = '))
    b  = int(input('\tb = '))
    op = input('Enter an operator (+, -, *, /): ')

    # Perform operation
    if   op == '+':
        res = calc_sum(a, b)
    elif op == '-':
        res = calc_diff(a, b)
    elif op == '*':
        res = calc_prod(a, b)
    elif op == '/':
        res = calc_prod(a, b)
    else:
        print('Error: Unidentified operator.')
        return

    print('\nResult:')
    print(f'\t {a} {op} {b} = {res}')


main()
