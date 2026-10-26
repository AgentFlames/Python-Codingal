from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("500x500")
window.title("After-School Routine Checker")

heading1 = Label(window, "My After School Routine", font=("Arial",18, "bold"))
heading1.pack()

text1 = Label(window, "Enter your next after-school task:" , font=("Arial", 7, "bold"))
textbox1 = Entry()

def Last_Key_Pressed(event): 
    print(f"Last Key pressed: {event.char}")

def clear_routine(): 
    return "Routine area selected"

button1 = Button(window, background="pink", width= 75, height = 25 ) 