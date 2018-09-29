# Modulo Operator: %
# Write a function that will tell if a year is
# a leap year or not.
# Leap years
# 1700 - NO
# 2000 - YES


def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def main():
    year = int(input('Enter year: '))
    result = is_leap_year(year)
    if result:
        print(f'Year {year} is a leap year :)')
    else:
        print(f'Year {year} is not a leap year :(')

main()