from tkinter import *
from tkinter import ttk


def rad_click(direction):
    global num
    print(num.get(), direction)


# build window called win
win = Tk()
win.geometry('600x400')
win.title('Example 3')

Label(win, text='peebo', bg='sky blue').grid(row=0, column=0, padx=30)
box = Frame(win, bg='sky blue', width=300, height=80,
            borderwidth=5, relief=RAISED)
box.grid(row=0, column=1, columnspan=2, sticky=E)
box.pack_propagate(0)  #

Label(box, text='Something', bg='sky blue').pack(anchor=NW)

num = IntVar()
num.set(1)

rad_btn1 = Radiobutton(box, bg='sky blue', variable=num, text='Up', value=1, indicatoron=0,
                       command=lambda: rad_click('U'))  # can use bind or command to connect to a function
rad_btn1.pack()

rad_btn2 = Radiobutton(box, bg='sky blue', variable=num, text='Down', value=2, indicatoron=0,
                       command=lambda: rad_click('D'))  # can use bind or command to connect to a function
rad_btn2.pack()

win.mainloop()
