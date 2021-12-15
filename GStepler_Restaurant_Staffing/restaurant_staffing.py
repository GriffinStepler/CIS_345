# Griffin Stepler, CIS345, iCourse, Final Project
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import json


class Employee:
    """ Employee of the restaurant, includes following methods and properties: """
    def __init__(self, fname, lname, phone='(555)555-5555', email='',
                 food_handers='', positions=None, cook_type='', int_avg=0, hired='Not Hired'):
        self.first = fname
        self.last = lname
        self.phone = phone
        self.email = email
        self.food_handers = food_handers
        if positions is None:
            self.positions = list()
        else:
            self.positions = positions
        if 'C' in self.positions:
            self.cook_type = cook_type
        else:
            self.cook_type = ''
        self.int_avg = int_avg
        self.hired = hired

    @property
    def first(self):
        return self.__fname.capitalize()

    @first.setter
    def first(self, fname):
        if fname.isalpha():
            self.__fname = fname
        else:
            self.__fname = 'Unknown'

    @property
    def last(self):
        return self.__lname.capitalize()

    @last.setter
    def last(self, lname):
        if lname.isalpha:
            self.__lname = lname
        else:
            self.__lname = 'Unknown'

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, number):
        self.__phone = number

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def food_handers(self):
        return self.__food_handers

    @food_handers.setter
    def food_handers(self, fh):
        self.__food_handers = fh

    @property
    def cook_type(self):
        return self.__cook_type

    @cook_type.setter
    def cook_type(self, ct):
        self.__cook_type = ct

    @property
    def int_avg(self):
        return self.__int_avg

    @int_avg.setter
    def int_avg(self, val):
        self.__int_avg = val

    @property
    def hired(self):
        return self.__hired

    @hired.setter
    def hired(self, state):
        self.__hired = state

    def add_position(self, position):
        self.positions.append(position)

    def positions(self):
        return self.positions

    def list_positions(self):
        self.pos_string = ''
        for p in self.positions:
            self.pos_string = self.pos_string + p + ' '
        return self.pos_string

    def __str__(self):
        info = f'{self.first} {self.last}  -- {self.list_positions()} -- {self.int_avg} : {self.hired}'
        return info


def load_employees():
    """ loads employees.json, imports contents to dict, for each dict key create Employee object
     and append Employee object to candidates list """
    with open('employees.json', 'r') as fp:
        emps = json.load(fp)
        for v in emps:
            t_emp = Employee(fname=v['fname'], lname=v['lname'], phone=v['phone'], email=v['email'],
                             food_handers=v['food_handers'], positions=v['positions'], cook_type=v['cook_type'],
                             int_avg=v['int_avg'], hired=v['hired'])
            candidates.append(t_emp)

    messagebox.showinfo('Loaded', 'Successfully loaded information.')
    for c in candidates:
        emp_listbox.insert(END, c)


def save_info():
    """ saves candidate information back to .json file for non-volatile storage """
    candidate_list = list()
    for e in candidates:
        e_dict = dict()
        e_dict['fname'] = e.first
        e_dict['lname'] = e.last
        e_dict['phone'] = e.phone
        e_dict['email'] = e.email
        e_dict['food_handers'] = e.food_handers
        e_dict['positions'] = e.positions
        e_dict['cook_type'] = e.cook_type
        e_dict['int_avg'] = e.int_avg
        e_dict['hired'] = e.hired

        candidate_list.append(e_dict)

    with open('employees.json', 'w') as fp:
        json.dump(candidate_list, fp)

    messagebox.showinfo('Saved', 'Successfully saved information.')


def set_add_edit_mode():  # does this do anything
    global mode_edit, mode_delete, asd_button
    mode_edit = False
    mode_delete = False

    asd_button.config(text='Add')
    asd_button.config(command=lambda: add_interact())


def set_edit_mode(event):
    global mode_edit, mode_delete, asd_button, emp_listbox
    mode_edit = True
    mode_delete = False

    asd_button.config(text='Save')
    emp_listbox.bind('<Double-Button-1>', edit_emp)


