import time

def countdown_timer():
    print("Welcome to the Countdown Timer!")
    
    while True:
        try:
            seconds = int(input("Enter the number of seconds (positive integer): "))
            if seconds < 1:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    while seconds:
        mins, secs = divmod(seconds, 60)
        time_format = f"{mins:02d}:{secs:02d}"
        print(f"Time remaining: {time_format}", end='\r')
        time.sleep(1)
        seconds -= 1
    
    print("\nTime's up!")

if __name__ == "__main__":
    countdown_timer()
