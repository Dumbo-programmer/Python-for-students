import math
import cmath
import json
import os
import sys

HISTORY_FILE = "calculator_history.json"

def perform_calculation(expression):
    """Evaluate the given mathematical expression safely."""
    try:
        # Define allowed functions and constants
        allowed_locals = {
            'sqrt': math.sqrt,
            'log': math.log,
            'exp': math.exp,
            'pi': math.pi,
            'e': math.e,
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'asin': math.asin,
            'acos': math.acos,
            'atan': math.atan,
            'degrees': math.degrees,
            'radians': math.radians,
            'abs': abs
        }

        # Use cmath for complex number support
        result = eval(expression, {"__builtins__": None}, allowed_locals)
        return result
    except ZeroDivisionError:
        raise ValueError("Cannot divide by zero.")
    except (SyntaxError, NameError):
        raise ValueError("Invalid expression.")
    except Exception as e:
        raise ValueError(f"An unexpected error occurred: {e}")

def save_history(history):
    """Save history to a file."""
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f)

def load_history():
    """Load history from a file."""
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as f:
            return json.load(f)
    return []

def calculator():
    """Run an advanced calculator program with history management."""
    print("Welcome to the Advanced Calculator!")
    history = load_history()

    while True:
        print("\nOptions:")
        print("1. Calculate an expression")
        print("2. View calculation history")
        print("3. Clear history")
        print("4. Save history")
        print("5. Load history")
        print("6. Quit")

        choice = input("Enter your choice (1/2/3/4/5/6): ").strip()

        if choice == '1':
            expression = input("Enter your expression (e.g., 2 * (3 + 4) / 5, sqrt(16), log10(100)): ").strip()
            try:
                result = perform_calculation(expression)
                if isinstance(result, complex):
                    print(f"The result is: {result:.2f} (complex number)")
                else:
                    print(f"The result is: {result:.2f}")
                history.append(f"{expression} = {result:.2f}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '2':
            if history:
                print("\nCalculation History:")
                for entry in history:
                    print(entry)
            else:
                print("No history available.")

        elif choice == '3':
            history.clear()
            print("History cleared.")

        elif choice == '4':
            save_history(history)
            print("History saved.")

        elif choice == '5':
            history = load_history()
            print("History loaded.")

        elif choice == '6':
            print("Thank you for using the calculator. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    # Command-line argument parsing
    if len(sys.argv) > 1:
        if sys.argv[1] == '--help':
            print("Usage: python calculator.py [option]")
            print("Options:")
            print("  --help       Show this help message")
            print("  --calculate  Calculate an expression directly (e.g., --calculate '2 * (3 + 4)')")
            sys.exit()
        elif sys.argv[1] == '--calculate' and len(sys.argv) == 3:
            try:
                result = perform_calculation(sys.argv[2])
                print(f"The result is: {result:.2f}")
            except ValueError as e:
                print(f"Error: {e}")
            sys.exit()
        else:
            print("Unknown option. Use '--help' for usage information.")
            sys.exit()
    
    calculator()
