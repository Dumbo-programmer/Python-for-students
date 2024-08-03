#Temperature Converter
def temperature_converter():
    print("Welcome to the Temperature Converter!")
    temp = float(input("Enter the temperature: "))
    unit = input("Enter the unit (C/F): ").upper()

    if unit == 'C':
        converted_temp = (temp * 9/5) + 32
        print(f"{temp}C is {converted_temp}F")
    elif unit == 'F':
        converted_temp = (temp - 32) * 5/9
        print(f"{temp}F is {converted_temp}C")
    else:
        print("Invalid unit")

if __name__ == "__main__":
    temperature_converter()