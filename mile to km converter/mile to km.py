import tkinter as tk
import ttkbootstrap as ttk

def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    print(entry_int.get())
    OutputString.set(str(km_output))

# window
window = ttk.Window(themename='darkly')
window.title('mile to KM converter')
window.geometry('400x200')

# title
title_label = ttk.Label(master=window, text='miles to kilometers', font=('Bell MT', 20, 'bold italic'), foreground='red')
title_label.pack()

# input field
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int, foreground='sky blue')
button = ttk.Button(master=input_frame, text='convert', command=convert)
entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=10)

# output
OutputString = tk.StringVar()
output_label = ttk.Label(master=window, text='output', font=('Bell MT', 24, 'bold italic'), foreground='red', textvariable=OutputString)
output_label.pack(pady=5)

# run
window.mainloop()
