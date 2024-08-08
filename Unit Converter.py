def cm_to_inch(cm):
    return cm / 2.54

def inch_to_cm(inch):
    return inch * 2.54

def meter_to_feet(meter):
    return meter * 3.28084

def feet_to_meter(feet):
    return feet / 3.28084

def meter_to_yard(meter):
    return meter * 1.09361

def yard_to_meter(yard):
    return yard / 1.09361

def cm_to_meter(cm):
    return cm / 100

def meter_to_cm(meter):
    return meter * 100

def inch_to_meter(inch):
    return inch * 0.0254

def meter_to_inch(meter):
    return meter / 0.0254

def unit_converter():
    print("Welcome to the Unit Converter!")
    print("Available conversions:")
    print("1. cm to inch and vice versa")
    print("2. meter to feet and vice versa")
    print("3. meter to yard and vice versa")
    print("4. cm to meter and vice versa")
    print("5. inch to meter and vice versa")

    conversion_type = input("Select the conversion type (1-5): ")

    if conversion_type in ["1", "2", "3", "4", "5"]:
        unit_from = input("Enter the unit to convert from: ").lower()
        unit_to = input("Enter the unit to convert to: ").lower()
        value = float(input("Enter the value to convert: "))

        if conversion_type == "1":
            if unit_from == "cm" and unit_to == "inch":
                converted_value = cm_to_inch(value)
            elif unit_from == "inch" and unit_to == "cm":
                converted_value = inch_to_cm(value)
            else:
                print("Invalid units for conversion type 1")
                return

        elif conversion_type == "2":
            if unit_from == "meter" and unit_to == "feet":
                converted_value = meter_to_feet(value)
            elif unit_from == "feet" and unit_to == "meter":
                converted_value = feet_to_meter(value)
            else:
                print("Invalid units for conversion type 2")
                return

        elif conversion_type == "3":
            if unit_from == "meter" and unit_to == "yard":
                converted_value = meter_to_yard(value)
            elif unit_from == "yard" and unit_to == "meter":
                converted_value = yard_to_meter(value)
            else:
                print("Invalid units for conversion type 3")
                return

        elif conversion_type == "4":
            if unit_from == "cm" and unit_to == "meter":
                converted_value = cm_to_meter(value)
            elif unit_from == "meter" and unit_to == "cm":
                converted_value = meter_to_cm(value)
            else:
                print("Invalid units for conversion type 4")
                return

        elif conversion_type == "5":
            if unit_from == "inch" and unit_to == "meter":
                converted_value = inch_to_meter(value)
            elif unit_from == "meter" and unit_to == "inch":
                converted_value = meter_to_inch(value)
            else:
                print("Invalid units for conversion type 5")
                return

        print(f"The converted value is: {converted_value:.2f} {unit_to}")

    else:
        print("Invalid conversion type selected")

if __name__ == "__main__":
    unit_converter()
