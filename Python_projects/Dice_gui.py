from tkinter import *
import random as rand
from PIL import Image, ImageTk, ImageSequence

num = ""
photo = ""
img = None
photo_dict = {1: "assets/1.png", 2: "assets/2.png", 3: "assets/3.png", 4: "assets/4.png", 5: "assets/5.png", 6: "assets/6.png"}


def roller_img():  # function to load the image of particular dice
    global num, photo, photo_dict
    num = rand.randint(1, 6)  # generates a random number and assigns to num
    for i in photo_dict:  # loops through the dict and finds the particular image
        if i == num:
            p_file = photo_dict[i]
    photo = PhotoImage(file=p_file)  # converts the image to tkinter printable object
    lbl.config(image=photo)


def roll_animation():
    global img
    img = Image.open("assets/dice.gif")
    for img in ImageSequence.Iterator(img):  # iterates through the img frame by frame
        img = ImageTk.PhotoImage(img)  # converts the image to tkinter printable object
        lbl.config(image=img)
        window.update()  # updates the window continously
    roller_img()


window = Tk()
window.title("Dice Roller 🎲")
window.geometry("600x600")
window.configure(bg="#9fc8fc")

lbl = Label(window, image=photo,borderwidth=1)
lbl.pack()
btn = Button(window, text="Roll", command=roll_animation, width=15, height=3)
btn.pack(side=BOTTOM)

window.mainloop()
