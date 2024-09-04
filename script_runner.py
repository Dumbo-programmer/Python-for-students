import os
import subprocess

# List of available scripts
scripts = [
    "BMI Calculator.py",
    "Calendar Display.py",
    "Countdown timer.py",
    "Currency Converter.py",
    "Dictionary Lookup.py",
    "Fibonacci Sequence Generator.py",
    "Flashcard Quiz.py",
    "Grade Calculator.py",
    "Math Quiz.py",
    "Name Generator.py",
    "Prime Number Checker.py",
    "Random PasswordGen.py",
    "Rock, Paper, Scissors Game.py",
    "Simple Calculator.py",
    "Simple Chatbot.py",
    "StopWatch.py",
    "TODO List.py",
    "Temperature Converter.py",
    "Unit Converter.py",
    "Word Counter.py",
]

def list_scripts():
    print("Available Scripts:")
    for index, script in enumerate(scripts, start=1):
        print(f"{index}. {script}")

def run_script(script_name):
    try:
        # Running the script
        subprocess.run(["python", script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running script {script_name}: {e}")

def main():
    while True:
        list_scripts()
        choice = input("\nEnter the number of the script to run (or 'q' to quit): ")
        
        if choice.lower() == 'q':
            print("Exiting the script runner. Goodbye!")
            break
        
        if choice.isdigit() and 1 <= int(choice) <= len(scripts):
            script_index = int(choice) - 1
            script_to_run = scripts[script_index]
            print(f"\nRunning script: {script_to_run}")
            run_script(script_to_run)
        else:
            print("Invalid choice. Please enter a number corresponding to a script or 'q' to quit.")

if __name__ == "__main__":
    main()
