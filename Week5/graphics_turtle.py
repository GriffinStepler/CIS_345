import turtle

# setting up a turtle object
turtle.setup(1200, 800)
window = turtle.Screen()
window.reset()
window.bgcolor('white')

# creating a turtle object
t = turtle.Turtle()
t.turtlesize(5)
t.speed(1)  # 1 slowest, 10 fast, 0 is fastest (almost instant)

# turtle --> 0 heading points east
t.forward(100)  # pixels
t.left(90)  # degrees
t.hideturtle()  # arrow disappears
t.color('blue')  # color of the pointer/turtle
t.pencolor('red')  # color of the line
t.showturtle()  # arrow reappears
t.pensize(4)
t.forward(100)
t.right(45)
t.forward(300)
t.left(45)
t.backward(400)

t.penup()  # OR t.up() takes the "pen" off the surface; stops drawing while still navigating
t.pendown()  # OR t.down()

t.setheading(315)  # sets heading based on 0 = east
turtle.done()  # leaves window open until you manually close it
