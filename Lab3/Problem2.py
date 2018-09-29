# Write a program that tells whether a given letter is a consonant or vowel.
# Enter a letter: A
# ‘A’ is a vowel.
# Enter a letter: c
# ‘c’ is a consonant.

def is_it_a_vowel(vowel):
    if   vowel == 'A':
        return True
    elif vowel == 'E':
        return True
    elif vowel == 'I':
        return True
    elif vowel == 'O':
        return True
    elif vowel == 'U':
        return True
    else:
        return False


def main():
    vowel = input('Enter a letter: ')
    letter = is_it_a_vowel(vowel)
    if letter == vowel:
        print(f'{letter}, it is a vowel.')
    else:
        print(f'{letter}, it is a consonant.')

main()