def set_delete_mode():
    global mode_edit, mode_delete, asd_button, emp_listbox
    mode_edit = False
    mode_delete = True

    asd_button.config(text='Delete')
    asd_button.config(command=lambda: add_interact())
    # emp_listbox.bind('<Double-Button-1>', delete_emp)


def delete_interact():
    global edit_index, edited_emp, candidates, emp_listbox
    select_edit()

    mbox = messagebox.askquestion('Delete Employee', 'Are you sure you want to delete this Employee')

    if mbox == 'yes':
        candidates.pop(edit_index)
        emp_listbox.delete(edit_index)
    else:
        pass


def add_interact():
    global candidates, first_name, last_name, phone_no, email_addr, fh_cbox, ct_cbox, cook_var, dw_var, server_var
    global mode_edit, mode_delete
    pos = list()

    if fh_cbox.get() == 'Yes':
        fh = 'yes'
    else:
        fh = 'no'

    if ct_cbox.get() == 'Basic':
        ct = 'basic'
    elif ct_cbox.get() == 'Advanced':
        ct = 'advanced'
    else:
        ct = ''

    if cook_var.get() == 1:
        pos.append('C')
        toggle_cook('on')
    if dw_var.get() == 1:
        pos.append('DW')
    if server_var.get() == 1:
        pos.append('S')

    if cook_var.get() == 0:
        toggle_cook('off')

    temp_emp = Employee(fname=first_name.get(), lname=last_name.get(), phone=phone_no.get(), email=email_addr.get(),
                        positions=pos, food_handers=fh, cook_type=ct, int_avg=0, hired='Not Hired')

    if mode_edit:
        candidates[edit_index] = temp_emp
        emp_listbox.delete(edit_index)
        emp_listbox.insert(edit_index, temp_emp)
        mode_edit = False
        asd_button.config(text='Add')
    elif not mode_delete:
        candidates.append(temp_emp)
        emp_listbox.insert(END, temp_emp)

    clear_forms()


def edit_emp(event):
    """ edits contents of listbox based on double click """
    global candidates, first_name, last_name, phone_no, email_addr, fh_cbox, ct_cbox, cook_var, dw_var, server_var
    global edit_index, mode_edit, mode_delete

    mode_edit = True
    asd_button.config(text='Save')
    mode_delete = False

    select_edit()


def select_edit():
    global candidates, first_name, last_name, phone_no, email_addr, fh_cbox, ct_cbox, cook_var, dw_var, server_var
    global edit_index, mode_edit

    edit_index = emp_listbox.curselection()[0]
    edited_emp = candidates[edit_index]

    first_name.set(edited_emp.first)
    last_name.set(edited_emp.last)
    phone_no.set(edited_emp.phone)
    email_addr.set(edited_emp.email)

    if edited_emp.food_handers.casefold() == 'yes':
        fh_cbox.current(0)
    else:
        fh_cbox.current(1)

    if edited_emp.cook_type.casefold() == 'advanced':
        ct_cbox.current(1)
    elif edited_emp.cook_type.casefold() == 'basic':
        ct_cbox.current(0)

    pos = edited_emp.positions

    if 'C' in pos:
        cook_var.set(1)
        toggle_cook('on')
    else:
        cook_var.set(0)
        ct_cbox.current(2)
        toggle_cook('off')

    if 'DW' in pos:
        dw_var.set(1)
    else:
        dw_var.set(0)

    if 'S' in pos:
        server_var.set(1)
    else:
        server_var.set(0)


def toggle_cook(mode):
    global cook_var, ct_cbox
    if mode == 'on':
        ct_cbox.config(state='normal')
    elif mode == 'off':
        ct_cbox.config(state='disabled')


