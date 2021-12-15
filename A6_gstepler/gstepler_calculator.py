# Griffin Stepler, CIS345, iCourse, A6
import math
from tkinter import *


def press(button):
    """ gets button pressed, concatenates to end of expression to be evaluated """
    global expression, equation
    expression += str(button)
    equation.set(expression)


def equals():
    """ calculates/evaluates the content of expression
    sets equation value to be displayed and resets expression
    for next mathematical input """
    global expression, equation

    try:
        result = eval(expression)
        equation.set(result)
        expression = ''
    except ZeroDivisionError:
        equation.set('Error')
        expression = ''


def clear():
    global expression, equation
    expression = ''
    equation.set(expression)


def backspace():
    """ slices away the last element of the string """
    global equation, expression
    expression = expression[:-1]
    equation.set(expression)


def sqrt_press():
    global equation, expression
    result = math.sqrt(float(expression))
    equation.set(result)


# create window
win = Tk()
win.config(bg='blue')
win.geometry('240x280')
win.title('Calculator')

# GUI related variables
equation = StringVar()
expression = str()

# row 0 screen
display = Entry(win, textvariable=equation, width=30)
display.grid(column=0, row=0, columnspan=4, padx=10, pady=10)

# row 1 buttons
clear_button = Button(win, width=4, text='C', bg='red', fg='white', command=lambda: clear())
clear_button.grid(column=0, row=1, padx=10, pady=10)

back_button = Button(win, width=4, text='<-', bg='light gray', fg='black', command=lambda: backspace())
back_button.grid(column=1, row=1, padx=10, pady=10)

negative_button = Button(win, width=4, text='+/-', bg='light gray', fg='black', command=lambda: press('-'))
negative_button.grid(column=2, row=1, padx=10, pady=10)

sqrt_button = Button(win, width=4, text='sqrt', bg='light gray', fg='black', command=lambda: sqrt_press())
sqrt_button.grid(column=3, row=1, padx=10, pady=10)

# row 2 buttons
b_7 = Button(win, width=4, text='7', bg='gray', fg='white', command=lambda: press('7'))
b_7.grid(column=0, row=2, padx=10, pady=10)

b_8 = Button(win, width=4, text='8', bg='gray', fg='white', command=lambda: press('8'))
b_8.grid(column=1, row=2, padx=10, pady=10)

b_9 = Button(win, width=4, text='9', bg='gray', fg='white', command=lambda: press('9'))
b_9.grid(column=2, row=2, padx=10, pady=10)

divide_button = Button(win, width=4, text='/', bg='light gray', fg='black', command=lambda: press(' / '))
divide_button.grid(column=3, row=2, padx=10, pady=10)

# row 3 buttons
b_4 = Button(win, width=4, text='4', bg='gray', fg='white', command=lambda: press('4'))
b_4.grid(column=0, row=3, padx=10, pady=10)

b_5 = Button(win, width=4, text='5', bg='gray', fg='white', command=lambda: press('5'))
b_5.grid(column=1, row=3, padx=10, pady=10)

b_6 = Button(win, width=4, text='6', bg='gray', fg='white', command=lambda: press('6'))
b_6.grid(column=2, row=3, padx=10, pady=10)

multiply_button = Button(win, width=4, text='x', bg='light gray', fg='black', command=lambda: press(' * '))
multiply_button.grid(column=3, row=3, padx=10, pady=10)

# row 4 buttons
b_1 = Button(win, width=4, text='1', bg='gray', fg='white', command=lambda: press('1'))
b_1.grid(column=0, row=4, padx=10, pady=10)

b_2 = Button(win, width=4, text='2', bg='gray', fg='white', command=lambda: press('2'))
b_2.grid(column=1, row=4, padx=10, pady=10)

b_3 = Button(win, width=4, text='3', bg='gray', fg='white', command=lambda: press('3'))
b_3.grid(column=2, row=4, padx=10, pady=10)

subtract_button = Button(win, width=4, text='-', bg='light gray', fg='black', command=lambda: press(' - '))
subtract_button.grid(column=3, row=4, padx=10, pady=10)

# row 5 buttons
b_0 = Button(win, width=4, text='0', bg='gray', fg='white', command=lambda: press('0'))
b_0.grid(column=0, row=5, padx=10, pady=10)

dec_button = Button(win, width=4, text='.', bg='gray', fg='white', command=lambda: press('.'))
dec_button.grid(column=1, row=5, padx=10, pady=10)

equals_button = Button(win, width=4, text='=', bg='blue', fg='white', command=lambda: equals())
equals_button.grid(column=2, row=5, padx=10, pady=10)

add_button = Button(win, width=4, text='+', bg='light gray', fg='black', command=lambda: press(' + '))
add_button.grid(column=3, row=5, padx=10, pady=10)

win.mainloop()
