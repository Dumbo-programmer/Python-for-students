import random

def load_names():
    """Load default name lists and allow user to add custom names."""
    first_names = ["John", "Jane", "Alex", "Emily", "Chris", "Katie", "Michael", "Sarah", "David", "Laura"]
    last_names = ["Smith", "Doe", "Johnson", "Brown", "Davis", "Wilson", "Miller", "Taylor", "Anderson", "Thomas"]
    middle_names = ["Marie", "James", "Lee", "Ann", "Paul", "Grace", "Renee", "Edward", "Rose", "Scott"]

    print("You can use default name lists or add your own.")
    if input("Would you like to add custom names? (yes/no): ").strip().lower() == 'yes':
        first_names += input("Enter custom first names separated by commas: ").split(',')
        last_names += input("Enter custom last names separated by commas: ").split(',')
        if input("Would you like to add middle names? (yes/no): ").strip().lower() == 'yes':
            middle_names += input("Enter custom middle names separated by commas: ").split(',')
    
    return first_names, last_names, middle_names

def name_generator():
    print("Welcome to the Enhanced Name Generator!")

    first_names, last_names, middle_names = load_names()

    while True:
        try:
            num_names = int(input("How many names would you like to generate? "))
            if num_names <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    while True:
        choice = input("Do you want to include middle names? (yes/no): ").strip().lower()
        if choice == 'yes':
            include_middle_name = True
            break
        elif choice == 'no':
            include_middle_name = False
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    # Generate names
    for _ in range(num_names):
        first_name = random.choice(first_names).strip()
        last_name = random.choice(last_names).strip()
        if include_middle_name:
            middle_name = random.choice(middle_names).strip()
            full_name = f"{first_name} {middle_name} {last_name}"
        else:
            full_name = f"{first_name} {last_name}"

        print(f"Generated name: {full_name}")

if __name__ == "__main__":
    name_generator()
