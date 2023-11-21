import time
import tkinter as tk
from tkinter import filedialog

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

if __name__ == "__main__":
    set_alarm_time()
    set_alarm_sound()
