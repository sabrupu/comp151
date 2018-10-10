# Write a program that will generate the following shape:
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
#
# Hint: You will need to use nested loops (a loop within a loop!)


def print_triangle(n):
    for row in range(1, n+1):
        for col in range(1, row+1):
            print(' *', end='')
        print()
    for row in range(n-1, 0, -1):
        for col in range(1, row+1):
            print(' *', end='')
        print()


def main():
    print_triangle(5)


main()
