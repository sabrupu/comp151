import math

def main():
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

    # For each of the functions below, add the correct number of arguments!
    grade_book_average = calculate_grade_book_average()
    student_average = calculate_student_average()
    subject_average = calculate_subject_average()

    print(f"Grade book Average: {grade_book_average}")
    print(f"Student {selected_student} Average: {student_average}")
    print(f"Subject {selected_subject} Average: {subject_average}")


# Function that returns the average of all grades, across all subjects, of all students
def calculate_grade_book_average():
    average = 0


# Function that returns the average of all grades across all subjects
def calculate_student_average():
    average = 0



# Function that will return the average of all grades across a single subject from all students
def calculate_subject_average():
    average = 0




main()