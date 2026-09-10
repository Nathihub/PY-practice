from datetime import date
from tkinter import *

window = Tk()
window.title("Demo Window")
window.geometry("400x300")

lbl = Label(text="Hey There", fg="white", bg="#072f5f", height=1, width=300)
lbl.pack()

name_entry = Entry()
name_entry.pack()
name_entry.get()

def display():
    name = name_entry.get()
    global message
    message = "welcome to the Application! \ntoday's date is:"
    greet = "Hello " + name + "\n"

    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box = Text(height=3)
text_box.pack()

btn = Button(text="Begin", command=display, height=1, bg="#1261a0", fg="white")
btn.pack()


window.mainloop()

