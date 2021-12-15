# Griffin Stepler, CIS345, iCourse, PE9
from tkinter import *
from tkinter import ttk
import random


def reset_game():
    """ initializes all data, resetting all variables """
    global count, answer, feedback, guess, counter, submit_button, progress
    guess.set('')
    answer = random.randint(1, 10)
    feedback.set('Enter Guess 1')
    count = 0
    counter.set(f'Guess {count}/3')
    submit_button['state'] = NORMAL
    progress['value'] = 0


def check_answer():
    """ tests if the user guessed the right number, gives feedback, tracks tries """
    global count, answer, feedback, guess, counter, submit_button, progress
    count += 1
    counter.set(f'Guess {count}/3')
    progress.step(100)

    try:
        g = int(guess.get())
    except (ValueError, TypeError):
        guess.set('0')
        g = 0

    if g == answer:
        feedback.set('You have won!')
        submit_button.config(state=DISABLED)
    elif g > answer:
        feedback.set(f'{g} was too high')
    else:
        feedback.set(f'{g} was too low')

    guess.set('')
    guess_textBox.focus()

    if count == 3:
        feedback.set(f'Correct Answer: {answer}')
        submit_button.config(state=DISABLED)


# window creation
window = Tk()
window.title('Guess Game')
window.geometry('250x195')
window.iconbitmap('pic.ico')

# global variables
answer = int()          # holds a random integer user needs to guess
count = int()           # starts at 0, counts up to 3
feedback = StringVar()  # linked to feedback label to tell user if guess is too high/low or win/loss
guess = StringVar()     # linked to textvariable of Entry textbox
counter = StringVar()   # set by count and linked to counter label to show "Guess {count}/3"

# creating menu_bar for window
# TODO: use .grid() to place GUI elements
menu_bar = Menu(window)  # creates new menu attached to window
window.config(menu=menu_bar)  # configures menu_bar as menu of previously declared window (Tk object)

file_menu = Menu(menu_bar, tearoff=False)  # creates another menu attached to menu_bar
menu_bar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Reset', command=reset_game)
file_menu.add_command(label='Exit', command=window.quit)

# setup of GuessingGame window
feedback_label = Label(window, textvariable=feedback, justify=LEFT)
feedback_label.grid(column=0, row=0, ipadx=10)

guess_textBox = Entry(window, textvariable=guess, justify=RIGHT)
guess_textBox.grid(column=0, row=1, padx=60)

progress = ttk.Progressbar(window, orient='horizontal', maximum=301, mode='determinate')  # TODO: add length= value
progress.grid(column=0, row=2, ipadx=10)

counter_label = Label(window, textvariable=counter, justify=CENTER)
counter_label.grid(column=0, row=3, ipadx=10)

submit_button = Button(window, text='Submit', command=check_answer)
submit_button.grid(column=0, row=4, ipadx=10)


if __name__ == '__main__':
    reset_game()
    window.mainloop()
