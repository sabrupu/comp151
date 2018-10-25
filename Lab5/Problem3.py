# count the number of digits in n.
# Enter your number: 41256
# 5


def main():

    n = int(input('Enter a number: '))

    length = len(str(abs(n)))

    print(length)

main()

