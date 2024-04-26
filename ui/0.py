import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Hello World App")

label_hello = tk.Label(root, text="Hello")
label_hello.pack()

label_world = tk.Label(root, text="World!")
label_world.pack()

# Start the Tkinter event loop
root.mainloop()
