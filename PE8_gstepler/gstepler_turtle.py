# Griffin Stepler. CIS345, iCourse, PE8
import turtle

turtle.setup(800, 700)  # setting window dimensions
window = turtle.Screen()  # constructing screen

window.reset()
window.bgcolor('cornsilk')

t = turtle.Turtle()

t. color('blue')
t.pencolor('blue')
t.turtlesize(4)  # sets size of the triangle
t.speed(8)

# drawing 'G'
t.up()
t.setposition(-340, 100)  # sets position to upper left
t.down()
t.setheading(180)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(25)
t.left(90)
t.forward(25)

# drawing 'R'
t.up()
t.setposition(-320, 75)
t.down()
t.setheading(0)
t.forward(50)
t.left(90)
t.forward(25)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.up()
t.setposition(-320, 75)
t.down()
t.setposition(-270, 50)

# drawing 'I'
t.up()
t.setposition(-200, 100)
t.down()
t.setheading(180)
t.forward(50)
t.setposition(-225, 100)
t.setheading(270)
t.forward(50)
t.setposition(-200, 50)
t.setheading(180)
t.forward(50)

# drawing 'F'
t.up()
t.setposition(-130, 100)
t.down()
t.setheading(180)
t.forward(50)
t.left(90)
t.forward(50)
t.up()
t.setposition(-180, 75)
t.down()
t.setheading(0)
t.forward(50)

# drawing second 'f'
t.up()
t.setposition(-60, 100)
t.down()
t.setheading(180)
t.forward(50)
t.left(90)
t.forward(50)
t.up()
t.setposition(-110, 75)
t.down()
t.setheading(0)
t.forward(50)

# drawing second 'I'
t.up()
t.setposition(10, 100)
t.down()
t.setheading(180)
t.forward(50)
t.setposition(-15, 100)
t.setheading(270)
t.forward(50)
t.setposition(10, 50)
t.setheading(180)
t.forward(50)

# drawing 'N'
t.up()
t.setposition(30, 50)
t.down()
t.setheading(90)
t.forward(50)
t.setposition(80, 50)
t.setheading(90)
t.forward(50)

t.hideturtle()

turtle.done()
