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
from backend import Database

database = Database("books.db")

def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        t1.delete(0, END)
        t1.insert(END, selected_tuple[1])
        t2.delete(0, END)
        t2.insert(END, selected_tuple[3])
        t3.delete(0, END)
        t3.insert(END, selected_tuple[2])
        t4.delete(0, END)
        t4.insert(END, selected_tuple[4])
    except IndexError:
        pass

def view_command():
    list1.delete(0, END) # this code will the stop the view button from reloading again the same data
    for row in database.view():
        list1.insert(END, row) # this means that after the row, a new row is added to the list1 or Listbox

def search_command():
    list1.delete(0, END) #to empty the listbox
    for row in database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()): # .get() will produce a string
        list1.insert(END, row)

def add_command():
    database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))
    view_command()


def delete_command():
    database.delete(selected_tuple[0])
    view_command()

def update_command():
    database.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_command()



window = Tk()
window.wm_title("Nordic Bookstore")



title_text = StringVar()
t1 = Entry(window, textvariable=title_text)
t1.grid(row=0, column=1)
author_text = StringVar()
t3 = Entry(window, textvariable=author_text)
t3.grid(row=0, column=3)
year_text = StringVar()
t2 = Entry(window, textvariable=year_text)
t2.grid(row=1, column=1)
isbn_text = StringVar()
t4 = Entry(window, textvariable=isbn_text)
t4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

view_command()

l1 = Label(window, text="Title").grid(row=0, column=0)
l2 = Label(window, text="Year").grid(row=1, column=0)
l3 = Label(window, text="Author").grid(row=0, column=2)
l4 = Label(window, text="ISBN").grid(row=1, column=2)

b1 = Button(window, text="View All", width=12, command=view_command).grid(row=2, column=3)
b2 = Button(window, text="Search Entry", width=12, command=search_command).grid(row=3, column=3)
b3 = Button(window, text="Add Entry", width=12, command=add_command).grid(row=4, column=3)
b4 = Button(window, text="Update Selected", width=12, command=update_command).grid(row=5, column=3)
b5 = Button(window, text="Delete Selected", width=12, command=delete_command).grid(row=6, column=3)
b6 = Button(window, text="Close", width=12, command=window.destroy).grid(row=7, column=3)

window.mainloop()

