import tkinter as tk
from tkinter import messagebox
import time
import json

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0
        self.lap_times = []
        self.is_running = False
        self.is_paused = False

    def start(self):
        if not self.is_running:
            self.start_time = time.time() - self.elapsed_time
            self.is_running = True
            self.is_paused = False
            self.update_time()

    def stop(self):
        if self.is_running:
            self.elapsed_time = time.time() - self.start_time
            self.is_running = False
            self.is_paused = False

    def pause(self):
        if self.is_running and not self.is_paused:
            self.elapsed_time = time.time() - self.start_time
            self.is_paused = True

    def resume(self):
        if self.is_paused:
            self.start_time = time.time() - self.elapsed_time
            self.is_paused = False

    def lap(self):
        if self.is_running:
            self.lap_times.append(self.elapsed_time)
            return self.elapsed_time
        return None

    def get_formatted_time(self):
        elapsed = self.elapsed_time
        hours, remainder = divmod(elapsed, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{seconds:.2f}"

    def get_statistics(self):
        if not self.lap_times:
            return "No laps recorded."
        fastest_lap = min(self.lap_times)
        average_lap = sum(self.lap_times) / len(self.lap_times)
        return (f"Fastest Lap: {self.get_formatted_time_from_seconds(fastest_lap)}\n"
                f"Average Lap: {self.get_formatted_time_from_seconds(average_lap)}")

    def get_formatted_time_from_seconds(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{seconds:.2f}"

    def save_record(self, filename):
        record = {
            "elapsed_time": self.elapsed_time,
            "lap_times": self.lap_times
        }
        with open(filename, 'w') as file:
            json.dump(record, file)

    def load_record(self, filename):
        with open(filename, 'r') as file:
            record = json.load(file)
            self.elapsed_time = record["elapsed_time"]
            self.lap_times = record["lap_times"]

class StopwatchApp:
    def __init__(self, root):
        self.stopwatch = Stopwatch()
        self.root = root
        self.root.title("Stopwatch")

        self.time_display = tk.Label(root, text="00:00:00.00", font=("Helvetica", 48))
        self.time_display.pack()

        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack(side=tk.LEFT)

        self.pause_button = tk.Button(root, text="Pause", command=self.pause)
        self.pause_button.pack(side=tk.LEFT)

        self.resume_button = tk.Button(root, text="Resume", command=self.resume)
        self.resume_button.pack(side=tk.LEFT)

        self.lap_button = tk.Button(root, text="Lap", command=self.record_lap)
        self.lap_button.pack(side=tk.LEFT)

        self.save_button = tk.Button(root, text="Save", command=self.save_record)
        self.save_button.pack(side=tk.LEFT)

        self.load_button = tk.Button(root, text="Load", command=self.load_record)
        self.load_button.pack(side=tk.LEFT)

        self.stats_button = tk.Button(root, text="Statistics", command=self.show_statistics)
        self.stats_button.pack(side=tk.LEFT)

        self.lap_display = tk.Label(root, text="", font=("Helvetica", 14))
        self.lap_display.pack()

        self.update_time()

    def update_time(self):
        if self.stopwatch.is_running:
            self.stopwatch.elapsed_time = time.time() - self.stopwatch.start_time
            self.time_display.config(text=self.stopwatch.get_formatted_time())
        self.root.after(100, self.update_time)

    def start(self):
        self.stopwatch.start()

    def stop(self):
        self.stopwatch.stop()
        self.lap_display.config(text="")

    def pause(self):
        self.stopwatch.pause()

    def resume(self):
        self.stopwatch.resume()

    def record_lap(self):
        lap_time = self.stopwatch.lap()
        if lap_time is not None:
            lap_display_text = f"Lap Time: {self.stopwatch.get_formatted_time_from_seconds(lap_time)}"
            self.lap_display.config(text=lap_display_text)

    def save_record(self):
        self.stopwatch.save_record("stopwatch_record.json")
        messagebox.showinfo("Save Record", "Record saved successfully!")

    def load_record(self):
        self.stopwatch.load_record("stopwatch_record.json")
        messagebox.showinfo("Load Record", "Record loaded successfully!")

    def show_statistics(self):
        stats = self.stopwatch.get_statistics()
        messagebox.showinfo("Statistics", stats)

if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()
