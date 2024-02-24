import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Tony's Pizzeria")  # Set the title of the window
# Create and add widgets
welcome_label = tk.Label(root, text="Welcome to Tony's!")
welcome_label.pack()

# Create frames for organizing content
menu_frame = tk.Frame(root)
menu_frame.pack()

# Add menu items
pizza_label = tk.Label(menu_frame, text="Menu")
pizza_label.pack()

# Add buttons for pizza options
pepperoni_button = tk.Button(menu_frame, text="Pepperoni Pizza")
pepperoni_button.pack()

# Add more buttons for other pizza options
cheese_button = tk.Button(menu_frame, text="Cheese Pizza")
cheese_button.pack()

# Add more buttons for other pizza options
veggie_button = tk.Button(menu_frame, text="Veggie Pizza")
veggie_button.pack()

# Add more buttons for other pizza options
meat_lovers_button = tk.Button(menu_frame, text="Meat Lover's Pizza")
meat_lovers_button.pack()

def order_pizza(pizza_type):
    # Logic for ordering the selected pizza type
    pass

def show_pizza_details(pizza_type):
    # Logic for showing details of the selected pizza type
    pass

# Bind buttons to event handlers
pepperoni_button.config(command=lambda: show_pizza_details("Pepperoni"))
# Add bindings for other pizza buttons
cheese_button.config(command=lambda: show_pizza_details("Cheese"))
# Add bindings for other pizza buttons
veggie_button.config(command=lambda: show_pizza_details("Veggie"))
# Add bindings for other pizza buttons
meat_lovers_button.config(command=lambda: show_pizza_details("Meat Lover's"))

# Run the application
root.mainloop()

