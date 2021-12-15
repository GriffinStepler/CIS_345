import turtle

def move_forward():
    global player1
    player1.forward(15)


def move_backward():
    global player1
    player1.backward(15)


def turn_left():
    global player1
    heading = player1.heading()
    player1.setheading(heading + 15)


def turn_right():
    global player1
    heading = player1.heading()
    player1.setheading(heading - 15)


# setup for turtle window
turtle.setup(1200,800)
window = turtle.Screen()
window.bgcolor('light gray')

# Player 1
player1 = turtle.Turtle()
player1.turtlesize(3)
player1.color('red')
player1.pencolor('red')
player1.up()
player1.setposition(-300, 0)
player1.setheading(0)
player1.down()

# Player 2
player2 = turtle.Turtle()
player2.turtlesize(3)
player2.color('blue')
player2.pencolor('blue')
player2.up()
player2.setposition(300, 0)
player2.setheading(180)
player2.down()


# link a keypress event to player1 functions above
window.onkey(move_forward, 'w')
window.onkey(move_backward, 's')
window.onkey(turn_right, 'd')
window.onkey(turn_left, 'a')

# link player 2 to mouse click event
window.onclick(player2.goto)

window.listen()

turtle.done()