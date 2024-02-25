import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("Tony's Pizzeria")  # Set the title of the window

# Create frames for organizing content
menu_frame = tk.Frame(root)
menu_frame.pack()

# Function to load images
def load_image(image_path):
    return tk.PhotoImage(file=image_path)

# Load pizza images
cheese_image = load_image(r"C:\Users\jrenf\OneDrive\Pictures\cheese.png")
meat_lovers_image = load_image(r"C:\Users\jrenf\OneDrive\Pictures\meat.png")
pepperoni_image = load_image(r"C:\Users\jrenf\OneDrive\Pictures\pepperoni.png")
veggie_image = load_image(r"C:\Users\jrenf\OneDrive\Pictures\veggie.png")

# Add menu items
pizza_label = tk.Label(menu_frame, text="Menu")
pizza_label.pack()

# Callback functions for pizza buttons
def order_cheese():
    messagebox.showinfo("Order", "You ordered a Cheese Pizza")

def order_meat_lovers():
    messagebox.showinfo("Order", "You ordered a Meat Lover's Pizza")

def order_pepperoni():
    messagebox.showinfo("Order", "You ordered a Pepperoni Pizza")

def order_veggie():
    messagebox.showinfo("Order", "You ordered a Veggie Pizza")

# Add buttons for pizza options with images and bind them to callback functions
cheese_button = tk.Button(menu_frame, text="Cheese Pizza", image=cheese_image, compound=tk.LEFT, command=order_cheese)
cheese_button.pack()

meat_lovers_button = tk.Button(menu_frame, text="Meat Lover's Pizza", image=meat_lovers_image, compound=tk.LEFT, command=order_meat_lovers)
meat_lovers_button.pack()

pepperoni_button = tk.Button(menu_frame, text="Pepperoni Pizza", image=pepperoni_image, compound=tk.LEFT, command=order_pepperoni)
pepperoni_button.pack()

veggie_button = tk.Button(menu_frame, text="Veggie Pizza", image=veggie_image, compound=tk.LEFT, command=order_veggie)
veggie_button.pack()

# Function to handle exit button
def exit_program():
    if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
        root.destroy()

# Add exit button
exit_button = tk.Button(root, text="Exit", command=exit_program)
exit_button.pack()

# Run the application
root.mainloop()
