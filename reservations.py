"""
reservations.py
by Paul Renaud, LaToya Finnell, Sidart Rav, Kodi Righthouse
Allows a restaurant employee to add, edit, or remove existing reservations.

April 11, 2025 - Paul Renaud
Basic functionality works in text mode.
We will need to add date/time checkers, restaurant checks (hours and seat
availability), file saving, and GUI.

April 10, 2025 - Paul Renaud
Started writing.
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

    def full_print(self):
        print("\nCustomer Information")
        print("Name -", self.name)
        print("Phone -", self.phone)
        print("Email -", self.email)

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
    
    def full_print(self):
        print("\nReservation Information")
        print("Date -", self.datetime)
        print("Name -", self.cust.name)
        print("Party size -", str(self.party_size))
        print("Notes -", self.notes)

    

all_cus = []

# code testing for debug
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
    Main view. Shows reservation list. Allows you to edit, add, and delete reservations.
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
            choice = del_res()
            if choice == "Q":
                return "Q"
        elif choice == "N":
            new_res()
        elif choice == "C":
            choice = cus_list()
            if choice == "Q":
                return "Q"
        elif selection > 0 and selection <= len(all_res):
            edit_res(all_res[selection - 1])  # adjusted for offset

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
            edit_cus(all_cus[selection - 1]) # adjusted for offset
        

def new_res():
    """
    Returns the new reservation or empty string if none made.
    """
    r = edit_res(Reservation("datetime", Customer("name"), 1)) # creates a blank reservation to edit.
    if r:
        all_res.append(r)
        return r
    else:
        return ""
    
def del_res():
    """
    Deletes a reservation. Asks for confirmation first.
    """
    while True:
        print("\n---------------------")
        print("Delete reservation")
        i = 0
        for r in all_res:
            i += 1
            print(i, "-", r)
        if len(all_res) == 0:
            print("No reservations in list.")
        print("\nEnter number to delete, or go back to R)eservation list.")
        choice = input("Make a selection [#, R]: ").upper()
        if choice == "R":
            return
        else:
            selection = 0
            try:
                selection = int(choice)
            except:
                pass
            if selection > 0 and selection <= len(all_res):
                all_res[selection - 1].full_print()
                choice = input("Type DEL to delete this reservation: ")
                if choice == "DEL":
                    del all_res[selection - 1]
                    print("Deleted.")
                else:
                    print("Did not delete.")

def edit_res(res):
    """
    Accepts a Reservation, and returns a possibly modified Reservation.
    If reservation customer name is "name" it returns empty string "" instead.
    """
    while True:
        print("\n---------------------")
        res.full_print()
        choice = input("Make changes? Y/N ").upper()
        if choice == "Y":  # asks for fields one at a time, with existing information prefilled.
            prompt = "Date [" + res.datetime + "]: "
            choice = input(prompt)
            if choice != "":
                res.datetime = choice

            i = 0
            for c in all_cus:
                i += 1
                print(i, "-", c.name)
            while True:
                prompt = "Name (N to add a new customer) [" + res.cust.name + "]:"
                choice = input(prompt).upper()
                if choice != "":
                    if choice == "N":
                        c = new_cus()
                        if c:
                            res.cust = all_cus[len(all_cus) - 1]
                    else:
                        selection = 0
                        try:
                            selection = int(choice)
                        except:
                            pass
                        if selection > 0 and selection <= len(all_cus):
                            res.cust = all_cus[selection - 1]
                        else:
                            print("Not a valid customer.")
                else:
                    break

            while True:
                prompt = "Party Size [" + str(res.party_size) + "]: "
                choice = input(prompt)
                if choice != "":
                    try:
                        res.party_size = int(choice)
                        break
                    except:
                        print("Not a valid number.")
                else:
                    break
            prompt = "Notes ["
            if res.notes != None:
                prompt += res.notes
            prompt += "]: "
            choice = input(prompt)
            if choice != "":
                res.notes = choice
        else:  # does not want to make changes
            if res.cust.name != "name":
                return res
            else:
                return ""

def new_cus():
    """
    Returns the new customer or empty string if none made.
    """
    c = edit_cus(Customer("name")) # creates a blank customer.
    if c:
        all_cus.append(c)
        return c
    else:
        return ""

def del_cus():
    """
    Deletes a customer's info. Prompts for confirmation first.
    """
    while True:
        print("\n---------------------")
        print("Delete customer information")
        i = 0
        for c in all_cus:
            i += 1
            print(i, "-", c)
        if len(all_cus) == 0:
            print("No customers in list.")
        print("\nEnter number to delete, or go back to R)eservation list.")
        choice = input("Make a selection [#, R]: ").upper()
        if choice == "R":
            return
        else:
            selection = 0
            try:
                selection = int(choice)
            except:
                pass
            if selection > 0 and selection <= len(all_cus):
                all_cus[selection - 1].full_print()
                choice = input("Type DEL to delete this customer: ")
                if choice == "DEL":
                    del all_cus[selection - 1]
                    print("Deleted.")
                else:
                    print("Did not delete.")


def edit_cus(cus):
    """
    Accepts a Customer, and returns a possibly modified Customer.
    If customer name is "name" upon exiting, returns empty string "" instead.
    This prevents a new customer from being added accidentally.
    """
    while True:
        print("\n---------------------")
        cus.full_print()
        choice = input("Make changes? Y/N ").upper()
        if choice == "Y":  # asks for fields one at a time, with existing information prefilled.
            prompt = "Name [" + cus.name + "]: "
            choice = input(prompt)
            if choice != "":
                cus.name = choice

            p = cus.phone
            if p == None:
                p = ""
            prompt = "Phone [" + p + "]: "
            choice = input(prompt)
            if choice != "":
                cus.phone = choice

            e = cus.email
            if e == None:
                e = ""
            prompt = "Email [" + e + "]: "
            choice = input(prompt)
            if choice != "":
                cus.phone = choice

        else:  # does not want to make changes
            if cus.name != "name":
                return cus
            else:
                return ""


# Main program start. Runs the reservation list until Quit.
while True:
    choice = res_list()
    if choice == "Q":
        break

print("Thank you. Goodbye.")

