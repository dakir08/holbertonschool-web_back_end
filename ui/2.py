import tkinter as tk

def add_one():
    # Increment the current value by 1.
    current_value = int(value_label["text"])
    value_label.config(text=str(current_value + 1))

def subtract_one():
    # Decrement the current value by 1.
    current_value = int(value_label["text"])
    value_label.config(text=str(current_value - 1))

def double_value():
    # Double the current value.
    current_value = int(value_label["text"])
    value_label.config(text=str(current_value * 2))

def reset_value():
    # Reset the current value to 0.
    value_label.config(text="0")

# Create the main window
root = tk.Tk()
root.title("Value Modifier")

# Configure the grid layout
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Create buttons and assign them to the grid
add_button = tk.Button(root, text="Add one", command=add_one)
add_button.grid(row=0, column=0, sticky="nsew")

subtract_button = tk.Button(root, text="Subtract one", command=subtract_one)
subtract_button.grid(row=0, column=1, sticky="nsew")

double_button = tk.Button(root, text="Double", command=double_value)
double_button.grid(row=0, column=2, sticky="nsew")

# Create the value display label
value_label = tk.Label(root, text="0", font=("Helvetica", 14))
value_label.grid(row=1, column=0, columnspan=3)

# Create the reset button
reset_button = tk.Button(root, text="Reset", command=reset_value)
reset_button.grid(row=2, column=0, columnspan=3, sticky="nsew")

# Set grid row configurations for even distribution
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)

# Start the Tkinter event loop
root.mainloop()
