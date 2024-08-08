import math

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True  # 2 is the only even prime number
    if n % 2 == 0:
        return False  # Exclude even numbers greater than 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def prime_checker():
    """Interactive prime number checker with improved user experience."""
    print("Welcome to the Enhanced Prime Number Checker!")

    while True:
        try:
            number = int(input("Enter a positive integer to check if it is prime: "))
            if number < 0:
                raise ValueError("Negative numbers are not considered for prime checking.")
            break
        except ValueError as ve:
            print(f"Invalid input: {ve}. Please enter a valid positive integer.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")

    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
    
    while True:
        again = input("Would you like to check another number? (yes/no): ").strip().lower()
        if again in ['yes', 'no']:
            break
        print("Invalid input. Please enter 'yes' or 'no'.")
    
    if again == 'yes':
        print("\nGreat! Let's check another number.")
        prime_checker()
    else:
        print("Thank you for using the Prime Number Checker! Have a great day!")

if __name__ == "__main__":
    prime_checker()
