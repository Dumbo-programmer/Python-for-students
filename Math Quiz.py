import random
import operator

def generate_question(level):
    """Generate a math question based on the difficulty level."""
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    
    if level == 'easy':
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
    elif level == 'medium':
        num1 = random.randint(10, 50)
        num2 = random.randint(10, 50)
    else:  # 'hard'
        num1 = random.randint(50, 100)
        num2 = random.randint(50, 100)
    
    operation = random.choice(list(ops.keys()))
    
    if operation == '/':
        # Ensure we avoid division by zero and produce an integer result
        num2 = random.choice([i for i in range(1, 11) if num1 % i == 0])
        question = f"What is {num1} / {num2}?"
        correct_answer = ops[operation](num1, num2)
    else:
        question = f"What is {num1} {operation} {num2}?"
        correct_answer = ops[operation](num1, num2)

    return question, correct_answer

def math_quiz():
    print("Welcome to the Math Quiz!")
    
    # Choose difficulty level
    while True:
        level = input("Choose difficulty level (easy, medium, hard): ").strip().lower()
        if level in ['easy', 'medium', 'hard']:
            break
        else:
            print("Invalid choice. Please enter 'easy', 'medium', or 'hard'.")
    
    score = 0
    num_questions = 5
    
    for _ in range(num_questions):
        question, correct_answer = generate_question(level)
        
        while True:
            try:
                user_answer = float(input(question + " ").strip())
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        if abs(user_answer - correct_answer) < 0.01:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {correct_answer:.2f}.")

    print(f"\nYour final score is: {score}/{num_questions}")
    
    if score == num_questions:
        print("Excellent work! You got all the questions right!")
    elif score >= num_questions / 2:
        print("Good job! You got more than half of the questions right.")
    else:
        print("Keep practicing! You'll improve with more practice.")

    # Replay option
    while True:
        replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if replay == 'yes':
            math_quiz()
            break
        elif replay == 'no':
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    math_quiz()