def clear_forms():
    global first_name, last_name, email_addr, phone_no, ct_cbox, fh_cbox, cook_var, dw_var, server_var

    first_name.set('')
    last_name.set('')
    email_addr.set('')
    phone_no.set('')

    fh_cbox.current(1)
    ct_cbox.current(2)

    cook_var.set(0)
    dw_var.set(0)
    server_var.set(0)


def emp_mgmnt_win():
    global lb_frame, fname_entry, lname_entry, email_entry, phone_entry, fname_label, lname_label, phone_label, dw_b
    global email_label, fh_label, ct_label, pos_label, fh_cbox, ct_cbox, cook_b, server_b, asd_button, delete_button

    # forget other widgets
    q1_label.grid_forget()
    q2_label.grid_forget()
    q3_label.grid_forget()
    q4_label.grid_forget()
    q1_rb_1.grid_forget()
    q1_rb_2.grid_forget()
    q1_rb_3.grid_forget()
    q1_rb_4.grid_forget()
    q1_rb_5.grid_forget()
    q2_rb_1.grid_forget()
    q2_rb_2.grid_forget()
    q2_rb_3.grid_forget()
    q2_rb_4.grid_forget()
    q2_rb_5.grid_forget()
    q3_rb_1.grid_forget()
    q3_rb_2.grid_forget()
    q3_rb_3.grid_forget()
    q3_rb_4.grid_forget()
    q3_rb_5.grid_forget()
    q4_rb_1.grid_forget()
    q4_rb_2.grid_forget()
    q4_rb_3.grid_forget()
    q4_rb_4.grid_forget()
    q4_rb_5.grid_forget()
    avg_button.grid_forget()
    avg_display_label.grid_forget()
    avg_display.grid_forget()
    hire_button.grid_forget()
    rate_button.grid_forget()

    # place frame
    lb_frame.grid(column=0, row=0, columnspan=6, padx=10, pady=5)
    # place entries and labels
    fname_label.grid(row=1, column=0, sticky=W, padx=10)
    fname_entry.grid(row=1, column=1)
    lname_label.grid(row=2, column=0, sticky=W, padx=10)
    lname_entry.grid(row=2, column=1)
    phone_label.grid(row=3, column=0, sticky=W, padx=10)
    phone_entry.grid(row=3, column=1)
    email_label.grid(row=4, column=0, sticky=W, padx=10)
    email_entry.grid(row=4, column=1)
    # place comboboxes and labels
    fh_label.grid(row=1, column=2, sticky=W, padx=10)
    fh_cbox.grid(row=1, column=3, padx=10)
    ct_label.grid(row=5, column=2, sticky=W, padx=10)
    ct_cbox.grid(row=5, column=3, padx=10)
    # place checkbuttons and labels
    pos_label.grid(row=2, column=2, sticky=W, padx=10)
    cook_b.grid(row=2, column=3, sticky=W)
    dw_b.grid(row=3, column=3, sticky=W)
    server_b.grid(row=4, column=3, sticky=W)
    # place buttons
    asd_button.grid(row=6, column=3, pady=5)
    delete_button.grid(row=7, column=3)


