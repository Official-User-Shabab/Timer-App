import tkinter as tk
from tkinter import ttk
import time
import threading
import pygame
import os
import sys

def resource_path(relative_path):

    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ming's Timer")
        self.root.geometry("600x400")
        self.root.attributes('-topmost', True)
        self.root.configure(bg="black")
      #-------
        self.running = False
        self.remaining = 0
        self.timer_thread = None

        pygame.mixer.init() # sound
        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.theme_use("default")
        style.configure("TCombobox",
                        fieldbackground="black",
                        background="black",
                        foreground="red",
                        selectbackground="black",
                        selectforeground="red",
                        arrowcolor="red")

        # Title
        title = tk.Label(self.root, text="TIMER", font=("Times New Roman", 24, 'bold'), bg="black", fg="red")
        title.pack(pady=(10, 5))

        # time pickers
        frame = tk.Frame(self.root, bg="black")
        frame.pack()

        self.hours_var = tk.StringVar(value='00')
        self.minutes_var = tk.StringVar(value='00')
        self.seconds_var = tk.StringVar(value='00')
#----------------------------------------------------------------
        self.hours = self.create_dropdown(frame, self.hours_var, 24)
        self.minutes = self.create_dropdown(frame, self.minutes_var, 60)
        self.seconds = self.create_dropdown(frame, self.seconds_var, 60)
#----------------------------------------------------------------
        self.hours.grid(row=0, column=0, padx=10)
        self.minutes.grid(row=0, column=1, padx=10)
        self.seconds.grid(row=0, column=2, padx=10)

        #Timer display
        self.display = tk.Label(self.root, text="00:00:00",
                                font=("Times New Roman", 48),
                                bg="black", fg="red")
        self.display.pack(pady=20)

        # buttons
        btn_frame = tk.Frame(self.root, bg="black")
        btn_frame.pack()

        btn_opts = {'width': 10, 'height': 2, 'bg': 'gray20', 'fg': 'white', 'activebackground': 'gray30', 'font': ("Times New Roman", 12)}

        tk.Button(btn_frame, text="Start / Restart", command=self.start_timer, **btn_opts).pack(side='left', padx=10)
        tk.Button(btn_frame, text="Stop", command=self.stop_timer, **btn_opts).pack(side='left', padx=10)
        tk.Button(btn_frame, text="Resume", command=self.resume_timer, **btn_opts).pack(side='left', padx=10)

        self.root.bind("<Button-1>", lambda e: self.root.focus())
      #----------------------------------------------------------------#----------------------------------------------------------------
    def create_dropdown(self, parent, var, max_val):
        values = [f"{i:02}" for i in range(max_val)]
        cb = ttk.Combobox(parent, textvariable=var, values=values, width=5,
                          font=("Times New Roman", 18), state="readonly", justify='center')
        cb.bind("<FocusIn>", lambda e: e.widget.selection_clear())
        return cb

  
    def start_timer(self):
        
        try:
            h = int(self.hours_var.get())
            m = int(self.minutes_var.get())
            s = int(self.seconds_var.get())
            self.remaining = h * 3600 + m * 60 + s
        except ValueError:
            return

        if self.remaining == 0:
            return

        self.running = True
        self.launch_timer_thread()
# stop
    def stop_timer(self):
        self.running = False
# resume
    def resume_timer(self):
        if self.remaining > 0 and not self.running:
            self.running = True
            self.launch_timer_thread()
# reset
    def reset_timer(self):
        self.running = False
        self.remaining = 0
        self.display.config(text="00:00:00")

    def launch_timer_thread(self):
        if self.timer_thread is None or not self.timer_thread.is_alive():
            self.timer_thread = threading.Thread(target=self.update_timer, daemon=True)
            self.timer_thread.start()

    def play_alarm(self):
        try:
            alarm_path = resource_path("alarm.wav")
            pygame.mixer.music.load(alarm_path)
            pygame.mixer.music.play()
        except Exception as e:
            print(f"Error playing sound: {e}")

    def update_timer(self):
        while self.remaining > 0 and self.running:
            mins, secs = divmod(self.remaining, 60)
            hrs, mins = divmod(mins, 60)
            self.display.config(text=f"{hrs:02}:{mins:02}:{secs:02}")
            time.sleep(1)
            self.remaining -= 1
        if self.remaining <= 0 and self.running:
            self.display.config(text="00:00:00")
            self.running = False
            threading.Thread(target=self.play_alarm, daemon=True).start()


if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
