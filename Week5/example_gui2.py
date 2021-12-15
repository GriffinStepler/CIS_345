from tkinter import *
from tkinter import ttk


def year_selected(event):
    global combo_box, name, list_box
    selection = combo_box.get()
    print(combo_box.current(), selection)  # what is currently in the combo_box object
    name.set(selection)
    list_box.insert(END, selection)


def list_clicked(event):
    global list_box
    x = list_box.curselection()[0]
    print(x)


def event_handler_key(event):
    global name_entry
    valid_keys = ['a', 'b', '1', '2']
    if event.char not in valid_keys:
        return 'break'
    else:
        data = name.get()
        name.set(data + event.char)
        return 'break'


# build window called win
win = Tk()
win.config(bg='linen')
win.geometry('600x400')
win.title('Example 2')

# variables
name = StringVar(value='name')

Label(win, text='Name:', bg='linen').grid(row=0, column=0, ipadx=10)
name_entry = Entry(win, textvariable=name)
name_entry.grid(row=0, column=1, pady=20, sticky=W)
name_entry.bind('<Key>', event_handler_key)

# combobox
years = ['Freshman', 'Sophomore', 'Junior', 'Senior']
combo_box = ttk.Combobox(win, values=years)
combo_box.grid(row=1, column=1, sticky=W)
combo_box.bind('<<ComboboxSelected>>', year_selected)
combo_box.current(0)

#listbox
list_box = Listbox(win, width=23)
list_box.grid(row=2, column=1, sticky=W, pady=20)
list_box.insert(END, 'Item1')
list_box.bind('<Double-Button-1>', list_clicked)

win.mainloop()