def int_rating_win():
    # forget other widgets
    fname_entry.grid_forget()
    lname_entry.grid_forget()
    email_entry.grid_forget()
    phone_entry.grid_forget()
    fname_label.grid_forget()
    lname_label.grid_forget()
    phone_label.grid_forget()
    email_label.grid_forget()
    fh_label.grid_forget()
    ct_label.grid_forget()
    pos_label.grid_forget()
    fh_cbox.grid_forget()
    ct_cbox.grid_forget()
    cook_b.grid_forget()
    dw_b.grid_forget()
    server_b.grid_forget()
    asd_button.grid_forget()
    delete_button.grid_forget()

    # place int_rating_widgets
    q1_label.grid(row=1, column=0, columnspan=7, padx=5, sticky=W)
    q2_label.grid(row=3, column=0, columnspan=7, padx=5, sticky=W)
    q3_label.grid(row=5, column=0, columnspan=7, padx=5, sticky=W)
    q4_label.grid(row=7, column=0, columnspan=7, padx=5, sticky=W)

    q1_rb_1.grid(row=2, column=1)
    q1_rb_2.grid(row=2, column=2)
    q1_rb_3.grid(row=2, column=3)
    q1_rb_4.grid(row=2, column=4)
    q1_rb_5.grid(row=2, column=5)

    q2_rb_1.grid(row=4, column=1)
    q2_rb_2.grid(row=4, column=2)
    q2_rb_3.grid(row=4, column=3)
    q2_rb_4.grid(row=4, column=4)
    q2_rb_5.grid(row=4, column=5)

    q3_rb_1.grid(row=6, column=1)
    q3_rb_2.grid(row=6, column=2)
    q3_rb_3.grid(row=6, column=3)
    q3_rb_4.grid(row=6, column=4)
    q3_rb_5.grid(row=6, column=5)

    q4_rb_1.grid(row=8, column=1)
    q4_rb_2.grid(row=8, column=2)
    q4_rb_3.grid(row=8, column=3)
    q4_rb_4.grid(row=8, column=4)
    q4_rb_5.grid(row=8, column=5)

    avg_display_label.grid(row=9, column=6)
    avg_display.grid(row=9, column=7, pady=5)
    avg_button.grid(row=10, column=7)
    rate_button.grid(row=11, column=7)


def calc_avg():
    global avg_rating, avg_display, var1, var2, var3, var4, avg
    avg = (var1.get() + var2.get() + var3.get() + var4.get()) / 4
    avg_rating.set(str(avg))

    if avg >= 3.8:
        hire_button.grid(row=12, column=7)
    else:
        hire_button.grid_forget()


def hire_emp():
    global avg
    rate_index = emp_listbox.curselection()[0]
    rated_emp = candidates[rate_index]
    rated_emp.hired = 'Hired'
    rated_emp.int_avg = avg
    candidates[rate_index] = rated_emp
    emp_listbox.delete(rate_index)
    emp_listbox.insert(rate_index, rated_emp)
    hire_button.grid_forget()


def rate_emp():
    global avg
    rate_index = emp_listbox.curselection()[0]
    rated_emp = candidates[rate_index]
    rated_emp.int_avg = avg
    candidates[rate_index] = rated_emp
    emp_listbox.delete(rate_index)
    emp_listbox.insert(rate_index, rated_emp)


# mode toggles
mode_edit = False
mode_delete = False

# list to hold employee objects
candidates = list()
# load_employees()  # used for testing, fills candidates with premade employees

# window creation
win = Tk()
win.title('Restaurant Staffing')
win.geometry('800x500')  # this is a good size

# widgets - menu_bar
menu_bar = Menu(win)
win.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=False)
mode_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label='File', menu=file_menu)
menu_bar.add_cascade(label='Mode', menu=mode_menu)

file_menu.add_command(label='Save All', command=lambda: save_info())
file_menu.add_command(label='Load', command=lambda: load_employees())

mode_menu.add_command(label='Employee Management', command=lambda: emp_mgmnt_win())
mode_menu.add_command(label='Interview Rating', command=lambda: int_rating_win())

# WINDOW CONTENTS FOR EMPLOYEE MANAGEMENT MODE
# frame
lb_frame = Frame(win)

lb_frame.grid(column=0, row=0, columnspan=6, padx=10, pady=5)

# widgets - listbox
emp_listbox = Listbox(lb_frame, width=60)
for candidate in candidates:
    emp_listbox.insert(END, candidate)
# emp_listbox.bind('<Double-Button-1>', edit_emp)
emp_listbox.bind('<Double-Button-1>', set_edit_mode)


emp_listbox.pack(fill='both')

# widgets - entries
first_name = StringVar()
last_name = StringVar()
phone_no = StringVar()
email_addr = StringVar()
fname_entry = Entry(win, width=30, textvariable=first_name)
lname_entry = Entry(win, width=30, textvariable=last_name)
phone_entry = Entry(win, width=30, textvariable=phone_no)
email_entry = Entry(win, width=30, textvariable=email_addr)

