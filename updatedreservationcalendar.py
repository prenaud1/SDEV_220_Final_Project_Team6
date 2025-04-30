import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta

# Generate a list of dates for the dropdown
def generate_date_list(start_date, days=30):
    return [(start_date + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(days)]

def on_submit():
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
    date = date_inp.get()

    if not time:
        messagebox.showerror('Error', 'Please select at least one time.')
        return

    if not occasion:
        messagebox.showerror('Error', 'Please select at least one Special Occasion or none.')
        return

    # Create the order summary message
    message = (f"Thanks for placing your reservation, {name}!\n\n"
               f"Your reservation will be for a party of {size} seated at the {seat} at {time} on {date}.\n"
               f"We will text the phone number {number} when your table is ready.\n"
               f"Confirmation will be sent to your email {address}.")

    # Create a new window to display the output message
    output_window = tk.Toplevel(root)
    output_window.title('Reservation Summary Confirmation')
    message_label = tk.Label(output_window, text=message)
    message_label.pack()

    close_button = tk.Button(output_window, text='Close', command=output_window.destroy)
    close_button.pack()

    output_window.geometry('550x150')

def on_clear():
    name_inp.delete(0, tk.END)
    address_inp.delete(0, tk.END)
    number_inp.delete(0, tk.END)
    size_var.set('0')
    seat_var.set('Private Room')
    occasion_var.set('None')
    time_var.set('')
    date_inp.set(date_list[0])  # Reset dropdown to default date

def on_exit():
    if messagebox.askokcancel('Exit', 'Are you sure you want to exit?'):
        root.destroy()

# Create the window title, size, and color
root = tk.Tk()
root.title("Reservation")
root.geometry('600x600')
root.resizable(True, True)
root.configure(bg='black')

# Generate list of dates for dropdown
date_list = generate_date_list(datetime.today(), days=30)

title = tk.Label(root, text="Welcome to A Seat at the Table Reservation!", font=('Times Roman', 20), bg='black', fg='orange', pady=10)

name_label = tk.Label(root, text='Name', bg='black')
name_inp = tk.Entry(root)

address_label = tk.Label(root, text='Email Address', bg='black')
address_inp = tk.Entry(root)

number_label = tk.Label(root, text='Phone Number', bg='black')
number_inp = tk.Entry(root)

size_label = tk.Label(root, text='Select Party Size', bg='black')
size_var = tk.StringVar(root, '0')
size_opts = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
size_inp = tk.OptionMenu(root, size_var, *size_opts)

seat_label = tk.Label(root, text='Select Seating Area', bg='black')
seat_var = tk.StringVar(root, 'Private Room')
seat_opts = ['Private Room', 'Patio', 'Roof Top View']
seat_inp = tk.OptionMenu(root, seat_var, *seat_opts)

time_label = tk.Label(root, text='Select an available time:', bg='black')
time_var = tk.StringVar(root)
time_opts = ['3:00 PM', '3:30 PM', '4:00 PM', '4:30 PM', '5:00 PM', '5:30 PM', '6:00 PM', '6:30 PM', '7:00 PM', '7:30 PM', '8:00 PM', '8:30 PM', '9:00 PM']
time_inp = tk.OptionMenu(root, time_var, *time_opts)

occasion_label = tk.Label(root, text='Select Special Occasion', bg='black')
occasion_var = tk.StringVar(root, 'None')
occasion_opts = ['Birthday', 'Mothers Day', 'Fathers Day', 'Anniversary', 'Wedding', 'Graduation', 'None']
occasion_inp = tk.OptionMenu(root, occasion_var, *occasion_opts)

# Add dropdown for date selection
date_label = tk.Label(root, text='Select a date for reservation:', bg='black')
date_inp = ttk.Combobox(root, values=date_list)
date_inp.set(date_list[0])  # Set default date

submit_btn = tk.Button(root, text='Submit', command=on_submit, bg='white')
clear_btn = tk.Button(root, text='Clear Reservation', command=on_clear, bg='white')
exit_btn = tk.Button(root, text='Exit', command=on_exit, bg='white')

# Arrange widgets on the window
title.grid(row=0, column=0, columnspan=2)
name_label.grid(row=1, column=0, sticky='w')
name_inp.grid(row=1, column=1, sticky='e')

address_label.grid(row=2, column=0, sticky='w')
address_inp.grid(row=2, column=1, sticky='e')

number_label.grid(row=3, column=0, sticky='w')
number_inp.grid(row=3, column=1, sticky='e')

size_label.grid(row=4, column=0, sticky='w')
size_inp.grid(row=4, column=1, sticky='e')

seat_label.grid(row=5, column=0, sticky='w')
seat_inp.grid(row=5, column=1, sticky='e')

time_label.grid(row=6, column=0, sticky='w')
time_inp.grid(row=6, column=1, sticky='e')

occasion_label.grid(row=7, column=0, sticky='w')
occasion_inp.grid(row=7, column=1, sticky='e')

date_label.grid(row=8, column=0, sticky='w')
date_inp.grid(row=8, column=1, sticky='e')

submit_btn.grid(row=9, column=0, columnspan=1, sticky='nsew')
clear_btn.grid(row=9, column=1, columnspan=1, sticky='nsew')
exit_btn.grid(row=10, column=0, columnspan=2, sticky='nsew')

root.mainloop()
