from tkinter import *
from plyer import notification
from time import sleep


# In this project three packages are used Tkinter,plyer,time.

def set():  # this function is called when the button is pressed
    # try catch block is used to capture any unwanted errors
    try:
        h = int(hour.get())
        m = int(minutes.get())
        sleep_time = (60 * (60 * h + m))  # equation to convert hour and minutes into seconds,since sleep function
        # only takes seconds as input
        window.destroy()
        sleep(sleep_time)
        notification.notify(
            title="Reminder",
            message=message.get(),
            app_icon="D:\\Finished Projects\\Python projects\\Python_projects\\assets\\alert.ico",
        )
    except:
        message.set("Error")


# window is initialized and configured
window = Tk()
window.configure(bg="#95dff0")
window.geometry("300x300")
window.title("Remainder")

photo = PhotoImage(file="D:\\Finished Projects\\Python projects\\Python_projects\\assets\\remicon.png")  # loads the
# image as PhotoImage object.
window.iconphoto(False, photo)  # loads the image as a icon
# variables are initialised inorder to take user input
time = IntVar()
message = StringVar()
hour = IntVar()
minutes = IntVar()
# labels
rem_lbl = Label(window, text="Remind :", bg="#95dff0")
time_lbl = Label(window, text="Time :", bg="#95dff0")
hr_lbl = Label(window, text="Hr", bg="#95dff0")
min_lbl = Label(window, text="Min", bg="#95dff0")

set_btn = Button(window, text="Set", command=set, bg="#aed5eb")
# entry
rem_entry = Entry(window, textvariable=message, bg="#aedfeb")
hr_entry = Entry(window, textvariable=hour, bg="#aedfeb")
min_entry = Entry(window, textvariable=minutes, bg="#aedfeb")
# position
rem_lbl.place(relx=0.2, rely=0.2)
rem_entry.place(rely=.2, relx=.4, height=50)
time_lbl.place(relx=.2, rely=.4)
hr_entry.place(rely=.4, relx=.4, width=30)
hr_lbl.place(rely=.4, relx=.5)
min_entry.place(rely=.5, relx=.4, width=30)
min_lbl.place(relx=.5, rely=.5)
set_btn.place(relx=.5, rely=.6, width=35)
window.mainloop()
