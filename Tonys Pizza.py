import tkinter as tk
from tkinter import messagebox

class ShoppingCart:
    def __init__(self):
        """Initialize the shopping cart with an empty list to store items."""
        self.items = []

    def add_item(self, item, price):
        """Add an item to the shopping cart."""
        self.items.append((item, price))

    def remove_item(self, index):
        """Remove an item from the shopping cart."""
        del self.items[index]

    def clear_cart(self):
        """Clear all items from the shopping cart."""
        self.items = []

    def display_cart(self):
        """Generate a string representation of the items in the cart."""
        return "\n".join([f"{item[0]} - ${item[1]:.2f}" for item in self.items])

    def calculate_total(self):
        """Calculate the total cost of items in the shopping cart."""
        return sum([item[1] for item in self.items])

# Create an instance of the ShoppingCart class
cart = ShoppingCart()

# Create the main application window
root = tk.Tk()
root.title("Tony's Pizzeria")  # Set the title of the window

# Create frames for organizing content
menu_frame = tk.Frame(root)
menu_frame.pack()

# Function to load images
def load_image(image_path):
    """Load an image from a file path."""
    return tk.PhotoImage(file=image_path)

# Load pizza images
cheese_image = load_image(r"C:\Users\jrenf\OneDrive\Pictures\cheese.png")
meat_lovers_image = load_image(r"C:\Users\jrenf\OneDrive\Pictures\meat.png")
pepperoni_image = load_image(r"C:\Users\jrenf\OneDrive\Pictures\pepperoni.png")
veggie_image = load_image(r"C:\Users\jrenf\OneDrive\Pictures\veggie.png")

# Add menu items
pizza_label = tk.Label(menu_frame, text="Menu")
pizza_label.pack()

# Dictionary to hold pizza prices
pizza_prices = {"Small": 10, "Medium": 15, "Large": 20}

# Callback functions for pizza buttons
def order_pizza(pizza_type, price):
    """Callback function to add a pizza to the cart."""
    cart.add_item(f"{pizza_type} Pizza - {size_var.get()}", price)
    update_cart_display()

# Function to create pizza buttons
def create_pizza_button(pizza_type, image, price):
    """Create a button for a pizza option."""
    button = tk.Button(menu_frame, text=f"{pizza_type} Pizza - ${price:.2f}", image=image, compound=tk.LEFT,
                       command=lambda: order_pizza(pizza_type, price))
    button.pack()

# Add buttons for pizza options with images and bind them to callback functions
create_pizza_button("Cheese", cheese_image, pizza_prices["Small"])
create_pizza_button("Meat Lover's", meat_lovers_image, pizza_prices["Medium"])
create_pizza_button("Pepperoni", pepperoni_image, pizza_prices["Large"])
create_pizza_button("Veggie", veggie_image, pizza_prices["Medium"])

# Create frame for pizza customization
custom_frame = tk.Frame(root)
custom_frame.pack()

# Add radio buttons for pizza sizes
size_label = tk.Label(custom_frame, text="Select Pizza Size:")
size_label.grid(row=0, column=0, sticky=tk.W)

size_var = tk.StringVar()
size_var.set("Medium")  # Default size

sizes = list(pizza_prices.keys())
for i, size in enumerate(sizes):
    size_radio = tk.Radiobutton(custom_frame, text=size, variable=size_var, value=size)
    size_radio.grid(row=1, column=i, sticky=tk.W)

# Function to handle customizing the pizza
def customize_pizza():
    """Callback function to add a customized pizza to the cart."""
    size = size_var.get()
    pizza_type = "Create Your Own"
    selected_ingredients = [ingredient.get() for ingredient in ingredient_vars if ingredient.get() != ""]
    price = pizza_prices[size] + len(selected_ingredients) * 2  # Base price + $2 per additional ingredient
    pizza_description = f"{size} {pizza_type} Pizza"
    if selected_ingredients:
        pizza_description += " with: " + ", ".join(selected_ingredients)
    cart.add_item(pizza_description, price)
    update_cart_display()

# Add label and checkboxes for selecting ingredients
ingredient_label = tk.Label(custom_frame, text="Select Ingredients:")
ingredient_label.grid(row=2, column=0, sticky=tk.W)

ingredient_vars = []

ingredients = ["Peppers", "Olives", "Mushrooms", "Onions", "Pepperoni"]
for i, ingredient in enumerate(ingredients):
    ingredient_var = tk.StringVar()
    ingredient_check = tk.Checkbutton(custom_frame, text=ingredient, variable=ingredient_var, onvalue=ingredient)
    ingredient_check.grid(row=3, column=i, sticky=tk.W)
    ingredient_vars.append(ingredient_var)

# Add button to customize pizza
customize_button = tk.Button(custom_frame, text="Add to Cart", command=customize_pizza)
customize_button.grid(row=4, columnspan=len(sizes)+1)

# Function to update cart display
def update_cart_display():
    """Update the cart display with current items and total."""
    cart_display.config(text=cart.display_cart())
    total_label.config(text=f"Total: ${cart.calculate_total():.2f}")

# Add label for cart display
cart_label = tk.Label(root, text="Your Cart:")
cart_label.pack()

# Add label to display cart items
cart_display = tk.Label(root, text="")
cart_display.pack()

# Add label to display total
total_label = tk.Label(root, text="")
total_label.pack()

# Function to handle checkout
def checkout():
    """Process the checkout, display order details, and clear the cart."""
    if not cart.items:
        messagebox.showinfo("Checkout", "Your cart is empty!")
    else:
        message = f"You have ordered:\n{cart.display_cart()}\n\nTotal amount: ${cart.calculate_total():.2f}\n\nThank you for your order!"
        messagebox.showinfo("Checkout", message)
        cart.clear_cart()
        update_cart_display()

# Add button for checkout
checkout_button = tk.Button(root, text="Checkout", command=checkout)
checkout_button.pack()

# Run the application
root.mainloop()
