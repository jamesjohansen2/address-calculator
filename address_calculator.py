'''
Name: Address Number Calculator
Author: James Johansen
Date: 9/27/2017
Purpose: Increase ease and accuracy of calculating a new address number.
         Formula derived from Addressing documentation.
Python Version 2.7
'''

from Tkinter import *

# create window with default size and a title
myGUI = Tk()
myGUI.geometry('400x200')
myGUI.title('Address Number Calculator')

# function that gets user input from window and calculates address number
def calculate_address():

    # get user inputs from window
    distance1 = float(d1.get())
    distance2 = float(d2.get())
    from_address = float(from_addr.get())
    to_address = float(to_addr.get())

    # calculation
    address = ( ( (to_address - from_address) / distance2 ) * distance1 ) + from_address

    # output statement
    label_result = Label(myGUI, text = 'The address number is: \n%.1f' % address, font = 'bold').grid(row = 5, column = 2)

    return

# create variables to hold user inputs
d1 = StringVar()
d2 = StringVar()
from_addr = StringVar()
to_addr = StringVar()

# create labels
label1 = Label(myGUI,text = 'Address Number Calculator',).grid(row = 0, column = 0)
label2 = Label(myGUI,text = 'Start of segment to address', fg = 'teal').grid(row = 1, column = 0)
label3 = Label(myGUI,text = 'Total segment length', fg = 'teal').grid(row = 2, column = 0)
label4 = Label(myGUI,text = 'From address', fg = 'teal').grid(row = 3, column = 0)
label5 = Label(myGUI,text = 'To address', fg = 'teal').grid(row = 4, column = 0)

# create entry boxes
entry1 = Entry(myGUI, textvariable = d1).grid(row = 1, column = 2)
entry2 = Entry(myGUI, textvariable = d2).grid(row = 2, column = 2)
entry3 = Entry(myGUI, textvariable = from_addr).grid(row = 3, column = 2)
entry4 = Entry(myGUI, textvariable = to_addr).grid(row = 4, column = 2)

# button that activates the calculate_address function
button1 = Button(myGUI, text = 'Calculate address', command = calculate_address).grid(row = 5, column = 0)

myGUI.mainloop()

