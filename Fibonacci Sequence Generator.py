def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]  # Ensure the sequence is sliced correctly for n < 2

def fibonacci_generator():
    print("Welcome to the Fibonacci Sequence Generator!")
    
    while True:
        try:
            terms = int(input("Enter the number of terms (positive integer): "))
            if terms <= 0:
                print("Please enter a positive integer greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    sequence = fibonacci(terms)
    print(f"The first {terms} terms of the Fibonacci sequence are: {sequence}")

if __name__ == "__main__":
    fibonacci_generator()
