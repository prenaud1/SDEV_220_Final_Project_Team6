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
button_font = ("", 14, "normal")  # tuple sent to button font (family, size, bold/normal)
paddingx = 20  # left and right padding for each element in edit window
paddingy = 3   # top and bottom padding for each element in edit window


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import json
RES_FILE = "reservations.json"
CUS_FILE = "customers.json"
USING_FILES = True  # change to create sample data if not loading from a file

class Customer:
    """
    Each Customer has 3 fields: name, phone, and email.
    name is required. phone and email are optional but may be specified in order or by name.
    """
    def __init__(self, name, phone="", email=""):
        self.name = name
        self.phone = phone
        self.email = email
        
    def __str__(self):
        return f"Customer: {self.name} | Phone: {self.phone} | Email {self.email}"
    
    def to_dict(self):
        # converts a single customer to dictionary format for saving
        return {"name": self.name,
                "phone": self.phone,
                "email": self.email
                }

    @classmethod
    def from_dict(cls, data):
        # create a single customer from dictionary (cls basically calls Customer.__init__)
        return cls(data["name"],
                data["phone"],
                data["email"]
        )

class Restaurant:
    """Contains info about the restaurant's open hours, and names of dining areas with number of seats.
    We might find a way to combine these (for example, outdoor seating only available during certain times)
    Not sure we need a class, but it may be useful for more than one location."""
    name = "Downtown location"
    open_time = "11:00"
    close_time = "22:00"
    total_tables = 30
    seating = {'Main area' : 60,
              'Private Room' : 12,
              'Patio' : 18,
              'Roof Top View': 8
              }

    def __str__(self):
        # str only returns location name for now
        return f"{self.name}"

class Reservation:
    """
    Each Reservation has location, datetime, cust, party_size, seating, occasion, and notes.
    location is a Restaurant class.
    datetime is just a string for now.
    cust is a Customer class.
    seating, occasion, and notes are optional.
    """
    def __init__(self, location, date, time, cust, tables=1, party_size=1, seating="", occasion="None", notes=""):
        # init to empty string if not specified
        self.location = location
        self.date = date
        self.time = time
        self.cust = cust
        self.tables = tables
        self.party_size = party_size
        self.seating = seating
        self.occasion = occasion
        self.notes = notes

    def to_dict(self):
        # converts a single reservation to dictionary format for saving
        return {"location": self.location.name,
                "date": self.date,
                "time": self.time,
                "cust": self.cust.to_dict(),
                "tables": self.tables,
                "party_size": self.party_size,
                "seating": self.seating,
                "occasion": self.occasion,
                "notes": self.notes
                }

    @classmethod
    def from_dict(cls, data):
        # create a single reservation from dictionary (cls calls Reservation.__init__)
        return cls(data["location"],
                data["date"],
                data["time"],
                data["cust"],
                data["tables"],
                data["party_size"],
                data["seating"],
                data["occasion"],
                data["notes"]
        )
                
    def __str__(self):
        output_string = f"Location: {self.location}"
        output_string += f" | Date: {self.date}"
        output_string += f" | Time: {self.time}"
        output_string += f" | Name: {self.cust.name}"
        output_string += f" | Tables: {self.tables}"
        output_string += f" | Party Size:  {self.party_size}"
        output_string += f" | Seating: {self.seating}"
        output_string += f" | Occasion: {self.occasion}"
        output_string += f" | Notes: {self.notes}"
        return output_string


# init empty lists
# lists can contain any data, but these are for each of the classes
restaurants = []

# add sample restaurant
restaurants.append(Restaurant())
loc = restaurants[0]  # We only have one restaurant, so use this to save on typing.

