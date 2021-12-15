# Griffin Stepler, CIS345, iCourse, PE10
from tkinter import *
from tkinter import ttk
from student_classes import Student, GradStudent


def save_student_click():
    """ executes on clicking save button, 
    Constructs Student/GradStudent object, adds to listbox"""
    global s_type, fname, lname, thesis, major, edit_mode

    if s_type.get() == 'G':
        temp_student = GradStudent(thesis.get(), fname.get(), lname.get(), major.get())
    else:
        temp_student = Student(fname.get(), lname.get(), major.get())

    if edit_mode:
        student_roster[edit_index] = temp_student
        student_listbox.delete(edit_index)
        student_listbox.insert(edit_index, temp_student)
        edit_mode = False
    else:
        student_roster.append(temp_student)
        student_listbox.insert(END, temp_student)

    clear_form()
    

def edit_student(Event):
    """ edits contents of listbox based on double click """
    global edit_mode, edit_index, s_type, fname, lname, thesis, major

    edit_mode = True
    edit_index = student_listbox.curselection()[0]
    edited_student = student_roster[edit_index]

    if isinstance(edited_student, GradStudent):
        s_type.set('')
        toggle_thesis()
        thesis = edited_student.thesis
    else:
        s_type.set('')
        toggle_thesis()

    fname.set(edited_student.fname)
    lname.set(edited_student.lname)
    major.set(edited_student.major)
    

def toggle_thesis():
    """ toggles thesis entry """
    global s_type
    if s_type.get() == 'G':
        thesis_entry.config(state='normal')
    else:
        thesis_entry.config(state='disabled')


def clear_form():
    """ clears text of all Entry widgets """
    global s_type, fname, lname, thesis
    s_type.set('')
    fname.set('')
    lname.set('')
    thesis.set('')


# window setup
win = Tk()
win.geometry('350x450')
win.title('Student Entry Form')

# global variables
student_roster = list()
edit_mode = False
edit_index = int()

student_types = {'S': 'Student', 'G': 'Grad Student'}

s_type = StringVar()
fname = StringVar()
lname = StringVar()
thesis = StringVar()

majors = ['CIS', 'FIN', 'ACC', 'MKT', 'BDA']
major = StringVar()

frame_color = 'light blue'

# frame setup
box = Frame(win, bg=frame_color, width=300, height=80, borderwidth=1, relief=SUNKEN)
box.grid(row=0, column=0, columnspan=2, padx=25)
box.pack_propagate(0)
Label(box, text='Student Type', bg=frame_color).pack(anchor=NW)

# radio buttons
rad_btn_s = Radiobutton(box, bg=frame_color, text='Student', variable=s_type,
                        value='S', command=toggle_thesis)
rad_btn_s.pack()

rad_btn_g = Radiobutton(box, bg=frame_color, text='GradStudent', variable=s_type,
                        value='G', command=toggle_thesis)
rad_btn_g.pack()

# Entry widgets
Label(win, text='First Name', justify=LEFT).grid(column=0, row=1)
fname_entry = Entry(win, textvariable=fname, justify=RIGHT)
fname_entry.grid(column=1, row=1)

Label(win, text='Last Name', justify=LEFT).grid(column=0, row=2)
lname_entry = Entry(win, textvariable=lname, justify=RIGHT)
lname_entry.grid(column=1, row=2)

Label(win, text='Thesis', justify=LEFT).grid(column=0, row=3)
thesis_entry = Entry(win, textvariable=thesis, justify=RIGHT)
thesis_entry.grid(column=1, row=3)

# Combobox
Label(win, text='Major', justify=LEFT).grid(column=0, row=4)
major_combo_box = ttk.Combobox(win, values=majors, textvariable=major)
major_combo_box.current(0)
major_combo_box.grid(column=1, row=4, columnspan=2)

# save button
save_button = Button(win, text='Save', command=save_student_click)
save_button.grid(column=1, row=6, sticky=E, padx=10)

# Listbox
Label(win, text='(Double-Click to Edit a Student').grid(column=0, row=7, columnspan=2)
student_listbox = Listbox(win, bg='white', width=50)
student_listbox.bind('<Double-Button-1>', edit_student)
student_listbox.grid(column=0, row=8, columnspan=2)

win.mainloop()
