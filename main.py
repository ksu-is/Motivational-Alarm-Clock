import pygame
import time
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, colorchooser

def play_alarm_sound(alarm_sound):
    pygame.mixer.init()
    sound = pygame.mixer.Sound(alarm_sound)
    sound.play()

def motivational_message():
    messages = [
        "Rise and shine! A new day awaits.",
        "You've got this! Time to conquer the day.",
        "Today is full of possibilities. Make it count!",
        "Wake up with determination. Go to bed with satisfaction.",
    ]
    return messages

def show_message(message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Motivational Alarm", message)

def set_alarm_time():
    root = tk.Tk()
    root.title("Motivational Alarm Clock")
    root.geometry("400x250")
    root.config(bg="#282c34")  # Set default background color

    def change_background_color():
        color = colorchooser.askcolor()[1]
        root.config(bg=color)
        clock_label.config(bg=color)  # Update clock label background color
        entry.config(foreground="black")  # Set text color to black

    clock_label = tk.Label(root, font=('calibri', 60, 'bold'), background='#282c34', foreground='white')
    clock_label.pack(pady=10)

    alarm_time_var = tk.StringVar()
    alarm_time_var.set("07:00")

    entry = ttk.Entry(root, textvariable=alarm_time_var, font=("Helvetica", 14), style="TEntry", foreground="black")
    entry.pack(pady=10)

    def save_alarm_time():
        alarm_time = entry.get()
        alarm_time_var.set(alarm_time)
        root.destroy()

    save_button = ttk.Button(root, text="Save", command=save_alarm_time, style="TButton")
    save_button.pack(pady=10)

    color_button = ttk.Button(root, text="Change Color", command=change_background_color, style="TButton")
    color_button.pack(pady=10)

    style = ttk.Style()
    style.configure("TEntry", padding=10, relief="flat", background='#3e4452', foreground='black')
    style.map("TEntry", fieldbackground=[('active', '#3e4452')])

    style.configure("TButton", padding=6, relief="flat", background='#61dafb', foreground='white')
    style.map("TButton", background=[('active', '#4fa3d1')])

    def update_clock():
        current_time = time.strftime('%H:%M:%S')
        clock_label['text'] = current_time
        clock_label.after(1000, update_clock)  # Update every second

    update_clock()  # Start updating the clock label

    root.mainloop()

    return alarm_time_var.get()

def set_alarm_sound():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(title="Select Alarm Sound File", filetypes=[("Sound files", "*.wav;*.mp3")])

    return file_path

def main():
    print("Motivational Alarm Clock")

    alarm_time = set_alarm_time()
    print("Alarm set for:", alarm_time)

    alarm_sound = set_alarm_sound()
    print("Alarm sound set:", alarm_sound)

    while True:
        current_time = time.strftime("%H:%M")
        print("Current Time:", current_time)

        if current_time == alarm_time:
            print("Time to wake up!")
            play_alarm_sound(alarm_sound)

            for message in motivational_message():
                show_message(message)
                time.sleep(2)

            break

        time.sleep(60)

if __name__ == "__main__":
    main()