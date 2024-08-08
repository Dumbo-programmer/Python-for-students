def grade_calculator():
    print("Welcome to the Grade Calculator!")
    
    while True:
        try:
            total_marks = float(input("Enter total marks: "))
            if total_marks <= 0:
                print("Total marks should be a positive number. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for total marks.")
    
    while True:
        try:
            obtained_marks = float(input("Enter obtained marks: "))
            if obtained_marks < 0:
                print("Obtained marks cannot be negative. Please try again.")
                continue
            if obtained_marks > total_marks:
                print("Obtained marks cannot be greater than total marks. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for obtained marks.")
    
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

    feedback = {
        'A': "Excellent work! Keep it up!",
        'B': "Good job! You can push for an A next time.",
        'C': "Fair effort. There's room for improvement.",
        'D': "You passed, but consider reviewing the material.",
        'F': "Unfortunately, you failed. Please study the material and try again."
    }

    print(feedback[grade])

if __name__ == "__main__":
    grade_calculator()
