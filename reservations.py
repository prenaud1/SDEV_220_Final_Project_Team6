"""
reservations.py
by Paul Renaud, LaToya Finnell, Sidart Rav, Kodi Righthouse
Allows a restaurant employee to add, edit, or remove existing reservations.

April 10, 2025
Started writing - Paul.
"""

class Customer:
    """
    Creates a Customer. Name is required. Phone and email are optional.
    """
    def __init__(self, name, phone=None, email=None):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        output_string = "Customer: "
        output_string += self.name
        output_string += " | Phone: "
        if self.phone != None:
            output_string += self.phone
        output_string += " | Email: "
        if self.email != None:
            output_string += self.email
        return output_string

class Reservation:
    """
    Creates a new Reservation. datetime is just a string for now. cust is a Customer class. Notes are optional.
    """
    def __init__(self, datetime, cust, party_size, notes=None):
        self.datetime = datetime
        self.cust = cust
        self.party_size = party_size
        self.notes = notes

    def __str__(self):
        output_string = "Date/Time: "
        output_string += self.datetime
        output_string += " | Name: "
        output_string += self.cust.name
        output_string += " | Party Size: "
        output_string += str(self.party_size)
        output_string += " | Notes: "
        if self.notes != None:
            output_string += self.notes
        return output_string
    

# code debug
all_cus = []
c = Customer("Smith", email="bsmith@domain.com")
all_cus.append(c)
c = Customer("Miller", phone="578-457-4082")
all_cus.append(c)
all_cus.append(Customer("Gale"))
for c in all_cus:
    print(c)

all_res = []

# debug
all_res.append(Reservation("12 noon", all_cus[0], 12, "30th birthday"))
all_res.append(Reservation("6pm", all_cus[1], 3))

def res_list():
    """
    Shows reservation list. Allows you to edit, add, and delete reservations.
    """
    while True:
        print("\n---------------------")
        print("Reservations")
        i = 0
        for r in all_res:
            i += 1
            print(i, "-", r)
        print("\n(N)ew reservation, (D)elete reservation, switch to (C)ustomer list, (Q)uit")
        choice = input("Make a selection [#, N, D, C, Q]: ").upper()
        selection = 0
        try:
            selection = int(choice)
        except:
            pass
        if choice == "Q":
            return "Q"
        elif choice == "D":
            del_res()
        elif choice == "N":
            new_res()
        elif choice == "C":
            choice = cus_list()
            if choice == "Q":
                return "Q"
        elif selection > 0 and selection <= len(all_res):
            edit_res(selection - 1)  # adjusted for offset

def cus_list():
    """
    Shows customer list, with options to edit, add New customer, Delete, or go back to Reservation list.
    """
    while True:
        print("\n---------------------")
        print("Customers")
        i = 0
        for c in all_cus:
            i += 1
            print(i, "-", c)
        print("\n(N)ew customer, (D)elete customer info, switch to (R)eservation list, (Q)uit")
        choice = input("Make a selection [#, N, D, R, Q]: ").upper()
        selection = 0
        try:
            selection = int(choice)
        except:
            pass
        if choice == "Q":
            return "Q"
        elif choice == "R":
            return
        elif choice == "D":
            del_cus()
        elif choice == "N":
            new_cus()
        elif selection > 0 and selection <= len(all_cus):
            edit_cus(selection - 1) # adjusted for offset
        

def new_res():
    print("New reservation")
    print("Ask for reservation info.")
    print("(May be able to call the edit screen with blank res.)")

def del_res():
    print("Delete reservation")
    print("Ask for confirmation.")

def edit_res(offset):
    print("Edit reservation at offset", offset)

def new_cus():
    print("New customer")
    print("Ask for customer info.")
    print("(May be able to call the edit screen with blank info.)")

def del_cus():
    print("Delete customer information")
    print("Ask for confirmation.")

def edit_cus(offset):
    print("Edit customer at offset", offset)


while True:
    choice = res_list()
    if choice == "Q":
        break

print("Thank you. Goodbye.")

