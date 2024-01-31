import tkinter as tk

import index as code
# Create the main application window
app = tk.Tk()
app.title("My GUI Application")

# Create a label
label = tk.Label(app, text="Click the button to call my_function")

# Create a button that calls my_function when clicked
button = tk.Button(app, text="Call Function", command=code)

# Pack the label and button into the window
label.pack(padx=10, pady=10)
button.pack(pady=10)

# Start the Tkinter event loop
app.mainloop()
