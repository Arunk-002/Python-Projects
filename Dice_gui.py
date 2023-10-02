from tkinter import *
import random as rand


num = ""
photo = ''
photo_dict = {1: "1.png", 2: "2.png", 3: "3.png", 4: "4.png", 5: "5.png", 6: "6.png"}


def roller():
    global num, photo, photo_dict
    num = rand.randint(1, 6)
    for i in photo_dict:
        if i == num:
            p_file = photo_dict[i]
    photo = PhotoImage(file=p_file)
    lbl.config(image=photo)


window = Tk()
window.title("Dice Roller 🎲")
window.geometry("700x700")
window.configure(bg="#9fc8fc")

btn = Button(window, text="Roll", command=roller, width=15, height=3)
btn.place(relx=0.5, rely=0.9, anchor=CENTER)

lbl = Label(image=photo)
lbl.place(relx=.1, rely=.1)

window.mainloop()
