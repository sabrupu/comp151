# Write a program that accepts a score from the user and prints the appropriate grade. Use
# the standard grade distribution of:
#
# +----+--------+----+--------+----+--------+----+--------+
# | A  | 93-100 | B+ | 87-89  | C+ | 77-79  | D  | 60-69  |
# | A- | 90-92  | B  | 83-86  | C  | 73-76  | F  |  0-59  |
# |    |        | B- | 80-82  | C- | 70-72  |    |        |
# +----+--------+----+--------+----+--------+----+--------+


def get_grade(score):
    if score < 0 or score > 100:
        return 'Invalid grade: Enter a value between 0-100'

    if score >= 93:
        return 'A'
    if score >= 90:
        return 'A-'
    if score >= 87:
        return 'B+'
    if score >= 83:
        return 'B'
    if score >= 80:
        return 'B-'
    if score >= 77:
        return 'C+'
    if score >= 73:
        return 'C'
    if score >= 70:
        return 'C-'
    if score >= 60:
        return 'D'
    if score >= 0:
        return 'F'


def main():
    print('Grade Determiner\n')

    # Get user input
    score = int(input('Score: '))

    # Determine grade
    grade = get_grade(score)

    # Print grade
    print(f'Grade: {grade}')


main()
