from tkinter import *

window = Tk()

def kg_to_g():
    grams = float(e1_value.get())*1000
    t1.insert(END, grams)

def kg_to_pounds():
    pounds = float(e1_value.get()) * 2.20462
    t2.insert(END, pounds)

def kg_to_ounces():
    ounces = float(e1_value.get()) * 35.274
    t3.insert(END, ounces)

b1 = Button(window, text="Convert", command=lambda :[kg_to_g(), kg_to_pounds(), kg_to_ounces()])
b1.grid(row=0, column=2) # to see the button and choose the location,
# .pack() can also be used but you cant choose the location of the button


e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value)
e1.grid(row=0, column=0) # Entry is an area where you can enter the value

t1 = Text(window, height=1, width=15)
t1.grid(row=1, column=0)
t2 = Entry(window)
t2.grid(row=2, column=0)
t3 = Entry(window)
t3.grid(row=3, column=0)

Label(window, text="kilogram").grid(row=0, column=1)
Label(window, text="gram").grid(row=1, column=1)
Label(window, text="pounds").grid(row=2, column=1)
Label(window, text="gram").grid(row=3, column=1)

# Should be always on the end of the code:
window.mainloop()