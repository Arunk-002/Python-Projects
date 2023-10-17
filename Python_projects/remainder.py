from tkinter import *
from plyer import notification
from time import sleep


def set():
    window.destroy()
    sleep(int(time.get()))
    notification.notify(
        title="Reminder",
        message=message.get(),
        app_icon="D:\\Finished Projects\\Python projects\\Python_projects\\assets\\alert.ico",
    )


window = Tk()
window.geometry("300x300")
window.title("Remainder")

photo = PhotoImage(file="D:\\Finished Projects\\Python projects\\Python_projects\\assets\\remicon.png")
window.iconphoto(False, photo)
time = StringVar()
message = StringVar()
rem_lbl = Label(window, text="Remind :")
time_lbl = Label(window, text="Time :")
set_btn = Button(window, text="Set", command=set)
time_entry = Entry(window, textvariable=time)
rem_entry = Entry(window, textvariable=message)
rem_lbl.place(relx=0.2, rely=0.3)
rem_entry.place(rely=.3, relx=.4)
time_lbl.place(relx=.2, rely=.4)
time_entry.place(rely=.4, relx=.4)
set_btn.place(relx=.5, rely=.6)
window.mainloop()
