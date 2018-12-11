# Create a function that sums a list of numbers


def sum_nums_iterative(nums):
    sum = 0
    for num in nums:
        sum += num

    return sum


def sum_nums_recursive(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + sum_nums_recursive(nums[1:])


def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-2) + fib(n-1)


def main():
    nums = [1, 2, 3, 4, 5]
    print(f'Iterative sum = {sum_nums_iterative(nums)}')
    print(f'Recursive sum = {sum_nums_recursive(nums)}')

    print(f'First 40 Fibonacci numbers: ')
    for n in range(40):
        print(f'fib({n}) = {fib(n)}')


main()
