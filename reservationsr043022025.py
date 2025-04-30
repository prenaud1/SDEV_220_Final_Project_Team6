# Reservation Project File reservation.py copied 04/29/2025 at 10:14 am
"""
reservation.py
by Paul Renaud, LaToya Finnell, Sidart Rav, Kodi Righthouse
Allows a restaurant employee to add, edit, or remove existing reservations.
Keeps list of reservations, and list of customers.

"""

class Customer:
    """
    Each Customer has 3 fields: name, phone, and email.
    name is required. phone and email are optional but may be specified in order or by name.
    """
    def __init__(self, name, phone=None, email=None):
        self.name = name
        self.phone = phone
        if self.phone is None:
            self.phone = ""
        self.email = email
        if self.email is None:
            self.email = ""

    def __str__(self):
        return f"Customer: {self.name} | Phone: {self.phone} | Email {self.email}"

class Restaurant:
    """Contains info about the restaurant's open hours, and names of dining areas with number of seats.
    We might find a way to combine these (for example, outdoor seating only available during certain times)
    Not sure we need a class, but it may be useful for more than one location."""
    location = "Downtown location"
    hours = "M-F 11am - 9pm, Sat & Sun 11am - 10pm"
    seating = [{"Main area": 60},
               {"Private room": 12}]

    def __str__(self):
        # str only returns location name for now
        return f"{self.location}"

class Reservation:
    """
    Each Reservation has location, datetime, cust, party_size, seating, occasion, and notes.
    location is a Restaurant class.
    datetime is just a string for now.
    cust is a Customer class.
    seating, occasion, and notes are optional.
    """
    def __init__(self, location, datetime, cust, party_size, seating=None, occasion=None, notes=None):
        # init to empty string if not specified
        self.location = location
        self.datetime = datetime
        self.cust = cust
        self.party_size = party_size
        self.seating = seating
        if self.seating is None:
            self.seating = ""
        self.occasion = occasion
        if self.occasion is None:
            self.occation = ""
        self.notes = notes
        if self.notes is None:
            self.notes = ""

    def __str__(self):
        output_string = f"Location: {self.location}"
        output_string += f"Date/Time: {self.datetime}"
        output_string += f" | Name: {self.cust.name}"
        output_string += f" | Party Size:  {self.party_size}"
        output_string += f" | Seating: {self.seating}"
        output_string += f" | Occasion: {self.occasion}"
        output_string += f" | Notes: {self.notes}"
        return output_string


# init empty lists
# lists can contain any data, but these are for each of the classes
customers = []
restaurants = []
reservations = []


# code testing for debug
# will later load from file

# add sample customers
c = Customer("Smith", email="bsmith@domain.com")  # added in two lines
customers.append(c)
c = Customer("Gupta", phone="578-457-4082")
customers.append(c)
customers.append(Customer("Monet"))  # added directly in one line

# add sample restaurant
restaurants.append(Restaurant())
loc = restaurants[0]  # to save on typing

# add sample reservations
reservations.append(Reservation(loc, "12 noon", customers[0], 12, "Private Room", "30th birthday"))
reservations.append(Reservation(loc, "6pm", customers[1], 3, notes="Prefers near a window"))

def res_list():
    # main view, showing all reservations, and buttons for New Reservation, Change, Delete, or Exit program.
    # Possibly the delete option will be under the Change option.
    pass

def cus_list():
    # customer list, showing all customers, and buttons for New Customer, Change, Delete, or Return to res_list.
    # Delete option may be under the Change option.
    pass

import tkinter as tk
from tkinter import messagebox

def on_submit():
    # Runs if user tries to provide without providing additional information
    name = name_inp.get()
    if not name:
        messagebox.showerror('Name required', "This reservation must include a name")
        return

    number = number_inp.get()
    if not number:
        messagebox.showerror('Error', "Please enter the phone number!")
        return
    
    address = address_inp.get()
    #if not address:
    #    messagebox.showerror('Error', "Please enter your email address!")
    #    return

    size = size_var.get()
    seat = seat_var.get()
    time = time_var.get()
    occasion = occasion_var.get()
    
    if not time:
        messagebox.showerror('Error', 'Please select a time.')
        return
    
    #if not occasion:
    #    messagebox.showerror('Error', 'Please select at least one Special Occasion or none.')
    #    return
        
    # Create the order summary message
    message = f'Thank you! A reservation has been placed for: {name}. \n \n\
            The reservation will be for a party of {size} seated at the {seat} starting at {time}. \n'
    if number:
            message += f"We will text the phone number {number} when the table is ready. \n"
    if address:
            message += f"Confirmation will be sent to the email {address}. \n"
    
    #Create a new window to display the output message
    output_window = tk.Toplevel(root)
    output_window.title('Reservation Summary Confirmation')
 
    # Display the order summary message
    message_label = tk.Label(output_window, text=message)
    message_label.pack()

    # Add a button to close the output window
    close_button = tk.Button(output_window, text='Close', command=output_window.destroy)
    close_button.pack(pady=(0, 10))    # tuple for (top, bottom) padding

    # Set the size of the output window
    # output_window.geometry('550x115')

