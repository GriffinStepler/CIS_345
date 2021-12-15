from tkinter import *
from tkinter import ttk  # this allows us to specify whether we use the ttk or full tkinter version of classes

# create window
window = Tk()  # this builds a tkinter window object
window.geometry('600x400')  # dimensions of window in a single string
window.title('My Program')
# window.iconbitmap('small_lights.jpg')
# window['bg'] = 'gray'  # changes background to gray

# Menu section - widgits
menu_bar = Menu(window)  # specify which tkinter object we put it in
window.config(menu=menu_bar)  # links the window to your menu_bar, placing menu_bar into the menu setting/kwarg
file_menu = Menu(menu_bar, tearoff=False)  # tearoff is true by default
edit_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label='File', menu=file_menu)
menu_bar.add_cascade(label='Edit', menu=edit_menu)
file_menu.add_command(label='Exit', command=window.quit)
edit_menu.add_checkbutton(label='Info')

# label
Label(window, text='Name:').pack(side=LEFT, pady=20, padx=20)  # this is a static label; not usually good

# entry / text box
name_data = StringVar()
name_data.set('Griffin')
name_entry = Entry(window, textvariable=name_data, justify=CENTER)
name_entry.pack(side=LEFT)

results_lbl = Label(window, text='Label 2', bg='cornsilk', fg='Green')
results_lbl.pack(side=LEFT, pady=20, ipadx=50, ipady=30)


def button_click():
    global name_data, name_entry  # ensures you are referencing the global scope variable
    print(name_data.get())  # gets what's in the text box
    results_lbl.config(text=name_data.get())
    name_data.set('')
    pb['value'] += 100


# button
ok_button = Button(window, command=button_click, text='Ok')
ok_button.pack(side=BOTTOM, pady=10)

# progressbar
pb = ttk.Progressbar(window, orient='horizontal', maximum=301, mode='determinate')
pb.pack()

window.mainloop()  # last line in any GUI code block, runs until you hit 'x'
