# Write a program that tells whether a triangle is Equilateral, Isosceles, or Scalene.
# Equilateral: All 3 sides are equal. 5 5 5
# Isosceles: 2 sides are equal. 5 5 10
# Scalene: 0 sides are equal. 5 3 10


def name_triangle(s1, s2, s3):
    if s1 == s2 and s2 == s3:
        print('I am an equilateral.')
    elif s1 != s2 or s2 == s3 or s2 == s1:
        print('I am an isosceles.')
    else:
        print('I am a scalene.')


def main():
    side1 = int(input('Enter a number: '))
    side2 = int(input('Enter a number: '))
    side3 = int(input('Enter a number: '))

    name_triangle(side1, side2, side3)


main()
