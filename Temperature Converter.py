def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def temperature_converter():
    print("Welcome to the Temperature Converter!")
    temp = float(input("Enter the temperature: "))
    unit_from = input("Enter the unit of the temperature (C/F/K): ").upper()
    unit_to = input("Enter the unit to convert to (C/F/K): ").upper()

    if unit_from == unit_to:
        print(f"{temp}{unit_from} is the same as {temp}{unit_to}.")
        return

    if unit_from == 'C':
        if unit_to == 'F':
            converted_temp = celsius_to_fahrenheit(temp)
        elif unit_to == 'K':
            converted_temp = celsius_to_kelvin(temp)
        else:
            print("Invalid target unit")
            return

    elif unit_from == 'F':
        if unit_to == 'C':
            converted_temp = fahrenheit_to_celsius(temp)
        elif unit_to == 'K':
            converted_temp = fahrenheit_to_kelvin(temp)
        else:
            print("Invalid target unit")
            return

    elif unit_from == 'K':
        if unit_to == 'C':
            converted_temp = kelvin_to_celsius(temp)
        elif unit_to == 'F':
            converted_temp = kelvin_to_fahrenheit(temp)
        else:
            print("Invalid target unit")
            return

    else:
        print("Invalid source unit")
        return

    print(f"{temp}{unit_from} is {converted_temp:.2f}{unit_to}")

if __name__ == "__main__":
    temperature_converter()