if not USING_FILES:
    global customers, reservations
    customers = []
    reservations = []
    # add sample customers
    c = Customer("Smith", phone="555-0123", email="bsmith@domain.com")  # added in two lines
    customers.append(c)
    c = Customer("Gupta", phone="578-457-4082")
    customers.append(c)
    customers.append(Customer("Monet"))  # added directly in one line
    # add sample reservations
    reservations.append(Reservation(loc, "2025-03-05", "15:00", customers[1], tables=3, party_size=12, seating="Private Room", notes="30th birthday"))
    reservations.append(Reservation(loc, "2025-05-05", "18:00", customers[2], tables=1, party_size=3, notes="Prefers near a window"))

def save_customers():
    """Save customers to a file."""
    with open(CUS_FILE, "w") as f:
        json.dump([cus.to_dict() for cus in customers], f)

def load_customers():
    """Load customers from a file."""
    global customers
    try:
        with open(CUS_FILE, "r") as f:
            data = json.load(f)
            customers = [Customer.from_dict(cus) for cus in data]
    except (FileNotFoundError, json.JSONDecodeError):
        customers = []


def save_reservations():
    """Save reservations to a file."""
    with open(RES_FILE, "w") as f:
        json.dump([res.to_dict() for res in reservations], f)

def load_reservations():
    """Load reservations from a file."""
    global reservations
    global customers

    def find_customer_index(customers, name, phone, email):
        # looks for matches of name, phone, email and returns index of matching customer
        for index, cust in enumerate(customers):
            if cust.name==name and cust.phone==phone and cust.email==email:
                return index
        return -1

    try:
        with open(RES_FILE, "r") as f:
            data = json.load(f)
        reservations = []
        for item in data:
            cust_data = item["cust"]
            index = find_customer_index(customers, cust_data["name"], cust_data["phone"], cust_data["email"])
            if index == -1:  # no customer, create new one
                customers.append(Customer.from_dict(cust_data))
                index = len(customers) - 1  # index of the new customer
            reservations.append(Reservation(loc,
                                            item["date"],
                                            item["time"],
                                            customers[index],
                                            item["tables"],
                                            item["party_size"],
                                            item["seating"],
                                            item["occasion"],
                                            item["notes"],
                                            )
                                )

    except (FileNotFoundError, json.JSONDecodeError):
        reservations = []


if USING_FILES:
    load_customers()
    load_reservations()

