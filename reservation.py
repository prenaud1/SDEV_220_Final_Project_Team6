"""
reservation.py
by Paul Renaud, LaToya Finnell, Sidart Rav, Kodi Righthouse
Allows a restaurant employee to add, edit, or remove existing reservations.
Keeps list of reservations, and list of customers.

"""

occasion_list = ['None', 'Birthday', 'Mothers Day', 'Fathers Day', 'Anniversary', 'Wedding', 'Graduation']

# Set colors and fonts here
fg_color = "black"
window_bg_color = "#0077aa"
button_bg_color = "white"
select_bg_color = "white"
label_font = ("", 14, "normal")  # tuple sent to Label font (family, size, bold/normal)
input_font = ("", 14, "normal")  # tuple sent to input font (family, size, bold/normal)
button_font = ("", 18, "normal")  # tuple sent to button font (family, size, bold/normal)
paddingx = 20  # left and right padding for each element
paddingy = 3   # top and bottom padding for each element


from datetime import datetime

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
    seating = {'Main area' : 60,
              'Private Room' : 12,
              'Patio' : 18,
              'Roof Top View': 8
              }

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
    def __init__(self, location, date, time, cust, party_size, seating=None, occasion=None, notes=None):
        # init to empty string if not specified
        self.location = location
        self.date = date
        self.time = time
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
        output_string += f"Date: {self.date}"
        output_string += f"Time: {self.time}"
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

# first customer (customers[0]) is new customer field
customers.append(Customer("(new customer)"))

# code testing for debug
# will later load from file

# add sample customers
c = Customer("Smith", phone="555-0123", email="bsmith@domain.com")  # added in two lines
customers.append(c)
c = Customer("Gupta", phone="578-457-4082")
customers.append(c)
customers.append(Customer("Monet"))  # added directly in one line

# add sample restaurant
restaurants.append(Restaurant())
loc = restaurants[0]  # to save on typing

# add sample reservations
reservations.append(Reservation(loc, "3/5/2025", "3:00 PM", customers[1], 12, "Private Room", notes="30th birthday"))
reservations.append(Reservation(loc, "5,5,2025", "6pm", customers[2], 3, notes="Prefers near a window"))

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


