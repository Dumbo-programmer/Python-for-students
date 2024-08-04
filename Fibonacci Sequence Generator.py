#Fibonacci Sequence Generator
def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def fibonacci_generator():
    print("Welcome to the Fibonacci Sequence Generator!")
    terms = int(input("Enter the number of terms: "))

    sequence = fibonacci(terms)
    print(f"The first {terms} terms of the Fibonacci sequence are: {sequence}")

if __name__ == "__main__":
    fibonacci_generator()
