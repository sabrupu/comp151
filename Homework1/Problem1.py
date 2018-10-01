# Write a program that converts and prints a user-supplied measurement in inches into:
# a. foot (12 inches) c. centimeter (2.54/inch)
# b. yard (36 inches) d. meter (39.37 inches)


def inches_to_feet(inches):
    return inches / 12


def inches_to_yards(inches):
    return inches_to_feet(inches) / 3


def inches_to_centimeters(inches):
    return inches * 2.54


def inches_to_meters(inches):
    return inches_to_centimeters(inches) / 100


def main():
    print('Inch Converter\n')

    # Get user input
    inches = float(input('Enter the measurement(in inches): '))

    # Compute equivalent measurements
    feet        =   inches_to_feet(inches)
    yards       =   inches_to_yards(inches)
    centimeters =   inches_to_centimeters(inches)
    meters      =   inches_to_meters(inches)

    # Print equivalent measurements
    print('\nEquivalent measurements:')
    print(f'\t{feet       } ft')
    print(f'\t{yards      } yd')
    print(f'\t{centimeters} cm')
    print(f'\t{meters     } m' )


main()
