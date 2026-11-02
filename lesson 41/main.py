from tkinter import *
root = Tk()
root.geometry("400x300")
root.title("main")

def topwin(): 
    top = Toplevel()
    top.geometry("180x100")
    top.title("Top Level")
    l2 = Label(top, text="This is a Top Level Window")
    l2.pack()
    l2.mainloop()

l1 = Label(root, text="This is a root window")
btn = Button(root, text="Click here to open another window", command=topwin)
l1.pack()
btn.pack()
root.mainloop()