def edit_res(index=None, update_callback=None):
    # Shows fields to edit or add a reservation.
    # If sent an exsiting reservation, will be prefilled with that info.
    # Otherwise, will initilize to a blank reservation.
    # Returns a reservation (new or edited), or boolean False if cancelled. (These not yet implemented)
    if index is None or len(reservations) == 0:
        res = None
    else:
        if index < 0:
            index = 0
        if index >= len(reservations):
            index = len(reservations) - 1
        res = reservations[index]
    
    def validate_time(time_str):
        # Don't allow reservation if restaurant is closed.
        try:
            time_obj = datetime.strptime(time_str, "%H:%M")
            if loc.open_time <= time_obj.hour < loc.close_time:
                return True
            else:
                messagebox.showerror(f"Invalid Time", "Restaurant is only open from {loc.open_time} to {loc.close_time}.")
                return False
        except ValueError:
            messagebox.showerror("Invalid Time Format", "Please enter time in HH:MM format (24-hour clock).")
            return False

    def tables_available(date_str, time_str, requested_tables):
        """Check if requested tables exceed availability for the given 30-minute window."""
        time_obj = datetime.strptime(time_str, "%H:%M")
        start_range = time_obj.strftime("%H:%M")
        end_range = (time_obj.replace(minute=time_obj.minute + 30)).strftime("%H:%M")
        date_range = datetime.strptime(date_str, "yyyy-mm-dd")

        # Count tables reserved in this 30-minute window
        tables_used = 0
        for i in range(len(reservations)):
            if reservations[i].date == date_range:
                if start_range <= reservations[i].time < end_range:
                    tables_used += reservations[i].tables

        if tables_used + requested_tables > loc.total_tables:
            messagebox.showerror("No Tables Available", "Too many tables reserved in this time window.")
            return False

        return True


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

        # convert tables to integer. Silently defaults to 1 if invalid.
        try:
            tables = int(tables_inp.get())
        except:
            tables = 1
        if tables <= 0:
            tables = 1
        
        party_size = party_size_var.get()
        seat = seat_var.get()
        date = date_inp.get_date()
        time = time_var.get()
        occasion = occasion_var.get()
        notes = notes_inp.get("1.0", tk.END)

        # line for debugging
        # messagebox.showinfo("Vars", f"{name=}, {phone=}, {address=}, {tables=}, {party_size=}, {seat=}, {date=}, {time=}, {occasion=}, {notes=}")
        
        if isinstance(date, datetime):
            date = date.isoformat()  # Convert datetime to string
        elif not isinstance(date, str):
            date = str(date)  # Handle unexpected cases

        # check for exising customer, and create new if not found
        def find_customer_index(customers, name, phone, address):
            # looks for matches of name, phone, email and returns index of matching customer
            for index, cust in enumerate(customers):
                if cust.name==name and cust.phone==phone and cust.email==address:
                    return index
            return -1
        index = find_customer_index(customers, name, phone, address)
        if index == -1:  # no customer, create new one
            customers.append(Customer(name, phone, address))


        if res is None:   # create new
            reservations.append(Reservation(loc, date, time, Customer(name, phone, address), tables, party_size, seat, occasion, notes))
        else:   # update existing
            reservations[index] = Reservation(loc, date, time, Customer(name, phone, address), tables, party_size, seat, occasion, notes)
        if update_callback:  # run list update
            update_callback()

        # Create the order summary message
        message = f'Thank you! A reservation has been placed for: {name}. \n \n\
                The reservation will be for a party of {party_size} seated at the {seat} starting at {time}. \n'
        if phone:
                message += f"We will text the phone number {phone} when the table is ready. \n"
        if address:
                message += f"Confirmation will be sent to the email {address}. \n"
        
        #Create a new window to display the output message
        output_window = tk.Toplevel(edit_window)
        output_window.title('Reservation Summary Confirmation')
    
        # Display the order summary message
        message_label = tk.Label(output_window, text=message)
        message_label.pack()

        def close_windows():
            # closes the confirmation dialog and the edit window
            output_window.destroy()
            edit_window.destroy()

        # Add a button to close the output window
        close_button = tk.Button(output_window, text='Close', command=close_windows)
        close_button.pack(pady=(0, 10))    # tuple for (top, bottom) padding

        return

    def on_clear():
        # Runs when user clicks clear, form will delete input. May not be needed.
        name_inp.delete(0, tk.END)
        address_inp.delete(0, tk.END)
        phone_inp.delete (0, tk.END)
        party_size_var.set('1')
        seat_var.set('Main area')
        occasion_var.set('None')
        time_var.set("3:00 PM")
        output_line.configure(text='')


    def on_close():
        # Runs when user clicks Exit button and confirms
        #if messagebox.askokcancel('Exit', 'Are you sure you want to exit?'):
        edit_window.destroy()
        return False


    # begin with a blank reservation. If one sent as arg, prefill fields.
    this_res = Reservation(loc, datetime.today(), "11:00", Customer("(new customer)"), 1, 1, seating="Main area")
    if res:
        this_res = res    


    # Create the window title, size and color
    edit_window = tk.Toplevel()
    edit_window.title("Reservation Info")
    #edit_window.geometry('600x515')
    edit_window.resizable(True, True)
    edit_window.configure(bg=window_bg_color)

    r = 0  # to make it easier to rearrange items by moving the code

    # Add widgets to the window

    # Title
    title = tk.Label(edit_window, text="Welcome to A Nice Restaurant!",
                    font=('Times Roman', 24, "bold"),
                    bg=window_bg_color, fg=fg_color)
    title.grid(row=r, column=0, columnspan=2, sticky="ew", padx=paddingx, pady=paddingy)


    def new_input_field(label_text, row, default_value=""):
        # style and place a label and return the entry field
        # if using elsewhere, will need to change edit_window to name of window you are adding to.
        label = tk.Label(edit_window, text=label_text, bg=window_bg_color, fg=fg_color, font=label_font)
        label.grid(row=row, column=0, sticky="w", padx=paddingx, pady=paddingy)

        entry = tk.Entry(edit_window, font=input_font)
        entry.grid(row=row, column=1, sticky="we", padx=paddingx, pady=paddingy)
        entry.insert(0, default_value)  # Prefill

        return entry
    
    def new_option_menu(label_text, row, options, default_value):
        # Allows to easily add a label and option box.
        # Returns variable for getting later.
        parent = edit_window
        label = tk.Label(parent, text=label_text, bg=window_bg_color, fg=fg_color, font=label_font)
        label.grid(row=row, column=0, sticky="w", padx=paddingx, pady=paddingy)

        var = tk.StringVar(parent)
        var.set(default_value)  # Set the default selection

        option_menu = tk.OptionMenu(parent, var, *options)
        option_menu.configure(bg=select_bg_color, font=input_font, takefocus=True)
        # allow keyboard selection with Enter. Appear at the widget x, y position.
        option_menu.bind("<Return>", lambda event: parent.nametowidget(option_menu.menuname).tk_popup(
        option_menu.winfo_rootx(), option_menu.winfo_rooty() + option_menu.winfo_height()))

        # Configure dropdown menu items styling
        menu = parent.nametowidget(option_menu.menuname)
        menu.configure(font=input_font)

        #add to window
        option_menu.grid(row=row, column=1, sticky="we", padx=paddingx, pady=paddingy)

        return var  # Return the variable so you can get its value later

    # User inputs name information
    def on_focus(event):
        # if name is (new customer) auto-select it to overwrite
        if name_inp.get() == "(new customer)":
            name_inp.select_range(0, tk.END)    
    r += 1
    name_inp = new_input_field("Name *", r, this_res.cust.name)
    name_inp.bind("<FocusIn>", on_focus)  # to check if new customer

    # User inputs phone number information
    r += 1
    phone_inp = new_input_field("Phone Number *", r, this_res.cust.phone)

    # User inputs email address information
    r += 1
    address_inp = new_input_field("Email Address", r, this_res.cust.email)

    # Number of Tables
    r += 1
    tables_inp = new_input_field("Number of Tables *", r, this_res.tables)

    # Party Size Selection
    r += 1
    party_size_var = new_option_menu("Select Party Size", r, list(range(1, 13)), "1")

    # Seating Selection
    r += 1
    seat_var = new_option_menu("Select Seating Area", r, list(loc.seating.keys()), this_res.seating)

    # Date Selection
    r += 1
    from tkinter import ttk
    from tkcalendar import Calendar
    from tkcalendar import DateEntry
    date_label = tk.Label(edit_window, text='Select a date for reservation:')
    date_label.configure(bg=window_bg_color, fg=fg_color, font=label_font)
    date_label.grid(row=r, column=0, sticky='nw', padx=paddingx, pady=paddingy)
    date_inp = DateEntry(edit_window, firstweekday="sunday", date_pattern='yyyy-mm-dd', showweeknumbers=False, weekendbackground="white", weekendforeground="black") #, startdate=date)
    date_inp.configure(font=input_font, takefocus=True)
    date_inp.grid(row=r, column=1, sticky='e', padx=paddingx, pady=paddingy)
    date_inp.set_date(this_res.date)  # prefill

    # Time Selection
    r += 1
    time_opts = []
    for i in range(11, 22):    # Currently hard-coded. Maybe take from loc.open_time and loc.close_time
        time_opts.append(str(i) + ":00")
        time_opts.append(str(i) + ":30")
    time_var = new_option_menu("Select desired arrival time:", r, time_opts, this_res.time)

    # Special Occasion Selection
    r += 1
    occasion_var = new_option_menu("Select Special Occasion", r, occasion_list, this_res.occasion)

    # Extra notes
    r += 1
    occasion_label = tk.Label(edit_window, text='Notes')
    occasion_label.configure(bg=window_bg_color, fg=fg_color, font=label_font)
    occasion_label.grid(row=r, column=0, sticky='nw', padx=paddingx, pady=paddingy)
    notes_inp = tk.Text(edit_window, height=3, width=30)
    notes_inp.configure(bg=select_bg_color, font=input_font)
    notes_inp.grid(row=r, column=1, sticky='we', padx=paddingx, pady=paddingy)
    notes_inp.insert("1.0", this_res.notes)   # prefill
    notes_inp.bind("<Tab>", lambda event: event.widget.tk_focusNext().focus() or "break")
    notes_inp.bind("<Shift-Tab>", lambda event: event.widget.tk_focusPrev().focus() or "break")

    # add separator before action buttons
    r += 1
    # Separator object
    separator = ttk.Separator(edit_window, orient='horizontal')
    separator.grid(row=r, column=0, columnspan=2, sticky="ew", padx=paddingx, pady=paddingy*3)

    # Clear button
    clear_btn = tk.Button(edit_window, text='Cancel', command=on_close)
    clear_btn.configure(bg=button_bg_color, font=button_font)
    clear_btn.grid(row=99, column=0, columnspan=1, sticky='NSEW', padx=paddingx, pady=paddingy)

    # Checkout button
    submit_btn = tk.Button(edit_window, text='Save', command=on_submit)
    submit_btn.configure(bg=button_bg_color, font=button_font)
    submit_btn.grid(row=99, column=1, columnspan=1, sticky='NSEW', padx=paddingx, pady=paddingy)

    # Exit button
    # exit_btn = tk.Button(edit_window, text='Close', command=on_exit)
    # exit_btn.configure(bg=button_bg_color, font=button_font)
    # exit_btn.grid(row=100, column=0, columnspan=2, sticky='NSEW', padx=paddingx, pady=paddingy)

    # Output message
    output_line = tk.Label(edit_window, text='', anchor='w', justify='left', pady=10)
    error_line = tk.Label(edit_window, text='', anchor='w', justify='left', pady=10)

    # auto-select the first entry
    edit_window.after(100, lambda: name_inp.focus_set())

    edit_window.mainloop()

