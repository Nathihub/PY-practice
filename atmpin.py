from tkinter import *

root = Tk()
root.title("ATM PIN")
root.geometry("400x500")
root.configure(bg="#d0efff")

frame = Frame(master=root, height=200, width=360, bg="#d0efff")
frame.place(x=20, y=0)

entry1 = Entry(frame)
entry2 = Entry(frame, show="*")

def display():
    if entry1.get() == "" or entry2.get() == "":
        label = Label(frame, text="Please fill in all fields", bg="#d0efff", fg='white')
        label.pack(pady=5)
        return
    name = entry1.get()
    pin = entry2.get()
    greet = "Hey " + name
    message = "\nCongratulations for creating an account, " + name + "!"
    textbox.insert(END, greet)
    textbox.insert(END, message)
    label = Label(frame, text=message, bg="#d0efff", fg='black')
    label.pack(pady=5)

lbl1 = Label(frame, text="Name", bg="#3895D3", fg='white', width=12)
lbl2 = Label(frame, text="Pin", bg="#3895D3", fg='white', width=12)

textbox = Text(frame, height=5, width=40)
btn = Button(frame, text="Create Account", command=display, bg="blue", fg="white")

lbl1.place(x=20, y=20)
entry1.place(x=150, y=20)
lbl2.place(x=20, y=60)
entry2.place(x=150, y=60)
btn.place(x=130, y=100)
textbox.place(x=20, y=140)

nine =  Button(frame, relief=RAISED, text="9", bg="#d0efff", width=5, command=lambda: entry2.insert(END, "9"))
eight =  Button(frame, relief=RAISED, text="8", bg="#d0efff", width=5, command=lambda: entry2.insert(END, "8"))
seven =  Button(frame,relief=RAISED, text="7", bg="#d0efff", width=5, command=lambda: entry2.insert(END, "7"))
six =  Button(frame, relief=RAISED, text="6", bg="#d0efff", width=5, command=lambda: entry2.insert(END, "6"))
five =  Button(frame, relief=RAISED, text="5", bg="#d0efff", width=5, command=lambda: entry2.insert(END, "5"))
four =  Button(frame, relief=RAISED, text="4", bg="#d0efff", width=5, command=lambda: entry2.insert(END, "4"))
three =  Button(frame, relief=RAISED, text="3", bg="#d0efff", width=5, command=lambda: entry2.insert(END, "3"))
two =  Button(frame, relief=RAISED, text="2", bg="#d0efff", width=5, command=lambda: entry2.insert(END, "2"))
one =  Button(frame, relief=RAISED, text="1", bg="#d0efff", width=5, command=lambda: entry2.insert(END, "1"))
zero =  Button(frame, relief=RAISED, text="0", bg="#d0efff", width=5, command=lambda: entry2.insert(END, "0"))

nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ["#", 0, "*"]]

pad_frame = Frame(root, bg="#d0efff")
pad_frame.place(x=100, y=260)

for i in range(4):
    pad_frame.columnconfigure(i, weight=1, minsize=70)
    for j in range(0, 3):
        pad_frame.rowconfigure(j, weight=1, minsize=40)
        num_frame = Frame(master=pad_frame, relief=RAISED, borderwidth=5)
        num_frame.grid(row=i, column=j, padx=2, pady=2)
        numpad = Button(master=num_frame, text=nums[i][j], bg="#d0efff", width=5, command=lambda val=nums[i][j]: entry2.insert(END, str(val)))
        numpad.pack(padx=3, pady=3)
root.mainloop()