from tkinter import *
from datetime import date
window = Tk()
window.title("Getting Started with widgets")
window.geometry('400x300')
lbl = Label(text="Hey There!",  fg="white", bg= "black", height=1, width=300)
name_label = Label(text="Enter Your full name", bg = "black")
name_entry = Entry()

def display(): 
    name = name_entry.get()
    global message
    message = "Welcome to the application! \nToday's Date is: "
    greet = f"Hello {name}\n"
    text_box.insert(END, greet)
    text_box.insert(END,message)
    text_box.insert(END, date.today())

text_box = Text(height=3)
btn = Button(text = "click here", command=display, height=1, bg="lightblue", fg = "black")

lbl.pack()
name_label.pack()
name_entry.pack()
btn.pack()
text_box.pack()

window.mainloop()