# Write a function that will convert a list of characters into a string. Return this string to
# main and display it.
# # Input: [‘H’, ‘e’, ‘l’, ‘l’, ‘o’]
# # Output: “Hello”


def join_chars(char_list):
    str = ''
    for c in char_list:
        str += c
    return str


def main():
    input = ['H', 'e', 'l', 'l', 'o', ' ', 'p', 'r', 'o', 'f.']
    output = join_chars(input)

    print(input)
    print(output)


main()