def edit_cust(index=None, update_callback=None):
    # Shows fields to edit or add a customer.
    # If sent an exsiting customer index, will be prefilled with that info.
    # Otherwise, will initilize to a blank customer.
    
    if index is None or len(customers) == 0:
        cus = None
    else:
        if index < 0:
            index = 0
        if index >= len(customers):
            index = len(customers) - 1
        cus = customers[index]
    
    def on_submit():

        # Runs if user tries to provide without providing additional information
        name = name_inp.get()
        if not name:
            messagebox.showerror('Name required', "Please enter a name.")
            return

        phone = phone_inp.get()
        #if not phone:
        #    messagebox.showerror('Phone required', "Please enter your phone number")
        #    return
        
        address = address_inp.get()
        
        """
        # check for exising customer, and create new if not found
        def find_customer_index(customers, name, phone, address):
            # looks for matches of name, phone, email and returns index of matching customer
            for index, cust in enumerate(customers):
                if cust.name==name and cust.phone==phone and cust.email==address:
                    return index
            return -1
        index = find_customer_index(customers, name, phone, address)
        if index == -1:  # no customer, create new one
            customers.append(Customer(name, phone, address))
        """

        if cus is None:   # create new
            customers.append(Customer(name, phone, address))
        else:   # update existing
            customers[index] = Customer(name, phone, address)
        if update_callback:  # run list update
            update_callback()

        cust_window.destroy()

        return


    def on_close():
        # Runs when user clicks Exit button and confirms
        #if messagebox.askokcancel('Exit', 'Are you sure you want to exit?'):
        cust_window.destroy()
        return False


    # begin with a blank customer
    this_cus = Customer("(new customer)")
    if cus:
        this_cus = cus


    # Create the window title, size and color
    cust_window = tk.Toplevel()
    cust_window.title("Customer Info")
    cust_window.resizable(True, True)
    cust_window.configure(bg=window_bg_color)

    r = 0  # to make it easier to rearrange items by moving the code

    # Add widgets to the window

    # Title
    title = tk.Label(cust_window, text="Enter Customer Info",
                    font=('Times Roman', 24, "bold"),
                    bg=window_bg_color, fg=fg_color)
    title.grid(row=r, column=0, columnspan=2, sticky="ew", padx=paddingx, pady=paddingy)


    def new_input_field(label_text, row, default_value=""):
        # style and place a label and return the entry field
        # if using elsewhere, will need to change cust_window to name of window you are adding to.
        label = tk.Label(cust_window, text=label_text, bg=window_bg_color, fg=fg_color, font=label_font)
        label.grid(row=row, column=0, sticky="w", padx=paddingx, pady=paddingy)

        entry = tk.Entry(cust_window, font=input_font)
        entry.grid(row=row, column=1, sticky="we", padx=paddingx, pady=paddingy)
        entry.insert(0, default_value)  # Prefill

        return entry
    
    # User inputs name information
    def on_focus(event):
        # if name is (new customer) auto-select it to overwrite
        if name_inp.get() == "(new customer)":
            name_inp.select_range(0, tk.END)    
    r += 1
    name_inp = new_input_field("Name *", r, this_cus.name)
    name_inp.bind("<FocusIn>", on_focus)  # to check if new customer

    # User inputs phone number information
    r += 1
    phone_inp = new_input_field("Phone Number *", r, this_cus.phone)

    # User inputs email address information
    r += 1
    address_inp = new_input_field("Email Address", r, this_cus.email)

    # add separator before action buttons
    r += 1
    # Separator object
    separator = ttk.Separator(cust_window, orient='horizontal')
    separator.grid(row=r, column=0, columnspan=2, sticky="ew", padx=paddingx, pady=paddingy*3)

    # Clear button
    clear_btn = tk.Button(cust_window, text='Cancel', command=on_close)
    clear_btn.configure(bg=button_bg_color, font=button_font)
    clear_btn.grid(row=99, column=0, columnspan=1, sticky='NSEW', padx=paddingx, pady=paddingy)

    # Checkout button
    submit_btn = tk.Button(cust_window, text='Save Info', command=on_submit)
    submit_btn.configure(bg=button_bg_color, font=button_font)
    submit_btn.grid(row=99, column=1, columnspan=1, sticky='NSEW', padx=paddingx, pady=paddingy)

    # auto-select the first entry
    cust_window.after(100, lambda: name_inp.focus_set())

    cust_window.mainloop()


