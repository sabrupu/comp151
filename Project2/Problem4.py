# Write a function that will create a dictionary of every word in a text file as well as the number
# of occurrences of that word.
#
# Then, write the following functions:
#     - See if a user-supplied word exists in the dictionary, if so print the number of
#       occurrences. Else, print that it doesn't exist.
#     - Find the word with the highest number of occurrences.
#     - Find the word with the lowest number of occurrences.
#
# Upon running, your user should be able to search for as many words as they want until
# they are ready to quit the program.


def read_file(file):
    stream = open(file, 'r')
    lines = stream.readlines()
    stream.close()
    return lines


def create_dict(lines):
    dict = {}  # {key (word) : {value (number of occurrences)}

    for line in lines:
        words = line.split(' ')
        for word in words:
            word = word.strip(',.;:?!/()[]{}<>\'\"\n\r\t').lower()
            if word in dict:
                dict[word] += 1
            else:
                dict[word] = 1

    return dict


def exists(word, dict):
    if word in dict:
        num_occurrences = dict[word]
        print(f'The word {word} exists {num_occurrences} times.')
    else:
        print(f'The word {word} does not exist.')


def word_with_most_occurrences(dict):
    words = []
    most_occurrences = max(dict.values())

    for word in dict:
        num_occurrences = dict[word]
        if num_occurrences == most_occurrences:
            words.append(word)

    return words


def word_with_least_occurrences(dict):
    words = []
    least_occurrences = min(dict.values())

    for word in dict:
        num_occurrences = dict[word]
        if num_occurrences == least_occurrences:
            words.append(word)

    return words


def main():
    print('Project 2, Problem 4\n')

    lines = read_file('SherlockHolmes.txt')

    dict = create_dict(lines)

    while True:
        entry = input('Enter a word to search: ')
        if entry == '':
            print()
            break
        exists(entry, dict)
        print()

    print(f'word with the highest number of occurrences is:  {word_with_most_occurrences(dict)}')
    print(f'word with the lowest number of occurrences is:  {word_with_least_occurrences(dict)}')


main()
