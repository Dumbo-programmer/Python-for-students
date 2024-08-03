def flashcard_quiz():
    print("Welcome to the Flashcard Quiz!")
    questions = {
        "What is the capital of France?": "Paris",
        "What is 2 + 2?": "4",
        "Who wrote 'To Kill a Mockingbird'?": "Harper Lee"
    }
    score = 0

    for question, answer in questions.items():
        user_answer = input(question + " ")
        if user_answer.lower() == answer.lower():
            score += 1

    print(f"Your score is: {score}/{len(questions)}")

if __name__ == "__main__":
    flashcard_quiz()
        