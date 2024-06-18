import tkinter as tk
from time import strftime

def display_time():
    current_time = strftime('%H:%M:%S %p')
    label.config(text=current_time)
    label.after(1000, display_time)  # Update time every second

root = tk.Tk()
root.title('Simple Clock')

label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label.pack(anchor='center')

display_time()

root.mainloop()
