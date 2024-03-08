import tkinter as tk
from tkinter import messagebox

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def clear_cart(self):
        self.items = []

    def display_cart(self):
        return "\n".join(self.items)

cart = ShoppingCart()

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
    cart.add_item("Cheese Pizza")
    update_cart_display()

def order_meat_lovers():
    cart.add_item("Meat Lover's Pizza")
    update_cart_display()

def order_pepperoni():
    cart.add_item("Pepperoni Pizza")
    update_cart_display()

def order_veggie():
    cart.add_item("Veggie Pizza")
    update_cart_display()

# Add buttons for pizza options with images and bind them to callback functions
cheese_button = tk.Button(menu_frame, text="Cheese Pizza", image=cheese_image, compound=tk.LEFT, command=order_cheese)
cheese_button.pack()

meat_lovers_button = tk.Button(menu_frame, text="Meat Lover's Pizza", image=meat_lovers_image, compound=tk.LEFT, command=order_meat_lovers)
meat_lovers_button.pack()

pepperoni_button = tk.Button(menu_frame, text="Pepperoni Pizza", image=pepperoni_image, compound=tk.LEFT, command=order_pepperoni)
pepperoni_button.pack()

veggie_button = tk.Button(menu_frame, text="Veggie Pizza", image=veggie_image, compound=tk.LEFT, command=order_veggie)
veggie_button.pack()

# Create frame for pizza customization
custom_frame = tk.Frame(root)
custom_frame.pack()

# Add radio buttons for pizza sizes
size_label = tk.Label(custom_frame, text="Select Pizza Size:")
size_label.grid(row=0, column=0, sticky=tk.W)

size_var = tk.StringVar()
size_var.set("Medium")  # Default size

sizes = ["Small", "Medium", "Large"]
for i, size in enumerate(sizes):
    size_radio = tk.Radiobutton(custom_frame, text=size, variable=size_var, value=size)
    size_radio.grid(row=1, column=i, sticky=tk.W)

# Add check boxes for pizza toppings
toppings_label = tk.Label(custom_frame, text="Select Toppings:")
toppings_label.grid(row=2, column=0, sticky=tk.W)

toppings = ["Pepperoni", "Mushrooms", "Onions", "Peppers", "Olives"]
topping_vars = [tk.IntVar() for _ in toppings]
topping_checkboxes = []

for i, topping in enumerate(toppings):
    checkbox = tk.Checkbutton(custom_frame, text=topping, variable=topping_vars[i])
    checkbox.grid(row=3, column=i, sticky=tk.W)
    topping_checkboxes.append(checkbox)

# Function to handle customizing the pizza
def customize_pizza():
    size = size_var.get()
    selected_toppings = [toppings[i] for i, var in enumerate(topping_vars) if var.get() == 1]
    toppings_str = ", ".join(selected_toppings)
    cart.add_item(f"{size} pizza with {toppings_str}")
    update_cart_display()

# Add button to customize pizza
customize_button = tk.Button(custom_frame, text="Add to Cart", command=customize_pizza)
customize_button.grid(row=4, columnspan=len(sizes)+1)

# Function to update cart display
def update_cart_display():
    cart_display.config(text=cart.display_cart())

# Add label for cart display
cart_label = tk.Label(root, text="Your Cart:")
cart_label.pack()

# Add label to display cart items
cart_display = tk.Label(root, text="")
cart_display.pack()

# Function to handle checkout
def checkout():
    if not cart.items:
        messagebox.showinfo("Checkout", "Your cart is empty!")
    else:
        message = f"You have ordered:\n{cart.display_cart()}\n\nTotal amount: $10.00\n\nThank you for your order!"
        messagebox.showinfo("Checkout", message)
        cart.clear_cart()
        update_cart_display()

# Add button for checkout
checkout_button = tk.Button(root, text="Checkout", command=checkout)
checkout_button.pack()

# Run the application
root.mainloop()
