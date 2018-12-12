def multiple_dictionary_example():
    # A list of dictionaries/ This can be an empty list!
    dictionaries = []

    for entry in dictionaries:
        print(entry)

        user_input = int(input("Enter a number: "))

        while user_input != 0:

            # Use this for problem 4 in Project 2
            exists = False
            for entry in dictionaries:
                if entry["number"] == user_input:  # If this dictionary's number is equal to what the user input then
                    entry["count"] += 1            # this dictionaries count will be incremented by 1
                    exists = True
                    break

            if exists == False:
                dictionaries.append({"number": user_input, "count": 1})

            for entry in dictionaries:
                print(entry)
