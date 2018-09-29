print("Problem 1")
print('')
def main():
    years = 22
    months   =   age_in_months(years)
    days     =   age_in_days(months)
    hours    =   age_in_hours(days)
    seconds  =   age_in_seconds(hours)


    print(f'Age in years = {years}\r\nAge in months = {months}\r\nAge in days = {days}\r\nAge in hours = {hours}'
          f'\r\nAge in seconds = {seconds}'.format(years, months, days, hours, seconds))
    print('')

    print('The sum is', sum)
    print('The difference is', difference)
    print('The product is', product)


def get_user_age():
    return

def age_in_months(age):
    return age * 12

def age_in_days(age):
    return age * 365

def age_in_hours(age):
    return age * 24

def age_in_seconds(age):
    return age * 60





print("Problem 2")

def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def prod(sum, diff):
    return sum * diff

num1 = 12
num2 = 6

sum         = num1 + num2
difference  = num1 - num2
product     = sum  * difference

main()

