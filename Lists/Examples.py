
def fill_list():
    test = []

    for i in range(1, 11):
        test.append(i)

    return test

# A function that accepts a min and max
# Then returns a list of all even numbers between min and max inclusive


def get_even_list():
    even_list = []

    for i in range(min, max + 1):
        if i % 2 == 0:
            even_list.append(i)
    return even_list


def print_list(list):
    for i in list:
        if i % 2 == 0:
            print(i, end=' ')


def find_max(list):
    max = 0

    for i in list:
        if i > max:
            max = i
        return max


def clone_list():
    new_list = []

    for i in list:
        return list


def main():

    my_list = fill_list()

    print(my_list)

    print(get_even_list())


    main()
