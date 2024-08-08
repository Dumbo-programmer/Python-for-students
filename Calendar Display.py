import calendar

def display_calendar():
    print("Welcome to the Calendar Display!")
    
    while True:
        try:
            year = int(input("Enter the year (e.g., 2024): "))
            if year < 1:
                print("Please enter a valid year greater than 0.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid year.")
            continue
        
        while True:
            try:
                month = int(input("Enter the month (1-12): "))
                if 1 <= month <= 12:
                    break
                else:
                    print("Please enter a valid month between 1 and 12.")
            except ValueError:
                print("Invalid input. Please enter a valid month.")
        
        print("\n", calendar.month(year, month))
        break

if __name__ == "__main__":
    display_calendar()