def on_clear():
    # Runs when user clicks clear, form will delete input
    name_inp.delete(0, tk.END)
    address_inp.delete(0, tk.END)
    number_inp.delete (0, tk.END)
    size_var.set('1')
    seat_var.set('None')
    occasion_var.set('None')
    time_var.set('')
    output_line.configure(text='')

def on_exit():
    # Runs when user clicks Exit button and confirms
    if messagebox.askokcancel('Exit', 'Are you sure you want to exit?'):
        root.destroy()


# Set colors and fonts here
fg_color = "black"
window_bg_color = "#0077aa"
button_bg_color = "white"
select_bg_color = "white"
label_font = ("", 14, "normal")  # tuple sent to Label font (family, size, bold/normal)
input_font = ("", 14, "normal")  # tuple sent to input font (family, size, bold/normal)
button_font = ("", 18, "normal")  # tuple sent to button font (family, size, bold/normal)
paddingx = 20
paddingy = 3

# Create the window title, size and color
root = tk.Tk()
root.title("New Reservation")
#root.geometry('600x515')
root.resizable(True, True)
root.configure(bg=window_bg_color)

r = 0  # to make it easier to rearrange items by moving the code

# Add widgets to the window

# Title
title = tk.Label(root, text="Welcome to A Nice Restaurant!",
                 font=('Times Roman', 24, "bold"),
                 bg=window_bg_color, fg=fg_color)
title.grid(row=r, column=0, columnspan=2, sticky="ew", padx=paddingx, pady=paddingy)

# User inputs name information
r += 1
name_label = tk.Label(root, text='Name')
name_label.configure(bg=window_bg_color, fg=fg_color, font=label_font)
name_label.grid(row=r, column=0, sticky='w', padx=paddingx, pady=paddingy)
name_inp = tk.Entry(root)
name_inp.configure(font=input_font)
name_inp.grid(row=r, column=1, sticky='we', padx=paddingx, pady=paddingy)

# User inputs phone number information
r += 1
number_label = tk.Label(root, text='Phone Number')
number_label.configure(bg=window_bg_color, fg=fg_color, font=label_font)
number_label.grid(row=r, column=0, sticky='w', padx=paddingx, pady=paddingy)
number_inp = tk.Entry(root)
number_inp.configure(font=input_font)
number_inp.grid(row=r, column=1, sticky='we', padx=paddingx, pady=paddingy)

# User inputs email address information
r += 1
address_label = tk.Label(root, text='Email Address')
address_label.configure(bg=window_bg_color, fg=fg_color, font=label_font)
address_label.grid(row=r, column=0, sticky='w', padx=paddingx, pady=paddingy)
address_inp = tk.Entry(root)
address_inp.configure(font=input_font)
address_inp.grid(row=r, column=1, sticky='we', padx=paddingx, pady=paddingy)

# Party Size Selection
r += 1
size_label = tk.Label(root, text='Select Party Size')
size_label.configure(bg=window_bg_color, fg=fg_color, font=label_font)
size_label.grid(row=r, column=0, sticky='w', padx=paddingx, pady=paddingy)
size_var = tk.StringVar(root, '1')
size_opts = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
size_inp = tk.OptionMenu(root, size_var, *size_opts)
size_inp.configure(bg=select_bg_color, font=input_font)
menu = root.nametowidget(size_inp.menuname)
menu.configure(font=input_font) # set the drop down menu font
size_inp.grid(row=r, column=1,sticky='we', padx=paddingx, pady=paddingy)

# Seating Selection
r += 1
seat_label = tk.Label(root, text='Select Seating Area')
seat_label.configure(bg=window_bg_color, fg=fg_color, font=label_font)
seat_label.grid(row=r, column=0, sticky='w', padx=paddingx, pady=paddingy)
seat_var = tk.StringVar(root, 'Main area')
seat_opts = ['Main area', 'Private Room', 'Patio', 'Roof Top View']
seat_inp = tk.OptionMenu(root, seat_var, *seat_opts)
seat_inp.configure(bg=select_bg_color, font=input_font)
menu = root.nametowidget(seat_inp.menuname)
menu.configure(font=input_font) # set the drop down menu font
seat_inp.grid(row=r, column=1, sticky='we', padx=paddingx, pady=paddingy)

# Date Selection
r += 1
from tkinter import ttk
from tkcalendar import Calendar
date_label = tk.Label(root, text='Select a date for reservation:')
date_label.configure(bg=window_bg_color, fg=fg_color, font=label_font)
date_label.grid(row=r, column=0, sticky='nw', padx=paddingx, pady=paddingy)
date_inp = Calendar(root, selectmode='day', date_pattern='yyyy-mm-dd')
date_inp.grid(row=r, column=1, sticky='e', padx=paddingx, pady=paddingy)

