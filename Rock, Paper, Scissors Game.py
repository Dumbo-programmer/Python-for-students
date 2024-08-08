import random

def get_computer_choice():
    """Randomly select the computer's choice."""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "win"
    else:
        return "lose"

def rock_paper_scissors():
    """Play the Rock, Paper, Scissors game with score tracking."""
    print("Welcome to Rock, Paper, Scissors!")
    choices = ["rock", "paper", "scissors"]
    
    user_score = 0
    computer_score = 0
    rounds_played = 0

    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'quit' to stop): ").lower()
        
        if user_choice == 'quit':
            print(f"Game Over! You won {user_score} times, the computer won {computer_score} times.")
            break

        if user_choice not in choices:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        if result == "win":
            print("You win!")
            user_score += 1
        elif result == "lose":
            print("You lose!")
            computer_score += 1
        else:
            print("It's a tie!")

        rounds_played += 1

        # Display scores and round summary
        print(f"Score: You {user_score} - {computer_score} Computer")
        print(f"Rounds played: {rounds_played}")

        # Ask user if they want to play again
        play_again = input("Would you like to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print(f"Thanks for playing! Final score: You {user_score} - {computer_score} Computer")
            break

if __name__ == "__main__":
    rock_paper_scissors()
