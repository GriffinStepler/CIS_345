# Griffin Stepler, CIS345, iCourse, PE10
from tkinter import *
from tkinter import ttk
from student_classes import Student, GradStudent


def rad_click(stype):
    if stype == 'G':
        thesis_entry.config(state='enabled')
    else:
        thesis_entry.config(state='disabled')


def save_student_click():
    global fname, lname, major, thesis, major, edit_mode

    if s_type == 'G':
        temp_stu = GradStudent(thesis, fname, lname, major)
    else:
        temp_stu = Student(fname, lname, major)

    if edit_mode:
        student_roster[edit_index] = temp_stu
        student_lbox.delete(edit_index)
        student_lbox.insert(edit_index, temp_stu)
        edit_mode = False
    else:
        student_roster.append(temp_stu)
        student_lbox.insert(END, temp_stu)


def edit_student(event):
    global edit_mode, fname, lname, thesis, major, edit_index, s_type
    edit_mode = True
    edit_index = student_lbox.curselection()[0]
    edited_student = student_roster[edit_index]

    if edited_student.isinstance(GradStudent):
        s_type = 'G'
        thesis = edited_student.thesis
        thesis_entry.config(state='enabled')
    else:
        s_type = 'S'
        thesis_entry.config(state='disabled')



# window setup
window = Tk()
window.geometry('400x600')  # TODO: alter dimensions to window
window.title('Student Entry Form')

# global variables
student_roster = list()
edit_mode = False
edit_index = int()

student_types = {'S': 'Student', 'G': 'Grad Student'}

fname = StringVar()
lname = StringVar()
thesis = StringVar()

majors = ['CIS', 'ACC', 'LES', 'FIN', 'MKT', 'BDA']
major = StringVar()

# frame setup
box = Frame(window, bg='gray', width=300, height=80, borderwidth=1, relief=SUNKEN)
box.grid(row=0, column=0, columnspan=2)
box.pack_propagate(1)

Label(box, text='Student Type', bg='gray').pack(anchor=NW)

# radio buttons
s_type = StringVar()
# TODO: verify commands are done properly; may prefer bind statements
rad_btn_s = Radiobutton(box, bg='gray', text='Student', variable=s_type,
                        value='S', command=lambda: rad_click('S'))
# rad_btn_s.bind('<Button-1>', rad_click)
rad_btn_s.pack()

rad_btn_gs = Radiobutton(box, bg='gray', text='Grad Student', variable=s_type,
                         value='G', command=lambda: rad_click('G'))
# rad_btn_gs.bind('<Button-1>', rad_click)
rad_btn_gs.pack()

# 3 Entry and Label widgets for fname, lname, thesis
Label(window, text='First Name', justify=LEFT).grid(column=0, row=1)
fname_entry = Entry(window, textvariable=fname)
fname_entry.grid(column=1, row=1)
fname_entry.bind('<Key>', edit_student)  # TODO: add proper binding

Label(window, text='Last Name', justify=LEFT).grid(column=0, row=2)
lname_entry = Entry(window, textvariable=lname)
lname_entry.grid(column=1, row=2)
lname_entry.bind('<Key>', edit_student)  # TODO: add proper binding

Label(window, text='Thesis', justify=LEFT).grid(column=0, row=3)
thesis_entry = Entry(window, textvariable=thesis)
thesis_entry.grid(column=1, row=3)
thesis_entry.bind('<Key>', edit_student)

# combobox to select major
major_cbox = ttk.Combobox(window, values=majors, textvariable=major)  # TODO: assign width=
major_cbox.current(0)
major_cbox.grid(column=0, row=4)

# save button
save_button = Button(window, command=save_student_click, text='Save')  # TODO: bind save_click
save_button.grid(column=1, row=5, sticky=E)

# listbox listing instructions
Label(window, text='(Double-Click to Edit a Student)').grid(column=0, row=6)
student_lbox = Listbox(window, bg='white')  # TODO: assign width=
student_lbox.grid(column=0, row=6, columnspan=2)

window.mainloop()
