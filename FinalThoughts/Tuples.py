# Tuples are read only: collection of data
# Create them by using () not {}
# Tuples can be changed, lists can't


def main():

    my_tuple = (5, 10, 15)
    print(my_tuple)
    print(my_tuple[0])

    mixed_tuple = (1, 2, 3) + (10, 20, 30)
    print(mixed_tuple)


main()
