# 1. print all numbers from 1 to n in reverse.
# Enter your number: 5
# 5 4 3 2 1


def main():
    n = int(input('Enter a number: '))

    for i in reversed(range(n)):
        print(i + 1, end=' ')


main()
