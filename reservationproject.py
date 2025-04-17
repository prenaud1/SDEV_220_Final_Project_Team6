import tkinter as tk
from tkinter import messagebox


def on_submit():
    # Runs if user tries to provide without providing additional information
    name = name_inp.get()
    if not name:
        messagebox.showerror('Error', "Please enter your name!")
        return

    address = address_inp.get()
    if not address:
        messagebox.showerror('Error', "Please enter your email address!")
        return

    number = number_inp.get()
    if not number:
        messagebox.showerror('Error', "Please enter your phone number!")
        return

    size = size_var.get()
    seat = seat_var.get()
    time = time_var.get()
    occasion = occasion_var.get()

    if not time:
        messagebox.showerror('Error', 'Please select at least one time.')
        return

    if not occasion:
        messagebox.showerror('Error', 'Please select at least one Special Occasion or none.')
        return

    # Create the order summary message
    message = f'Thanks for placing your reservation, {name}! \n \n You reservation will be for a party of {size} seated at the {seat} at {time}. \n We will text the phone number {number} when your table is ready. \n Confirmation will be sent to your email {address}. \n'

    # Create a new window to display the output message
    output_window = tk.Toplevel(root)
    output_window.title('Reservation Summary Confirmation')

    # Display the order summary message
    message_label = tk.Label(output_window, text=message)
    message_label.pack()

    # Add a button to close the output window
    close_button = tk.Button(output_window, text='Close', command=output_window.destroy)
    close_button.pack()

    # Set the size of the output window
    output_window.geometry('550x115')


def on_clear():
    # Runs when user clicks clear, form will delete input
    name_inp.delete(0, tk.END)
    address_inp.delete(0, tk.END)
    number_inp.delete(0, tk.END)
    size_var.set('0')
    seat_var.set('Private Room')
    occasion_var.set('None')
    for time_var in time_var:
        time_var.set(False)
    output_line.configure(text='')


def on_exit():
    # Runs when user clicks Exit button and confirms
    if messagebox.askokcancel('Exit', 'Are you sure you want to exit?'):
        root.destroy()


# Create the window title, size and color
root = tk.Tk()
root.title("Reservation")
root.geometry('600x515')
root.resizable(True, True)
root.configure(bg='black')  # Change background color to black

# Add widgets to the window
title = tk.Label(root, text="Welcome to A Seat at the Table Reservation!", font=('Times Roman', 20), bg='black',
                 fg='orange', pady=10)

# User inputs name information
name_label = tk.Label(root, text='Name')
name_inp = tk.Entry(root)
name_label.configure(bg='black')

# User inputs email address information
address_label = tk.Label(root, text='Email Address')
address_inp = tk.Entry(root)
address_label.configure(bg='black')

# User inputs phone number information
number_label = tk.Label(root, text='Phone Number')
number_inp = tk.Entry(root)
number_label.configure(bg='black')

# Party Size Selection
size_label = tk.Label(root, text='Select Party Size')
size_var = tk.StringVar(root, '0')
size_opts = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
size_inp = tk.OptionMenu(root, size_var, *size_opts)
size_label.configure(bg='black')

# Seating Selection
seat_label = tk.Label(root, text='Select Seating Area')
seat_var = tk.StringVar(root, 'Private Room')
seat_opts = ['Private Room', 'Patio', 'Roof Top View']
seat_inp = tk.OptionMenu(root, seat_var, *seat_opts)
seat_label.configure(bg='black')

# Time Selection
time_label = tk.Label(root, text='Select an available time:')
time_var = tk.StringVar(root, '3:00 PM')
time_opts = ['3:00 PM', '3:30 PM', '4:00 PM', '4:30 PM', '5:00 PM', '5:30 PM', '6:00 PM', '6:30 PM', '7:00 PM',
             '7:30 PM', '8:00 PM', '8:30 PM', '9:00 PM']
time_inp = tk.OptionMenu(root, time_var, *time_opts)
time_label.configure(bg='black')

# Date Selection
from tkinter import ttk
from tkcalendar import Calendar

date_label = tk.Label(root, text='Select a date for reservation:')
date_label.configure(bg='black')
date_inp = Calendar(root, selectmode='day', date_pattern='yyyy-mm-dd')
date_label.grid(row=8, column=0, sticky='w')
date_inp.grid(row=8, column=1, sticky='e')

# Special Occasion Selection
occasion_label = tk.Label(root, text='Select Special Occasion')
occasion_var = tk.StringVar(root, 'None')
occasion_opts = ['Birthday', 'Mothers Day', 'Fathers Day', 'Anniversary', 'Wedding', 'Graduation', 'None']
occasion_inp = tk.OptionMenu(root, occasion_var, *occasion_opts)
occasion_label.configure(bg='black')

# Checkout button
submit_btn = tk.Button(root, text='Submit', command=on_submit)
submit_btn.configure(bg='white')

# Clear button
clear_btn = tk.Button(root, text='Clear Reservation', command=on_clear)
clear_btn.configure(bg='white')

# Exit button
exit_btn = tk.Button(root, text='Exit', command=on_exit)
exit_btn.configure(bg='white')

# Output message
output_line = tk.Label(root, text='', anchor='w', justify='left', pady=10)
error_line = tk.Label(root, text='', anchor='w', justify='left', pady=10)

# Arrange widgets on the window
title.grid(row=0, column=0, columnspan=2)

# Name input
name_label.grid(row=1, column=0, sticky='w')
name_inp.grid(row=1, column=1, sticky='e')

# Address input
address_label.grid(row=2, column=0, sticky='w')
address_inp.grid(row=2, column=1, sticky='e')

# Phone Number input
number_label.grid(row=3, column=0, sticky='w')
number_inp.grid(row=3, column=1, sticky='e')

# Size selection
size_label.grid(row=4, column=0, sticky='w')
size_inp.grid(row=4, column=1, sticky='e')
size_inp.configure(bg='green')

# Seating selection
seat_label.grid(row=5, column=0, sticky='w')
seat_inp.grid(row=5, column=1, sticky='e')
seat_inp.configure(bg='green')

# Time selection
time_label.grid(row=7, column=0, sticky='w')
time_inp.grid(row=7, column=1, sticky='e')
time_inp.configure(bg='green')

# Special Occasion selection
occasion_label.grid(row=6, column=0, sticky='w')
occasion_inp.grid(row=6, column=1, sticky='e')
occasion_inp.configure(bg='green')

# Submit button location
submit_btn.grid(row=99, column=0, columnspan=1, sticky='NSEW')

# Exit Button Location
exit_btn.grid(row=100, column=0, columnspan=2, sticky='NSEW')

# Clear Button Location
clear_btn.grid(row=99, column=1, columnspan=1, sticky='NSEW')

# error message location
error_line.grid(row=101, column=0)

root.mainloop()