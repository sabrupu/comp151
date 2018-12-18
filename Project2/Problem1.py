import math


# Function that returns the average of all grades, across all subjects, of all students
def calculate_grade_book_average(grade_book):
    num_students = len(grade_book)
    num_subjects = len(grade_book[0])
    num_grades   = len(grade_book[0][0])

    average = 0
    for student in range(num_students):
        for subject in range(num_subjects):
            grades = grade_book[student][subject]
            average += sum(grades)

    total_num_grades = num_students * num_subjects * num_grades
    average /= total_num_grades

    return average


# Function that returns the average of all grades across all subjects
def calculate_student_average(grade_book, student):
    num_subjects = len(grade_book[0])
    num_grades   = len(grade_book[0][0])

    average = 0
    for subject in range(num_subjects):
        grades = grade_book[student][subject]
        average += sum(grades)

    total_num_grades = num_subjects * num_grades
    average /= total_num_grades

    return average


# Function that will return the average of all grades across a single subject from all students
def calculate_subject_average(grade_book, subject):
    average = 0
    return average


def natural_round(n):
    return int(n + 0.5)


def main():
    print('Project 2, Problem 1\n')

    # 3x2x4 array
    grade_book = [
        # Student 1: Avg = 92.5
        [
            # Student 1 Subject 1: Avg = 96.25
            [100, 90, 95, 100],
            # Student 1 Subject 2: Avg = 88.75
            [85, 90, 80, 100]
        ],

        # Student 2: Avg = 81.875
        [
            # Student 2 Subject 1: Avg = 77.5
            [75, 70, 85, 80],
            # Student 2 Subject 2: Avg = 86.25
            [90, 85, 90, 80]
        ],
        # Student 3: Avg = 55.625
        [
            # Student 3 Subject 1: Avg = 47.5
            [45, 50, 35, 60],
            # Student 3 Subject 2: Avg = 63.75
            [70, 50, 75, 60]
        ]
    ]

    selected_student = int(input("Which student's average do you want to see?\nEnter 1, 2, 3: "))
    selected_subject = int(input("Which subject's average do you want to see?\nEnter 1, 2: "))
    print()

    # For each of the functions below, add the correct number of arguments!
    grade_book_average = calculate_grade_book_average(grade_book)
    student_average = calculate_student_average(grade_book, selected_student - 1)
    subject_average = calculate_subject_average(grade_book, selected_subject - 1)

    print(f"Grade book Average: {natural_round(grade_book_average)}")
    print(f"Student {selected_student} Average: {natural_round(student_average)}")
    print(f"Subject {selected_subject} Average: {natural_round(subject_average)}")


main()
