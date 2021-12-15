# Griffin Stepler, CIS345, iCourse, A7
from tkinter import *
from tkinter import messagebox


def check_for_winner():
    """ checks game board for winning combinations """
    global board

    if (board[0].cget('text') == board[1].cget('text') == board[2].cget('text') == 'X' or
            board[3].cget('text') == board[4].cget('text') == board[5].cget('text') == 'X' or
            board[6].cget('text') == board[7].cget('text') == board[8].cget('text') == 'X' or
            board[0].cget('text') == board[3].cget('text') == board[6].cget('text') == 'X' or
            board[1].cget('text') == board[4].cget('text') == board[7].cget('text') == 'X' or
            board[2].cget('text') == board[5].cget('text') == board[8].cget('text') == 'X' or
            board[0].cget('text') == board[4].cget('text') == board[8].cget('text') == 'X' or
            board[2].cget('text') == board[4].cget('text') == board[6].cget('text') == 'X'):

        messagebox.showinfo('Winner', 'X wins the game!')
        reset_game_board()

    elif (board[0].cget('text') == board[1].cget('text') == board[2].cget('text') == 'O' or
          board[3].cget('text') == board[4].cget('text') == board[5].cget('text') == 'O' or
          board[6].cget('text') == board[7].cget('text') == board[8].cget('text') == 'O' or
          board[0].cget('text') == board[3].cget('text') == board[6].cget('text') == 'O' or
          board[1].cget('text') == board[4].cget('text') == board[7].cget('text') == 'O' or
          board[2].cget('text') == board[5].cget('text') == board[8].cget('text') == 'O' or
          board[0].cget('text') == board[4].cget('text') == board[8].cget('text') == 'O' or
          board[2].cget('text') == board[4].cget('text') == board[6].cget('text') == 'O'):

        messagebox.showinfo('Winner', 'O wins the game!')
        reset_game_board()


def reset_game_board():
    """ resets the values of all buttons to '' """
    global turn_count, board
    turn_count = 0
    for button in board:
        button.config(text='')


def update_button(index):
    """ updates the text value in the button, updates the board list """
    global turn_count, board
    turn_count += 1

    if board[index].cget('text') == '':
        if turn_count % 2 == 1:
            board[index].config(text='X', font='Times 10 bold', fg='red')
        else:
            board[index].config(text='O', font='Times 10 bold', fg='blue')
    else:
        messagebox.showinfo('Oops!', 'That space is already occupied')
        turn_count -= 1

    check_for_winner()

    if turn_count == 9:
        messagebox.showinfo('Game Over', "Cat's game; it's a tie!")
        reset_game_board()


# window creation
win = Tk()
win.geometry('280x213')
win.title('Tic Tac Toe')

# global variables
turn_count = 0  # counts the number of turns that have occurred, if == 9, forces game_over

# buttons for game board
b1 = Button(win, text='', borderwidth=2, width=12, height=4, command=lambda: update_button(0))
b2 = Button(win, text='', borderwidth=2, width=12, height=4, command=lambda: update_button(1))
b3 = Button(win, text='', borderwidth=2, width=12, height=4, command=lambda: update_button(2))
b4 = Button(win, text='', borderwidth=2, width=12, height=4, command=lambda: update_button(3))
b5 = Button(win, text='', borderwidth=2, width=12, height=4, command=lambda: update_button(4))
b6 = Button(win, text='', borderwidth=2, width=12, height=4, command=lambda: update_button(5))
b7 = Button(win, text='', borderwidth=2, width=12, height=4, command=lambda: update_button(6))
b8 = Button(win, text='', borderwidth=2, width=12, height=4, command=lambda: update_button(7))
b9 = Button(win, text='', borderwidth=2, width=12, height=4, command=lambda: update_button(8))

# aligning buttons onto grid
b1.grid(column=0, row=0)
b2.grid(column=1, row=0)
b3.grid(column=2, row=0)

b4.grid(column=0, row=1)
b5.grid(column=1, row=1)
b6.grid(column=2, row=1)

b7.grid(column=0, row=2)
b8.grid(column=1, row=2)
b9.grid(column=2, row=2)

# creating board for logic
board = [b1, b2, b3,
         b4, b5, b6,
         b7, b8, b9]

win.mainloop()
