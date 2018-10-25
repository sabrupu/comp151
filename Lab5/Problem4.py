# print all prime numbers between 1 and n.
# Enter your number: 20
# 2 3 5 7 11 13 17 19


n = int(input('Enter a number: '))

for num in range(2, n):
    prime = True
    for i in range(2, n):
        if num % n == 0:
            prime = False
    print(num, end=' ')
