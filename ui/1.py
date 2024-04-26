import tkinter as tk

def submit_name():
    # Get the name from the entry widget and update the greeting label.
    name = name_entry.get()
    greeting_label.config(text=f"Hello {name}")

def clear_text():
    # Clear the text entry widget and reset the greeting label.
    name_entry.delete(0, tk.END)
    greeting_label.config(text="Hello")

# Create the main window
root = tk.Tk()
root.title("Greeting App")

# Create the 'Enter your name:' label
prompt_label = tk.Label(root, text="Enter your name:")
prompt_label.pack()

# Create the text entry widget for name input
name_entry = tk.Entry(root)
name_entry.pack()

# Create the label for displaying the greeting
greeting_label = tk.Label(root, text="Hello")
greeting_label.pack()

# Create the 'Submit' button
submit_button = tk.Button(root, text="Submit", command=submit_name)
submit_button.pack()

# Create the 'Clear' button
clear_button = tk.Button(root, text="Clear", command=clear_text)
clear_button.pack()

# Run the application
root.mainloop()
