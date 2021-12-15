from tkinter import *
from tkinter import ttk


def list_clicked(event):
    """ prints the index value of the current selection """
    global lb
    clicked_name = lb.curselection()[0]
    print(clicked_name)


def save_click():
    global name, lb
    data = name.get()
    lb.insert(END, data)
    pb['value'] += 50
    name.set('')


win = Tk()
win.geometry('600x500')
win.title('My Window')

# listbox
name_list = ['Dave', 'James', 'Tim']

lb = Listbox(win, width=20)
lb.grid(row=2, column=0, padx=10)
lb.bind('<Double-Button-1>', list_clicked)

for name in name_list:
    lb.insert(END, name)

# entry
name = StringVar()
name_entry = Entry(win, textvariable=name)
name_entry.grid(column=0, row=0, padx=10)

# save button
save_b = Button(win, text='Save', command=save_click)
save_b.grid(column=1, row=1, sticky=E)

# progressbar
pb = ttk.Progressbar(win, maximum=301, orient='horizontal', mode='determinate')
pb.grid(column=0, row=3, columnspan=2)

win.mainloop()