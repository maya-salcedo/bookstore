from tkinter import *

window = Tk()

def km_to_miles():
    miles = float(e1_value.get())*1.6
    t1.insert(END, miles)

b1 = Button(window, text="Execute", command=km_to_miles)
b1.grid(row=0, column=0) # to see the button and choose the location,
# .pack() can also be used but you cant choose the location of the button


e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value)
e1.grid(row=0, column=1) # Entry is an area where you can enter the value

t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)

# Should be always on the end of the code:
window.mainloop()