fname_label = Label(win, text='First Name:')
lname_label = Label(win, text='Last Name:')
phone_label = Label(win, text='Phone Number:')
email_label = Label(win, text='Email:')

# widgets - combobox
fh_vals = ['Yes', 'No']
fh_cbox = ttk.Combobox(win, values=fh_vals, width=10)
ct_vals = ['Basic', 'Advanced', '']
ct_cbox = ttk.Combobox(win, values=ct_vals, width=15)

fh_label = Label(win, text='Food Handers Card:')
ct_label = Label(win, text='Cook Type:')

# widgets - check buttons --> job types
cook_var = IntVar()
dw_var = IntVar()
server_var = IntVar()
cook_b = Checkbutton(win, text='Cook', variable=cook_var)
dw_b = Checkbutton(win, text='Dishwasher', variable=dw_var)
server_b = Checkbutton(win, text='Server', variable=server_var)
pos_label = Label(win, text='Positions:')

# widgets - add, delete button
asd_button = Button(win, text='Add', command=lambda: add_interact())
delete_button = Button(win, text='Delete', command=lambda: delete_interact())


# WINDOW CONTENTS FOR INTERVIEW RATING MODE
# labels
q1_label = Label(win, text='1. Verbal/Communication Skills')
q2_label = Label(win, text='2. Interpersonal Skills and Friendliness')
q3_label = Label(win, text='3. Math/Problem Solving Skills')
q4_label = Label(win, text='4. Applicable Work Experience')
avg_label = Label(win, text='Average Rating:')

# radiobuttons
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var1.set(0)
var2.set(0)
var3.set(0)
var4.set(0)

q1_rb_1 = Radiobutton(win, text='1', variable=var1, value=1)
q1_rb_2 = Radiobutton(win, text='2', variable=var1, value=2)
q1_rb_3 = Radiobutton(win, text='3', variable=var1, value=3)
q1_rb_4 = Radiobutton(win, text='4', variable=var1, value=4)
q1_rb_5 = Radiobutton(win, text='5', variable=var1, value=5)

q2_rb_1 = Radiobutton(win, text='1', variable=var2, value=1)
q2_rb_2 = Radiobutton(win, text='2', variable=var2, value=2)
q2_rb_3 = Radiobutton(win, text='3', variable=var2, value=3)
q2_rb_4 = Radiobutton(win, text='4', variable=var2, value=4)
q2_rb_5 = Radiobutton(win, text='5', variable=var2, value=5)

q3_rb_1 = Radiobutton(win, text='1', variable=var3, value=1)
q3_rb_2 = Radiobutton(win, text='2', variable=var3, value=2)
q3_rb_3 = Radiobutton(win, text='3', variable=var3, value=3)
q3_rb_4 = Radiobutton(win, text='4', variable=var3, value=4)
q3_rb_5 = Radiobutton(win, text='5', variable=var3, value=5)

q4_rb_1 = Radiobutton(win, text='1', variable=var4, value=1)
q4_rb_2 = Radiobutton(win, text='2', variable=var4, value=2)
q4_rb_3 = Radiobutton(win, text='3', variable=var4, value=3)
q4_rb_4 = Radiobutton(win, text='4', variable=var4, value=4)
q4_rb_5 = Radiobutton(win, text='5', variable=var4, value=5)

# calculate average button, display
avg_rating = StringVar()
avg_rating.set(0)
avg_button = Button(win, text='Calculate Average', command=lambda: calc_avg())
avg_display_label = Label(win, text=f'Average:')
avg_display = Label(win, textvariable=avg_rating)

# hire button
hire_button = Button(win, text='Hire', command=lambda: hire_emp())
rate_button = Button(win, text='Rate', command=lambda: rate_emp())

# main logic
emp_mgmnt_win()
win.mainloop()
