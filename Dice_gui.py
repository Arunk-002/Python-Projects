from tkinter import *
import random as rand
from PIL import Image, ImageTk, ImageSequence

num = ""
photo = ""
img = None
photo_dict = {1: "1.png", 2: "2.png", 3: "3.png", 4: "4.png", 5: "5.png", 6: "6.png"}


def roller_img():
    global num, photo, photo_dict
    num = rand.randint(1, 6)
    for i in photo_dict:
        if i == num:
            p_file = photo_dict[i]
    photo = PhotoImage(file=p_file)
    lbl.config(image=photo)


def roll_animation():
    global img
    img = Image.open("dice.gif")
    for img in ImageSequence.Iterator(img):
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        window.update()
    roller_img()


window = Tk()
window.title("Dice Roller 🎲")
window.geometry("700x700")
window.configure(bg="#9fc8fc")

lbl = Label(window, image=photo)
lbl.pack()
btn = Button(window, text="Roll", command=roll_animation, width=15, height=3)
btn.pack()

window.mainloop()
