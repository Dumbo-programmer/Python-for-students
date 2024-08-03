import time

def countdown_timer():
    print("Welcome to the Countdown Timer!")
    seconds = int(input("Enter the number of seconds: "))

    while seconds:
        print(f"{seconds} seconds remaining")
        time.sleep(1)
        seconds -= 1

    print("Time's up!")

if __name__ == "__main__":
    countdown_timer()
