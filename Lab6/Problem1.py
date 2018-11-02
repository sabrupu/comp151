# Write a function that will accept two arguments, a string and a character. Your function
# should search the string for and count the number of occurrences of the given character.
#
# Enter the string to search: Sally sells sea shells down by the sea shore.
# Enter the character to count: s
#
# There were 8 s's in that string.


def search_string(string, char):
    count = 0
    for c in string:
        if c.lower() == char.lower():
            count += 1
    return count


def main():
    string      = input('Enter a string to search: '    )
    character   = input('Enter the character to count: ')

    count = search_string(string, character)

    print(f'There were {count} {character}\'s in that string.')


main()
