import csv
import tkinter as tk
from tkinter import ttk
from Sorting import bubble_sort, merge_sort, quick_sort  # Importing from sorting.py

# Function to load products from a CSV file
def load_products(file_name):
    products = []
    with open(file_name, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['price'] = float(row['price'])
            row['rating'] = float(row['rating'])
            row['popularity'] = int(row['popularity'])
            products.append(row)
    products.sort(key=lambda x: x['name'])
    return products

# Function to display products in a treeview
def display_products(products):
    for product in products:
        tree.insert("", tk.END, values=(product['name'], product['price'], product['rating'], product['popularity']))
        
# Load products from a CSV file
products = load_products("products.csv")

# Function to sort products
def sort_products():
    sort_by = sort_by_combobox.get()
    order = order_combobox.get()
    
    if sort_by == "Price":
        sorted_products = merge_sort(products, "price")
    elif sort_by == "Rating":
        sorted_products = bubble_sort(products, "rating")
    elif sort_by == "Popularity":
        sorted_products = quick_sort(products, "popularity")
        
    if order == "High to Low":
        sorted_products = sorted_products[::-1]
        
    tree.delete(*tree.get_children())
    display_products(sorted_products)
    
# Create the main window
root = tk.Tk()
root.title("Product Catalog")

# Create a treeview to display products
tree = ttk.Treeview(root, columns=("Name", "Price", "Rating", "Popularity"))
tree.heading("#1", text="Name")
tree.heading("#2", text="Price")
tree.heading("#3", text="Rating")
tree.heading("#4", text="Popularity")
tree.pack() 

# Display products in the treeview
display_products(products) 

# Create a combobox to select the sorting criteria
sort_by_combobox = ttk.Combobox(root, values=["Price", "Rating", "Popularity"], state= "readonly")
sort_by_combobox.current(0) # Set default to Price
sort_by_combobox.pack(pady = 5)

order_combobox = ttk.Combobox(root, values=["Low to High", "High to Low"], state="readonly")
order_combobox.current(0)  # Set default to Ascending
order_combobox.pack(pady = 5)

# Create a button to sort products
sort_button = ttk.Button(root, text="Sort", command=sort_products)
sort_button.pack(pady = 10) # Add padding to the button

# Start the main event loop
root.mainloop()

