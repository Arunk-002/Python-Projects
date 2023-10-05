from tkinter import *

calculation = ""


def press(num):
    global calculation
    calculation = calculation + str(num)
    equation.set(calculation)


def clear():
    global calculation
    calculation = ""
    equation.set("")


def result():
    try:
        global calculation
        res = str(eval(calculation))
        # eval function is not suitable for projects that are to be deployed
        # it allows hackers to access the system files

        equation.set(res)
        calculation = ""
    except:
        equation.set("ERROR")
        calculation = ""


window = Tk()
window.configure(bg="#80d4ff")
window.geometry("180x220")
window.title("Calculator")
equation = StringVar()
entry = Entry(window, textvariable=equation)
entry.grid(columnspan=4, rowspan=1, column=1, sticky="EWNS")
button1 = Button(text="0", command=lambda: press(0), bg="#80d4ff", height=2, width=5)
button1.grid(row=1, column=2, sticky="EWNS")
button2 = Button(text="1", command=lambda: press(1), bg="#80d4ff", height=2, width=5)
button2.grid(row=2, column=2, sticky="EWNS")
button3 = Button(text="2", command=lambda: press(2), bg="#80d4ff", height=2, width=5)
button3.grid(row=3, column=2, sticky="EWNS")
button4 = Button(text="3", command=lambda: press(3), bg="#80d4ff", height=2, width=5)
button4.grid(row=4, column=3, sticky="EWNS")
button5 = Button(text="4", command=lambda: press(4), bg="#80d4ff", height=2, width=5)
button5.grid(row=1, column=3, sticky="EWNS")
button6 = Button(text="5", command=lambda: press(5), bg="#80d4ff", height=2, width=5)
button6.grid(row=2, column=3, sticky="EWNS")
button7 = Button(text="6", command=lambda: press(6), bg="#80d4ff", height=2, width=5)
button7.grid(row=3, column=3, sticky="EWNS")
button8 = Button(text="7", command=lambda: press(7), bg="#80d4ff", height=2, width=5)
button8.grid(row=3, column=4, sticky="EWNS")
button9 = Button(text="8", command=lambda: press(8), bg="#80d4ff", height=2, width=5)
button9.grid(row=1, column=4, sticky="EWNS")
button10 = Button(text="9", command=lambda: press(9), bg="#80d4ff", height=2, width=5)
button10.grid(row=2, column=4, sticky="EWNS")
btn = Button(text="+", command=lambda: press("+"), bg="#80d4ff", height=2, width=5)
btn.grid(row=1, column=1, sticky="EWNS")
btn1 = Button(text="-", command=lambda: press("-"), bg="#80d4ff", height=2, width=5)
btn1.grid(row=2, column=1, sticky="EWNS")
btn3 = Button(text="/", command=lambda: press("/"), bg="#80d4ff", height=2, width=5)
btn3.grid(row=3, column=1, sticky="EWNS")
btn4 = Button(text="x", command=lambda: press("*"), bg="#80d4ff", height=2, width=5)
btn4.grid(row=4, column=1, sticky="EWNS")
btn2 = Button(text="=", command=result, bg="#80d4ff", height=2, width=5)
btn2.grid(row=5, columnspan=4, column=1, sticky="EWNS")
btn5 = Button(text="C", command=clear, bg="#80d4ff", height=2, width=5)
btn5.grid(row=4, column=2, sticky="EWNS")
btn6 = Button(text='.', command=lambda: press('.'), bg="#80d4ff", height=2, width=5)
btn6.grid(row=4, column=4, sticky="EWNS")

window.mainloop()
