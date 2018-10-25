def middle(n):
    squared = square(n)
    return squared * 2


def square(n):
    return n * n


def main():
    n = int(input('Enter a number: '))
    print(middle(n))


main()
