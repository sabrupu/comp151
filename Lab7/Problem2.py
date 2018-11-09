# Write a function that will accept a list and find the 2nd largest element in the list.
# Copy this function and make it work for 2nd smallest.
#
# # Input: [5, 20, 15, 25, 10]
# # Output: The 2nd largest element is 20.


def find_2nd_largest(list):
    if len(list) < 2:
        print("Error: List too short.")
        return

    first = second = -2147483648  # smallest number possible
    for e in list:
        if e > first:
            second = first
            first = e
        elif e > second:
            second = e

    return second


def main():
    accept = [5, 20, 15, 25, 10]
    output = find_2nd_largest(accept)
    print(output)


main()
