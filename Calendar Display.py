#Calendar Display 
import calendar

def display_calendar():
    print("Welcome to the Calendar Display!")
    year = int(input("Enter the year: "))
    month = int(input("Enter the month (1-12): "))

    print(calendar.month(year, month))

if __name__ == "__main__":
    display_calendar()
