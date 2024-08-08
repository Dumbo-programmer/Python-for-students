def bmi_calculator():
    print("Welcome to the BMI Calculator!")
    
    while True:
        try:
            weight = float(input("Enter your weight in kg (or type 'exit' to quit): "))
            if weight <= 0:
                print("Weight must be a positive number. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number for weight.")
            continue
        
        try:
            height = float(input("Enter your height in meters (or type 'exit' to quit): "))
            if height <= 0:
                print("Height must be a positive number. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number for height.")
            continue

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            status = "Underweight"
        elif 18.5 <= bmi < 24.9:
            status = "Normal weight"
        elif 25 <= bmi < 29.9:
            status = "Overweight"
        else:
            status = "Obesity"

        print(f"Your BMI is: {bmi:.2f} ({status})")
        break

if __name__ == "__main__":
    bmi_calculator()
