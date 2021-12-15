# Griffin Stepler, CIS345, iCourse, A8
from tkinter import *
from tkinter import messagebox
from socket import *
from threading import Thread


def ip_entered(event):
    """ handles invalid entry into ip_entry box, if not valid key - do not add """
    global ip_address, ip_entry
    valid_keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '\b', '']

    if event.char not in valid_keys:
        return 'break'


def connect_func():
    """ connects the user to chat server, visually alters window and connect button,
     rebinds connect button to disconnect_fun """
    global ip_address, name, win, connect_button, win, chat_frame, sock

    ip = str(ip_address.get())  # create new IP variable for length + assignment
    screen_name = str(name.get())
    if len(ip) > 6 and name != '':
        try:
            # create socket object and bind to IP/port
            addr = (ip, 49000)
            sock = socket(AF_INET, SOCK_STREAM)
            sock.bind(addr)
            sock.send(screen_name.encode())
        except:  # super super exception handling!
            sock.close()
            sock = None
        else:
            x = Thread(target=receive_message, daemon=True)
            x.start()

        win.geometry('380x500')
        connect_button.config(text='Disconnect', bg='gold', command=disconnect_func)
        m_listbox.pack(side='left', fill='both')
        scrollbar.pack(side='right', fill='y')
        message_entry.grid(row=4, column=0, columnspan=2, padx=10)
        send_button.grid(row=4, column=2)
    else:
        messagebox.showinfo(title='Error', message='Please enter a full IPv4 address and screen name')


def disconnect_func():
    global ip_address, sock, name, connect_button, win, chat_frame

    # TODO: debug this
    sock = socket(AF_INET, SOCK_STREAM)
    try:
        sock.send('[Q]'.encode())  # this 'error' should not matter; this code only runs if sock is assigned
    except:  # more super super exception handling!
        pass
    finally:
        sock.close()
        sock = None

    # reset connect_button to original state
    connect_button.config(text='Connect', bg='SystemButtonFace', command=connect_func)
    chat_frame.grid_forget()
    message_entry.grid_forget()
    send_button.grid_forget()
    win.geometry('380x100')
    name.set('')


def receive_message():
    global sock

    while True:
        try:
            recv_message = sock.recv(1024)
        except OSError:
            recv_message = None
            break

        if not recv_message:
            disconnect_func()
            break

        m_listbox.insert(END, recv_message.decode())


def send_message(event):
    global sock, message

    client_message = str(message.get())
    if client_message == '[Q]':
        disconnect_func()
    elif client_message != '':
        try:
            sock.send(client_message.encode())
        except OSError:
            disconnect_func()
        message.set('')


def window_closed():
    global sock, win
    if sock:
        disconnect_func()
    win.quit()


def clear_entry(event):
    global message
    message.set('')


# window creation
win = Tk()
win.title('Instant Messenger')
win.geometry('380x100')

# Widget textvariables
ip_address = StringVar()
ip_address.set('127.0.0.1')  # default localhost address

name = StringVar()

c_button_text = StringVar()
c_button_text.set('Connect')

message = StringVar()
message.set('Type your message here')

# Widget creations
Label(win, text='IP Address:').grid(row=0, column=0, sticky=W, padx=10)
Label(win, text='Screen Name:').grid(row=1, column=0, sticky=W, padx=10)
ip_entry = Entry(win, textvariable=ip_address, width=40)
ip_entry.bind('<Key>', ip_entered)
name_entry = Entry(win, textvariable=name, width=40)
connect_button = Button(win, text='Connect', command=connect_func, width=50)
chat_frame = Frame(win, bg='maroon')

scrollbar = Scrollbar(chat_frame)
m_listbox = Listbox(chat_frame, yscrollcommand=scrollbar.set, width=50, height=20)
scrollbar.config(command=m_listbox.yview)

message_entry = Entry(win, textvariable=message, width=40)
message_entry.bind('<Button-1>', clear_entry)
message_entry.bind('<Return>', send_message)
send_button = Button(win, text='Send', width=8)
send_button.bind('<Button-1>', send_message)

# Widget placements
ip_entry.grid(row=0, column=1, columnspan=2, sticky=E, padx=10)
name_entry.grid(row=1, column=1, columnspan=2, sticky=E, padx=10)
connect_button.grid(row=2, column=0, columnspan=3, padx=10)
chat_frame.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

# main logic
win.protocol("WM_DELETE_WINDOW", window_closed)
win.mainloop()