global view
view = "reservations"

def main_list():
    # main view, showing all reservations, or customers, depending on view. Buttons for New, Edit, Delete, Change View, or Exit program.
    # Possibly the delete option will be under the Edit option.    

    def add_res():
        edit_res(None, update_listbox)  # sent with no args for new reservation

    def del_res():
        selected = listbox.curselection()
        if selected:
            # confirmation dialog goes here
            message = str(reservations[selected[0]])
            message += '\n\nAre you sure you want to delete?'
            messagebox.askokcancel('Delete Reservation', message) 
            del reservations[selected[0]]
            update_listbox()

    def exit_program():
        # Runs when user clicks Exit button and confirms
        if messagebox.askokcancel('Exit', 'Files will be saved. Are you sure you want to exit?'):
            save_customers()
            save_reservations()
            root.destroy()
            return False
    
    def edit_selected_res():
        # Gets current selection and sends index to edit_res function.
        selected = listbox.curselection()
        if selected:   # check if not blank
            edit_res(selected[0], update_listbox)  # sel is a tuple, but I only want the first entry

    def add_cust():
        edit_cust(None, update_listbox)  # sent with no args for new customer

    def edit_selected_cust():
        # Gets current selection and sends index to edit_res function.
        sel = listbox.curselection()
        if sel:   # check if not blank
            edit_cust(sel[0], update_listbox)  # sel is a tuple, but I only want the first entry

    def del_cust():
        #Runs when user clicks Delete Customers button and confirms
        selected = listbox.curselection()
        if selected:
            # confirmation dialog goes here
            message = str(customers[selected[0]])
            message += '\n\nAre you sure you want to delete?'
            messagebox.askokcancel('Delete Customer', message)
            del customers[selected[0]]
            update_listbox()

    def update_listbox():
        # Call this to refresh listbox after any changes.
        listbox.delete(0, tk.END)   # start with empty listbox
        if view=="reservations":
            title_label.config(text="Reservations")
            listbox.configure(bg="#bbbbff")
            for i in range(len(reservations)):
                s = "s" if reservations[i].tables != 1 else ""  # Do not include "s" for 1 table.
                listbox.insert(tk.END, f"   {reservations[i].date} - {reservations[i].time} - {reservations[i].cust.name} - {reservations[i].tables} table{s} in {reservations[i].seating}")
            # Re-define buttons
            switch_button.config(text="Switch to Customers", bg="#bbffbb")
            new_button.config(text="New Reservation", command=add_res)
            modify_button.config(text="Modify Reservation", command=edit_selected_res)
            delete_button.config(text="Delete Reservation", command=del_res)
        else:
            title_label.config(text="Customers")
            listbox.configure(bg="#bbffbb")
            for i in range(len(customers)):
                listbox.insert(tk.END, f"   {customers[i].name} - {customers[i].phone} - {customers[i].email}")
            # Re-define buttons
            switch_button.config(text="Switch to Reservations", bg="#bbbbff")
            new_button.config(text="New Customer", command=add_cust)
            modify_button.config(text="Modify Customer", command=edit_selected_cust)
            delete_button.config(text="Delete Customer Info", command=del_cust)

    def switch_view():
        global view
        if view=="reservations":
            view = "customers"
        else:
            view = "reservations"
        update_listbox()

    root = tk.Tk()
    root.title("Reservation System")
    #root.geometry("400x300")
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    scrollbar = tk.Scrollbar(frame)

    title_label = tk.Label(frame, text="Reservations", font=("Arial", 16, "bold"), bg="lightgray")
    title_label.pack(fill=tk.X, padx=10, pady=5)

    listbox = tk.Listbox(frame, selectmode=tk.SINGLE, yscrollcommand=scrollbar.set,
                         font=("Arial", 14), fg="black", bg="#bbbbff",
                         selectbackground="gray", activestyle=tk.NONE)

    scrollbar.config(command=listbox.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    btn_frame = tk.Frame(root)
    btn_frame.pack(fill=tk.X, padx=5, pady=5)

    def add_button(text, command):
        # Add a button easily. If porting somewhere else, change btn_frame.
        make_button = tk.Button(btn_frame, text=text, command=command)
        make_button.configure(bg=button_bg_color, font=button_font)
        make_button.pack(side=tk.LEFT, expand=True, padx=10)
        return make_button

    new_button = add_button("New", add_res)
    modify_button = add_button("Modify", edit_selected_res)
    delete_button = add_button("Delete", del_res)
    switch_button = add_button("Switch View", switch_view)
    exit_button = add_button("Save & Exit", exit_program)

    update_listbox()

    root.mainloop()    


if __name__ == "__main__":
    # edit_res(reservations[0])  # to test with prefilled info
    # edit_res()                   # to test with new customer info. Optionally, make new_res().
    main_list()

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