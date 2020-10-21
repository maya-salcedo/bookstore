#This is FRONTEND

"""
A program that stores this boook information
Title, Author
Year, ISBN

User can:
View all records
Search an entry
Add entry
Update entry
Delete
Close
"""

from tkinter import *
import backend

def view_command():
    list1.delete(0, END) # this code will the stop the view button from reloading again the same data
    for row in backend.view():
        list1.insert(END, row) # this means that after the row, a new row is added to the list1 or Listbox

def search_command():
    list1.delete #to empty the listbox



window = Tk()

title_text = StringVar()
t1 = Entry(window, textvariable=title_text).grid(row=0, column=1)
year_text = StringVar()
t2 = Entry(window, textvariable=year_text).grid(row=1, column=1)
author_text = StringVar()
t3 = Entry(window, textvariable= author_text).grid(row=0, column=3)
isbn_text = StringVar()
t4 = Entry(window, textvariable=isbn_text).grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

l1 = Label(window, text="Title").grid(row=0, column=0)
l2 = Label(window, text="Year").grid(row=1, column=0)
l3 = Label(window, text="Author").grid(row=0, column=2)
l4 = Label(window, text="ISBN").grid(row=1, column=2)

b1 = Button(window, text="View All", width=12, command=view_command).grid(row=2, column=3)
b2 = Button(window, text="Search Entry", width=12, command=search_command).grid(row=3, column=3)
b3 = Button(window, text="Add Entry", width=12).grid(row=4, column=3)
b4 = Button(window, text="Update", width=12).grid(row=5, column=3)
b5 = Button(window, text="Delete", width=12).grid(row=6, column=3)
b6 = Button(window, text="Close", width=12).grid(row=7, column=3)

window.mainloop()

