import time
import tkinter as tk
from tkinter import filedialog, messagebox
import pygame

def set_alarm_time():
    root = tk.Tk()
    root.title("Motivational Alarm Clock")
    root.geometry("400x200")
    root.config(bg="#000000")  # Set background color

    clock_label = tk.Label(root, font=('calibri', 60, 'bold'), background='#000000', foreground='white')
    clock_label.pack(pady=10)

    alarm_time_var = tk.StringVar()
    alarm_time_var.set("07:00")

    entry = tk.Entry(root, textvariable=alarm_time_var, font=("Helvetica", 14), bd=5, relief=tk.GROOVE, width=20)
    entry.pack(pady=10)

    def save_alarm_time():
        alarm_time = entry.get()
        alarm_time_var.set(alarm_time)
        root.destroy()

    save_button = tk.Button(root, text="Save", command=save_alarm_time, font=("Helvetica", 14), bg="#3f704d", fg="white", bd=5, relief=tk.RIDGE)
    save_button.pack(pady=10)

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

    file_path = filedialog.askopenfilename(title="Select Alarm Sound File", filetypes=[("Sound files", ".wav;.mp3")])

    return file_path
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
   
