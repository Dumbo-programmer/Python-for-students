import random
import string

def password_generator():
    print("Welcome to the Random Password Generator!")
    length = int(input("Enter the desired length of the password: "))

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))

    print(f"Generated password: {password}")

if __name__ == "__main__":
    password_generator()
