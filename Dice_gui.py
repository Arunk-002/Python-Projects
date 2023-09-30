from tkinter import *
import random as rand
from PIL import ImageTk, Image
num = ""
photo=''

def roller():
    global num,photo
    # num = rand.randint(1, 6)
    # msg.config(text=num)
    photo = PhotoImage(file="1.png")
    lbl.config(image=photo)


window = Tk()
window.title("Dice Roller 🎲")
window.geometry("700x700")
window.configure(bg="#9fc8fc")


btn = Button(window, text="Roll", command=roller)
btn.place(relx=0.5, rely=0.9, anchor=CENTER)

lbl=Label(image=photo)
lbl.place(relx=.1,rely=0)


window.mainloop()
