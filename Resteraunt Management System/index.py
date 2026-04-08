# 1) Import tkinter modules:
#    a) Import `tkinter as tk` to create the GUI window and canvas.
#    b) Import `ttk` for styled widgets like Frame, Label, Button, Combobox.
#    c) Import `messagebox` to show popup messages.
from tkinter import *
import tkinter as tk
from tkinter import ttk,messagebox

window=Tk()
window.geometry("800x600")
window.title("Restraunt Management System")

# 2) Create a class `RestaurantOrderManagement` to build and run the application.
class RestaurantOrderManagement:
    def __init__(self,root):
        self.root=window

# 3) Define the constructor `__init__(self, root)`:
#    a) Store the main window in `self.root`.
#    b) Set the window title to "Restaurant Management App".

# 4) Create a dictionary `self.menu_items` to store menu item names and their prices (in USD).
        self.menu_items={"Burger":2,"Drinks":1,"Chips":1.5,"Pizza":4,"Lunch":2}
        self.exchange_rate = 82

        self.setup_background(root)

        frame=ttk.Frame(root)
        frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)

# 5) Set an exchange rate `self.exchange_rate = 82`
#    to convert USD prices into INR when required.
        ttk.Label(frame,text="Restaurant Order Management",font=("arial",20,"bold")).grid(row=0,columnspan=3,padx=10,pady=10)
        self.menu_labels={}
        self.menu_quantities={}

# 6) Call `self.setup_background(root)` to load and display a background image.
        for i,(item,price) in enumerate(self.menu_items.items(),start=1):
            label=ttk.Label(frame,text=f"{item} (${price}):",font=("Arial",12))
            label.grid(row=i, column=0, padx=10, pady=5)
            self.menu_labels[item] = label

            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantities[item] = quantity_entry

# 7) Create a `ttk.Frame` and place it at the center of the window:
#    (This frame holds all the order widgets.)

# 8) Add a heading label "Restaurant Order Management" using `ttk.Label(...)`.

# 9) Create two empty dictionaries:
#    a) `self.menu_labels` to store label widgets for each menu item.
#    b) `self.menu_quantities` to store entry widgets for quantities.

# 10) Use a loop to create menu item rows:
#     a) For each item and price in `self.menu_items`:
#        i) Create a label showing item name and price.
#        ii) Create an entry box to input quantity.
#        iii) Store label references in `self.menu_labels`.
#        iv) Store entry references in `self.menu_quantities`.

# 11) Create a currency selection section:
#     a) Create a `StringVar` called `self.currency_var`.
#     b) Add a "Currency:" label.
#     c) Add a dropdown (`ttk.Combobox`) with options "USD" and "INR".
#     d) Set default selection to "USD".
#     e) Attach a trace to `self.currency_var` so when currency changes,
#        it automatically calls `self.update_menu_prices`.
        self.currency_var = tk.StringVar()

        ttk.Label(
            frame,
            text="Currency:",
            font=("Arial", 12)
        ).grid(row=len(self.menu_items) + 1,column=0,padx=10,pady=5)

        currency_dropdown = ttk.Combobox(
            frame,
            textvariable=self.currency_var,
            state="readonly",
            width=18,
            values=("USD", "INR")   # FIXED (must match logic)
        )
        currency_dropdown.grid(row=len(self.menu_items) + 1,column=1,padx=10,pady=5)
        currency_dropdown.current(0)

        self.currency_var.trace_add("write", self.update_menu_prices)

# 12) Add a "Place Order" button:
#     a) When clicked, it runs `self.place_order()`.
        order_button = ttk.Button(
            frame,
            text="Place Order",
            command=self.place_order
        )
        order_button.grid(row=len(self.menu_items) + 2,columnspan=3,padx=10,pady=10)

# 13) Define `setup_background(self, root)`:
    def setup_background(self, root):
        bg_width, bg_height = 800, 600
        canvas=tk.Canvas(root, width=bg_width, height=bg_height)
        canvas.pack()

        try:
            img = tk.PhotoImage(file="Bg.png")   # FIXED (your correct file + PNG supported)
            canvas.create_image(0, 0, anchor=tk.NW, image=img)
            canvas.image = img
        except:
            canvas.create_text(400, 300, text="Image not found", font=("Arial",20))

# 14) Define `update_menu_prices(self, *args)`:
    def update_menu_prices(self, *args):
        currency = self.currency_var.get()
        symbol = "₹" if currency == "INR" else "$"
        rate = self.exchange_rate if currency == "INR" else 1

        for item, label in self.menu_labels.items():
            price = self.menu_items[item] * rate
            label.config(text=f"{item} ({symbol}{price}):")

# 15) Define `place_order(self)`:
    def place_order(self):
        total_cost = 0
        order_summary = "Order Summary:\n"

        currency = self.currency_var.get()
        symbol = "₹" if currency == "INR" else "$"
        rate = self.exchange_rate if currency == "INR" else 1

        for item, entry in self.menu_quantities.items():
            quantity = entry.get()

            if quantity.isdigit():
                quantity = int(quantity)
                price = self.menu_items[item] * rate
                cost = quantity * price
                total_cost += cost

                if quantity > 0:
                    order_summary += (f"{item}: {quantity} x {symbol}{price} = {symbol}{cost}\n")

        if total_cost > 0:
            order_summary += f"\nTotal Cost: {symbol}{total_cost}"
            messagebox.showinfo("Order Placed", order_summary)
        else:
            messagebox.showerror("Error", "Please order at least one item.")

# 16) In the main block
if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantOrderManagement(root)
    root.geometry("800x600")
    root.mainloop()