def edit_res(res=None):
    # Shows fields to edit or add a reservation.
    # If sent an exsiting reservation, will be prefilled with that info.
    # Otherwise, will initilize to a blank reservation.
    # Returns a reservation (new or edited), or boolean False if cancelled. (These not yet implemented)
    
    def on_submit():

        # Runs if user tries to provide without providing additional information
        name = name_inp.get()
        if not name:
            messagebox.showerror('Name required', "This reservation must include a name")
            return

        phone = phone_inp.get()
        if not phone:
            messagebox.showerror('Phone required', "Please enter your phone number")
            return
        
        address = address_inp.get()
        #if not address:
        #    messagebox.showerror('Error', "Please enter your email address!")
        #    return

        party_size = party_size_var.get()
        seat = seat_var.get()
        date = date_inp.get_date()
        time = time_var.get()
        occasion = occasion_var.get()
        notes = notes_inp.get("1.0", tk.END)

        # line for debugging
        messagebox.showinfo("Vars", f"{name=}, {phone=}, {address=}, {party_size=}, {seat=}, {date=}, {time=}, {occasion=}, {notes=}")
                
        # Create the order summary message
        message = f'Thank you! A reservation has beel placed for: {name}. \n \n\
                The reservation will be for a party of {party_size} seated at the {seat} starting at {time}. \n'
        if phone:
                message += f"We will text the phone number {phone} when the table is ready. \n"
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
        return

    def on_clear():
        # Runs when user clicks clear, form will delete input
        name_inp.delete(0, tk.END)
        address_inp.delete(0, tk.END)
        phone_inp.delete (0, tk.END)
        party_size_var.set('1')
        seat_var.set('Main area')
        occasion_var.set('None')
        for time_var in time_var:
            time_var.set(False)
        output_line.configure(text='')


    def on_exit():
        # Runs when user clicks Exit button and confirms
        if messagebox.askokcancel('Exit', 'Are you sure you want to exit?'):
            root.destroy()
            return False


    # begin with a blank reservation. If one sent as arg, prefill fields.
    this_res = Reservation(loc, datetime.today(), "3:00 PM", customers[0], 1)
    if res:
        this_res = res    


    # Create the window title, size and color
    root = tk.Tk()
    root.title("Reservation Info")
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
    def on_focus(event):
        # if name is (new customer) auto-select it to overwrite
        if name_inp.get() == "(new customer)":
            name_inp.select_range(0, tk.END)    
    r += 1
    name_label = tk.Label(root, text='Name')
    name_label.configure(bg=window_bg_color, fg=fg_color, font=label_font)
    name_label.grid(row=r, column=0, sticky='w', padx=paddingx, pady=paddingy)
    name_inp = tk.Entry(root)
    name_inp.bind("<FocusIn>", on_focus)  # to check if new customer
    name_inp.insert(0, this_res.cust.name)  # prefill
    name_inp.configure(font=input_font)
    name_inp.grid(row=r, column=1, sticky='we', padx=paddingx, pady=paddingy)

    # User inputs phone number information
    r += 1
    phone_label = tk.Label(root, text='Phone Number')
    phone_label.configure(bg=window_bg_color, fg=fg_color, font=label_font)
    phone_label.grid(row=r, column=0, sticky='w', padx=paddingx, pady=paddingy)
    phone_inp = tk.Entry(root)
    phone_inp.insert(0, this_res.cust.phone)  # prefill
    phone_inp.configure(font=input_font)
    phone_inp.grid(row=r, column=1, sticky='we', padx=paddingx, pady=paddingy)

    # User inputs email address information
    r += 1
    address_label = tk.Label(root, text='Email Address')
    address_label.configure(bg=window_bg_color, fg=fg_color, font=label_font)
    address_label.grid(row=r, column=0, sticky='w', padx=paddingx, pady=paddingy)
    address_inp = tk.Entry(root)
    address_inp.insert(0, this_res.cust.email)  # prefill
    address_inp.configure(font=input_font)
    address_inp.grid(row=r, column=1, sticky='we', padx=paddingx, pady=paddingy)

    # Party Size Selection
    r += 1
    party_size_label = tk.Label(root, text='Select Party Size')
    party_size_label.configure(bg=window_bg_color, fg=fg_color, font=label_font)
    party_size_label.grid(row=r, column=0, sticky='w', padx=paddingx, pady=paddingy)
    party_size_opts = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    party_size_var = tk.StringVar(root, party_size_opts[0])
    party_size_inp = tk.OptionMenu(root, party_size_var, *party_size_opts)
    # party_size_var = this_res.party_size  # prefill
    party_size_inp.configure(bg=select_bg_color, font=input_font)
    menu = root.nametowidget(party_size_inp.menuname)
    menu.configure(font=input_font) # set the drop down menu font
    party_size_inp.grid(row=r, column=1,sticky='we', padx=paddingx, pady=paddingy)

    # Seating Selection
    r += 1
    seat_label = tk.Label(root, text='Select Seating Area')
    seat_label.configure(bg=window_bg_color, fg=fg_color, font=label_font)
    seat_label.grid(row=r, column=0, sticky='w', padx=paddingx, pady=paddingy)
    seat_opts = list(loc.seating.keys())   # pulled from restaurant location info
    seat_var = tk.StringVar(root, seat_opts[0])   # default to first option
    seat_inp = tk.OptionMenu(root, seat_var, *seat_opts)
    # seat_var = this_res.seating  # prefill
    seat_inp.configure(bg=select_bg_color, font=input_font)
    menu = root.nametowidget(seat_inp.menuname)
    menu.configure(font=input_font) # set the drop down menu font
    seat_inp.grid(row=r, column=1, sticky='we', padx=paddingx, pady=paddingy)

    # Date Selection
    r += 1
    from tkinter import ttk
    from tkcalendar import Calendar
    from tkcalendar import DateEntry
    date_label = tk.Label(root, text='Select a date for reservation:')
    date_label.configure(bg=window_bg_color, fg=fg_color, font=label_font)
    date_label.grid(row=r, column=0, sticky='nw', padx=paddingx, pady=paddingy)
    # date_inp = Calendar(root, selectmode='day', date_pattern='yyyy-mm-dd')
    # date = datetime.strptime(this_res.date, "%m,%d,%Y").date()  # prefill
    date_inp = DateEntry(root, firstweekday="sunday", date_pattern='yyyy-mm-dd', showweeknumbers=False, weekendbackground="white", weekendforeground="black") #, startdate=date)
    date_inp.configure(font=input_font)
    date_inp.grid(row=r, column=1, sticky='e', padx=paddingx, pady=paddingy)

    # Time Selection
    r += 1
    time_label = tk.Label(root, text='Select desired arrival time:')
    time_label.configure(bg=window_bg_color, fg=fg_color, font=label_font)
    time_label.grid(row=r, column=0, sticky='w', padx=paddingx, pady=paddingy)
    time_opts = ['3:00 PM', '3:30 PM', '4:00 PM', '4:30 PM', '5:00 PM', '5:30 PM', '6:00 PM', '6:30 PM', '7:00 PM', '7:30 PM', '8:00 PM', '8:30 PM', '9:00 PM']
    time_var = tk.StringVar(root, time_opts[0])
    # time_var = this_res.time  # prefill
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
    occasion_opts = occasion_list
    occasion_var = tk.StringVar(root, occasion_opts[0])
    occasion_inp = tk.OptionMenu(root, occasion_var, *occasion_opts)
    # if this_res.occasion != "":
        # occasion_inp = this_res.occasion   # prefill
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
    notes_inp.insert("1.0", this_res.notes)   # prefill
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

if __name__ == "__main__":
    # edit_res(reservations[0])  # to test with prefilled info
    edit_res()                   # to test with new customer info. Optionally, make new_res().

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

"""
if __name__ == "__main__":
    unittest.main()
"""
