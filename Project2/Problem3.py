# Write a recursive function that will print all permutations of the given list. For the code
# given, your output should be similar to the following:
# [‘A’, ‘B’, ‘C’]
# [‘A’, ‘C’, ‘B’]
# [‘B’, ‘A’, ‘C’]
# [‘B’, ‘C’, ‘A’]
# [‘C’, ‘B’, ‘A’]
# [‘C’, ‘A’, ‘B’]


def compute_permutations(string, index):
    if index >= len(string):
        print(string)
        return

    for i in range(index, len(string)):
        result = swap(string, index, i)  # Swapping element in string at index i
        compute_permutations(result, index + 1)


def swap(string, a, b):
    elem1 = string[a]
    elem2 = string[b]

    result = string.copy()
    result[a] = elem2
    result[b] = elem1
    return result


def main():
    print('Project 2, Problem 3\n')

    string = ['A', 'B', 'C']
    compute_permutations(string, 0)


main()
