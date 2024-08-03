import time

def stopwatch():
    print("Welcome to the Stopwatch!")
    input("Press Enter to start...")
    start_time = time.time()

    input("Press Enter to stop...")
    elapsed_time = time.time() - start_time

    print(f"Elapsed time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    stopwatch()
