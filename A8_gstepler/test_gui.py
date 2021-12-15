from tkinter import *

# window
win = Tk()
win.title('Instant Messenger')
# win.geometry('380x100')
win.geometry('380x500')

# widgets
Label(win, text='IP Address:').grid(row=0, column=0, sticky=W, padx=10)
Label(win, text='Screen Name:').grid(row=1, column=0, sticky=W, padx=10)
ip_entry = Entry(win, text='127.0.0.1', width=40)
name_entry = Entry(win, width=40)
connect_button = Button(win, text='Connect', width=50)
chat_frame = Frame(win, bg='maroon')

ip_entry.grid(row=0, column=1, columnspan=2, sticky=E, padx=10)
name_entry.grid(row=1, column=1, columnspan=2, sticky=E, padx=10)
connect_button.grid(row=2, column=0, columnspan=3, padx=10)
chat_frame.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

scrollbar = Scrollbar(chat_frame)
m_listbox = Listbox(chat_frame, yscrollcommand=scrollbar.set, width=50, height=20)
scrollbar.config(command=m_listbox.yview)

m_listbox.pack(side='left', fill='both')
scrollbar.pack(side='right', fill='y')

message_entry = Entry(win, width=40)
send_button = Button(win, width=8, text='Send')

message_entry.grid(row=4, column=0, columnspan=2, padx=10)
send_button.grid(row=4, column=2)

win.mainloop()
