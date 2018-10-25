# 2. find the sum of all products of n and n + 1 from 1 to n.
# Enter your number: 4
# 1 * 2 + 2 * 3 + 3 * 4 + 4 * 5 = 40




def main():
    # Enter user input
    n = int(input('Enter a number: '))


    # Loop through numbers
    sum = 0
    prod = 0
    str = ''
    for i in range(1, n+1):
        sum += i
        prod *= i
        str += f'{i} + '

    #
