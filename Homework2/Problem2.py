# Write a program that will read a number n from the user then generate a multiplication
# table from 1-n.

#     __1___2___3___4___5__
#   |1| 1   2   3   4   5
#   |2| 2   4   6   8   10
#   |3| 3   6   9   12  15
#   |4| 4   8   12  16  20
#   |5| 5   10  15  20  25


# Enter user input
n = int(input('Enter a number: '))
print()

# Generate multiplication table
print(f'{"":8}', end='')
for col in range(1, n+1):
    print(f'{col:8}', end='')
print()

for row in range(1, n+1):
    print(f'{row:8}', end='')
    for col in range(1, n+1):
        prod = row * col
        print(f'{prod:8}', end='')
    print()
