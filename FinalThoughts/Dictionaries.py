def single_dictionary_example():
    dict_a = {
        "number" : 5,
        "count" : 1
    }

    # Print entire dictionary
    print(dict_a)

    print()

    # Print all key names in a dictionary (key is the name associated with value)
    for x in dict_a:
        print(x)

    print()

    for x in dict_a:
        print(dict_a[x])
        # Access values via key

    dict_a["number"] = 10

    print(dict_a[x])

    # How to tell if a key already exists in the dictionary
    key_to_check = "number"

    if key_to_check in dict_a:
        print(f'{key_to_check} is a valid key!')
    else:
        print(f'{key_to_check} is not a valid key!')

        # Add a key-value entry to a dictionary

        print()

        # Remove a key value
        print()
        dict_a.pop("count")
        print(dict_a)
