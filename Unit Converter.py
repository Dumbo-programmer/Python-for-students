def unit_converter():
    print("Welcome to the Unit Converter!")
    unit_from = input("Enter the unit to convert from (cm/inch): ").lower()
    unit_to = input("Enter the unit to convert to (cm/inch): ").lower()
    value = float(input("Enter the value to convert: "))

    if unit_from == "cm" and unit_to == "inch":
        converted_value = value / 2.54
    elif unit_from == "inch" and unit_to == "cm":
        converted_value = value * 2.54
    else:
        print("Invalid units")
        return

    print(f"The converted value is: {converted_value} {unit_to}")

if __name__ == "__main__":
    unit_converter()
