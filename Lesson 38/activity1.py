from tkinter import *
screen = Tk()
screen.title("Number pad")
screen.geometry('250x300')
nums = [[9,8,7],[6,5,4],[3,2,1],["#", 0, "*"]]
for i in range(4): 
    screen.columnconfigure(i,weight=1, minsize=75)
    screen.rowconfigure(i, weight = 1, minsize=50)
    for j in range(0,3): 
        frame = Frame(master=screen, relief=RAISED, borderwidth=1)
        frame.grid(column= j , row=i)
        label = Label(master=frame, text=nums[i][j], bg = "red")
        label.pack(padx=3, pady=3)

screen.mainloop()