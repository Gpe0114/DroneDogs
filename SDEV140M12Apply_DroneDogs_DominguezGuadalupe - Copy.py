from tkinter import *
from tkinter import messagebox

def messageWindow():
    win = Toplevel()

    listbox = Listbox(win).grid(row=0, column = 0)

    label = Label(win, text = "DroneDogs Customer Form", fg="red").grid(row= 1, column=1)
    fname_label = Label (win, text = "First Name")
    lname_label = Label (win, text = "Last Name")
    email_label = Label (win, text = "Email")

    fname_label.grid(row=2, sticky=E)
    lname_label.grid(row=3, sticky=E)
    email_label.grid(row=4, sticky=E)

    fname_entry= Entry(win)
    lname_entry= Entry(win)
    email_entry= Entry(win)

    fname_entry.grid(row=2, column=1)
    lname_entry.grid(row=3, column=1)
    email_entry.grid(row=4, column=1)




root = Tk()                      


label = Label (root, text = "DroneDogs Order Form",font=("Arial Black", 15), fg="red")
label_1 = Label (root, text = " # BeefDogs")
label_2 = Label (root, text = " # PorkDogs")
label_3 = Label (root, text = " # TurkeyDogs")

label.grid(row=0, column=1)
label_1.grid(row=2, sticky=E)
label_2.grid(row=3, sticky=E)
label_3.grid(row=4, sticky=E)

entry_1= Entry(root)
entry_2= Entry(root)
entry_3= Entry(root)

entry_1.grid(row=2, column=1)
entry_2.grid(row=3, column=1)
entry_3.grid(row=4, column=1)

photo = PhotoImage (file = "C:/Users/guadalupe/Downloads/DroneDogs_small.png")
label = Label(root, image = photo)
label.grid(row=1, column=25)

        
def calculate():
        DBL_SALES_TAX_RATE = 0.07
        DBL_COST_PER_HOTDOG = 1.99

        BeefDogs = entry_1.get()
        PorkDogs = entry_2.get()
        TurkeyDogs = entry_3.get()

        TotalHotDogs = int(str(BeefDogs)) + int(str(PorkDogs)) + int(str(TurkeyDogs))
        
        SubTotalOrder = int(TotalHotDogs) * float(DBL_COST_PER_HOTDOG)
        TaxAmtSales = float(SubTotalOrder) * float(DBL_SALES_TAX_RATE)
        TotalOrderCost = float(SubTotalOrder) + float(TaxAmtSales)

        subtotal_label = Label (root, text = "Subtotal:")
        salestax_label = Label (root, text = "Sales Tax:")
        total_label = Label (root, text = "Total Cost:")

        subtotal_label.grid(row=11, sticky=E)
        salestax_label.grid(row=12, sticky=E)
        total_label.grid(row=13, sticky=E)

        subtotal_amount = Label(root)
        salestax_amount = Label(root)
        total_amount = Label(root)

        subtotal_amount.grid(row=11, column = 2, pady = (10, 10), sticky=E)
        salestax_amount.grid(row=12, column = 2, pady = (10, 10),  sticky=E)
        total_amount.grid(row=13, column = 2, sticky=E)

        subtotal_amount.configure(text = '${:,.2f}'.format(SubTotalOrder))
        salestax_amount.configure(text = '${:,.2f}'.format(TaxAmtSales))
        total_amount.configure(text = '${:,.2f}'.format(TotalOrderCost))

        

def submit():
        messagebox.showinfo(message = "Thank you for ordering in DroneDogs!")


def close():
        root.destroy()




calculate_button1 = Button(root, text = "Calculate Order", fg="blue", command=calculate)
submit_button2 = Button(root, text = "Submit Order", fg="green", command = submit)

close_button3= Button(root, text = "Exit", fg="red", command = close)


calculate_button1.grid(row=6,column=0)
submit_button2.grid(row=6,column=1)
close_button3.grid(row=6,column=2)


root.mainloop()