# Time Selection
r += 1
time_label = tk.Label(root, text='Select desired arrival time:')
time_label.configure(bg=window_bg_color, fg=fg_color, font=label_font)
time_label.grid(row=r, column=0, sticky='w', padx=paddingx, pady=paddingy)
time_var = tk.StringVar(root, '3:00 PM')
time_opts = ['3:00 PM', '3:30 PM', '4:00 PM', '4:30 PM', '5:00 PM', '5:30 PM', '6:00 PM', '6:30 PM', '7:00 PM', '7:30 PM', '8:00 PM', '8:30 PM', '9:00 PM']
time_inp = tk.OptionMenu(root, time_var, *time_opts)
time_inp.configure(bg=select_bg_color, font=input_font)
menu = root.nametowidget(time_inp.menuname)
menu.configure(font=input_font) # set the drop down menu font
time_inp.grid(row=r, column=1, sticky='we', padx=paddingx, pady=paddingy)

# Special Occasion Selection
r += 1
occasion_label = tk.Label(root, text='Select Special Occasion')
occasion_label.configure(bg=window_bg_color, fg=fg_color, font=label_font)
occasion_label.grid(row=r, column=0, sticky='w', padx=paddingx, pady=paddingy)
occasion_var = tk.StringVar(root, 'None')
occasion_opts = ['None', 'Birthday', 'Mothers Day', 'Fathers Day', 'Anniversary', 'Wedding', 'Graduation']
occasion_inp = tk.OptionMenu(root, occasion_var, *occasion_opts)
occasion_inp.configure(bg=select_bg_color, font=input_font)
menu = root.nametowidget(occasion_inp.menuname)
menu.configure(font=input_font) # set the drop down menu font
occasion_inp.grid(row=r, column=1, sticky='we', padx=paddingx, pady=paddingy)

# Extra notes
r += 1
occasion_label = tk.Label(root, text='Notes')
occasion_label.configure(bg=window_bg_color, fg=fg_color, font=label_font)
occasion_label.grid(row=r, column=0, sticky='nw', padx=paddingx, pady=paddingy)
notes_inp = tk.Text(root, height=3, width=30)
notes_inp.configure(bg=select_bg_color, font=input_font)
notes_inp.grid(row=r, column=1, sticky='we', padx=paddingx, pady=paddingy)

# add blank line before action buttons
r += 1
# Separator object
separator = ttk.Separator(root, orient='horizontal')
separator.grid(row=r, column=0, columnspan=2, sticky="ew", padx=paddingx, pady=paddingy*3)

# Clear button
clear_btn = tk.Button(root, text='Clear Reservation', command=on_clear)
clear_btn.configure(bg=button_bg_color, font=button_font)
clear_btn.grid(row=99, column=0, columnspan=1, sticky='NSEW', padx=paddingx, pady=paddingy)

# Checkout button
submit_btn = tk.Button(root, text='Submit', command=on_submit)
submit_btn.configure(bg=button_bg_color, font=button_font)
submit_btn.grid(row=99, column=1, columnspan=1, sticky='NSEW', padx=paddingx, pady=paddingy)

# Exit button
exit_btn = tk.Button(root, text='Exit', command=on_exit)
exit_btn.configure(bg=button_bg_color, font=button_font)
exit_btn.grid(row=100, column=0, columnspan=2, sticky='NSEW', padx=paddingx, pady=paddingy)

# Output message
output_line = tk.Label(root, text='', anchor='w', justify='left', pady=10)
error_line = tk.Label(root, text='', anchor='w', justify='left', pady=10)


root.mainloop()
import unittest
import tkinter as tk

class TestInputFields(unittest.TestCase):
    def setUp(self):
        """Initialize a Tkinter window for testing."""
        self.root = tk.Tk()
        self.name_inp = tk.Entry(self.root)
        self.number_inp = tk.Entry(self.root)
        self.address_inp = tk.Entry(self.root)

    def test_name_input(self):
        """Verify name input field works correctly."""
        self.name_inp.insert(0, "John Doe")
        self.assertEqual(self.name_inp.get(), "John Doe")

    def test_phone_input(self):
        """Verify phone number input field works correctly."""
        self.number_inp.insert(0, "123-456-7890")
        self.assertEqual(self.number_inp.get(), "123-456-7890")

    def test_address_input(self):
        """Verify email address input field works correctly."""
        self.address_inp.insert(0, "johndoe@example.com")
        self.assertEqual(self.address_inp.get(), "johndoe@example.com")

    def tearDown(self):
        """Destroy Tkinter window after tests."""
        self.root.destroy()

if __name__ == "__main__":
    unittest.main()
