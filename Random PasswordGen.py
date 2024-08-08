import random
import string

def generate_password(length, include_special_chars=True):
    """Generate a random password with specified length and character options."""
    if length < 1:
        raise ValueError("Password length must be at least 1.")
    
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation if include_special_chars else ''
    
    # Combine character sets
    characters = letters + digits + special_chars
    if not characters:
        raise ValueError("No characters available for password generation.")
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    """Interactive password generator with user options."""
    print("Welcome to the Enhanced Random Password Generator!")
    
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 1:
                raise ValueError("Password length must be at least 1.")
            break
        except ValueError as ve:
            print(f"Invalid input: {ve}. Please enter a positive integer.")
    
    include_special_chars = input("Include special characters (e.g., @, #, $)? (yes/no): ").strip().lower()
    include_special_chars = include_special_chars in ['yes', 'y']
    
    try:
        password = generate_password(length, include_special_chars)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")
    
    while True:
        again = input("Would you like to generate another password? (yes/no): ").strip().lower()
        if again in ['yes', 'no']:
            break
        print("Invalid input. Please enter 'yes' or 'no'.")
    
    if again == 'yes':
        print("\nGreat! Let's generate another password.")
        password_generator()
    else:
        print("Thank you for using the Random Password Generator! Stay secure!")

if __name__ == "__main__":
    password_generator()
