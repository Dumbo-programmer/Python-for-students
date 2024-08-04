#Math Quiz
import random

def math_quiz():
    print("Welcome to the Math Quiz!")
    score = 0

    for _ in range(5):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(['+', '-', '*', '/'])
        
        if operation == '/':
            question = f"What is {num1 * num2} / {num2}?"
            correct_answer = num1
        else:
            question = f"What is {num1} {operation} {num2}?"
            correct_answer = eval(f"{num1}{operation}{num2}")

        user_answer = float(input(question + " "))

        if user_answer == correct_answer:
            score += 1

    print(f"Your score is: {score}/5")

if __name__ == "__main__":
    math_quiz()
