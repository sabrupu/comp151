def static_allocation():
    static_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    # Each list is a row
    # Every number in the list is a column
    # static_list[0] = [0, 1, 2]
    # static_list[1] = [3, 4, 5]
    # static_list[2] = [6, 7, 8]
    # static_list[1][2] prints 5 (index 2 in list 1)

    print(static_list[1][2])


def dynamic_allocation():
    rows = 5
    cols = 5
    dynamic_list = []
    #
    # for row in range(rows):
    #     dynamic_list += [[0] * cols]  # Fill this list with 5 0's

    for row in range(rows):
        dynamic_list.append([])
        for col in range(cols):
            dynamic_list[row].append(0)  # Gives us [[0, 0, 0], [0, 0, 0], [0, 0, 0]

    print(dynamic_list)


def create_dynamically_allocated_list(rows, cols):
    dynamic_list = []

    for row in range(rows):
        dynamic_list += [[0] * cols]
    return dynamic_list


def main():
    static_allocation()


main()
