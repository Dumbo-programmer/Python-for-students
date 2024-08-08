import random

def flashcard_quiz():
    print("Welcome to the Flashcard Quiz!")
    questions = {
        "What is the capital of France?": "Paris",
        "What is 2 + 2?": "4",
        "Who wrote 'To Kill a Mockingbird'?": "Harper Lee",
        "What is the chemical symbol for water?": "H2O",
        "Who painted the Mona Lisa?": "Leonardo da Vinci",
        "What is the largest planet in our solar system?": "Jupiter",
        "What is the smallest prime number?": "2",
        "Who discovered penicillin?": "Alexander Fleming"
    }
    
    while True:
        question_list = list(questions.items())
        random.shuffle(question_list)
        score = 0
        incorrect_answers = []

        for question, answer in question_list:
            user_answer = input(question + " ").strip()
            if user_answer.lower() == answer.lower():
                print("Correct!\n")
                score += 1
            else:
                print(f"Incorrect! The correct answer is {answer}.\n")
                incorrect_answers.append((question, answer))

        print(f"Your final score is: {score}/{len(questions)}")
        
        if incorrect_answers:
            print("\nReview of incorrect answers:")
            for question, answer in incorrect_answers:
                print(f"{question} - Correct answer: {answer}")

        replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if replay != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    flashcard_quiz()
