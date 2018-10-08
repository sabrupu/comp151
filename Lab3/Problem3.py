# Write a program that will accept a month’s # and return the number of days in that
# month.
# Enter a month: 2
# That month has 28 days (29 on a leap year!)
# Enter a month: 10
# That month has 31 days!


def days_in_month(month):
    if month == 4 or month == 6 or  month == 11 or \
        month == 9 or month == 11:
        return 30
    elif month == 2:
        return 28
    else:
        return 31


def main():
    month = int(input('Enter a month\'s number: '))

    days = days_in_month(month)

    print(f'There are {days} days in month {month} !')

main()
