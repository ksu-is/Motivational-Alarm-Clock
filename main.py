import time
import tkinter as tk

def display_clock():
    root = tk.Tk()
    root.title("Motivational Alarm Clock")
    root.geometry("400x200")
    root.config(bg="#000000")  # Set background color

    clock_label = tk.Label(root, font=('calibri', 60, 'bold'), background='#000000', foreground='white')
    clock_label.pack(pady=10)

    def update_clock():
        current_time = time.strftime('%H:%M:%S')
        clock_label['text'] = current_time
        clock_label.after(1000, update_clock)  # Update every second

    update_clock()  # Start updating the clock label

    root.mainloop()

if __name__ == "main":
    display_clock()