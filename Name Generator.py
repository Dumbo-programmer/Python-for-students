#Name Generator
import random

def name_generator():
    print("Welcome to the Name Generator!")
    first_names = ["John", "Jane", "Alex", "Emily", "Chris", "Katie"]
    last_names = ["Smith", "Doe", "Johnson", "Brown", "Davis", "Wilson"]

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    print(f"Generated name: {first_name} {last_name}")

if __name__ == "__main__":
    name_generator()
