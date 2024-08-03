def grade_calculator():
    print("Welcome to the Grade Calculator!")
    total_marks = float(input("Enter total marks: "))
    obtained_marks = float(input("Enter obtained marks: "))

    percentage = (obtained_marks / total_marks) * 100

    if percentage >= 90:
        grade = 'A'
    elif percentage >= 80:
        grade = 'B'
    elif percentage >= 70:
        grade = 'C'
    elif percentage >= 60:
        grade = 'D'
    else:
        grade = 'F'

    print(f"Your grade is: {grade} ({percentage:.2f}%)")

if __name__ == "__main__":
    grade_calculator()
