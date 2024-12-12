#found from this post:
#https://stackoverflow.com/questions/35834691/change-appearance-of-turtle/35837569#35837569

#I was looking for a way to make my X's rotate. The solution MAY be to draw the X's as polygons. Let's see....

import turtle
import math

bar_len = 50
bar_width = 2
X_horiz = bar_len *math.sqrt(2)


def polyRectangle(t, x, y, slant, length1, length2):
    t.goto(x, y)
    t.setheading(slant)

    t.begin_poly()

    for count in range(2):
        t.forward(length1)
        t.left(90)
        t.forward(length2)
        t.left(90)

    t.end_poly()

    return t.get_poly()

#Create the red and black X turtle shapes, for use on the gameboard and on the bottom of the screen
def XCursors():
    temporary = turtle.Turtle()
    screen = turtle.getscreen()

    delay = screen.delay()
    screen.delay(0)

    temporary.hideturtle()
    temporary.penup()
    
    X_turtle = turtle.Shape("compound")
    X_turtle_red = turtle.Shape("compound")

    left_side = polyRectangle(temporary, 0.35*bar_len, -0.375*bar_len, 45, bar_width, bar_len)  # left_side of X
    X_turtle.addcomponent(left_side, "black", "black")
    X_turtle_red.addcomponent(left_side, "red", "red")

    right_side = polyRectangle(temporary, 0.35*bar_len, 0.325*bar_len, 135, bar_width, bar_len)  #right side of X
    X_turtle.addcomponent(right_side, "black", "black")
    X_turtle_red.addcomponent(right_side, "red", "red")
    
    turtle.register_shape("X_turtle", X_turtle)
    turtle.register_shape("X_turtle_red", X_turtle_red)
    
    del temporary

    for turt in turtle.turtles():
        turt.hideturtle()

        
'''
#made by me
def draw_X():
    temp = turtle.Turtle()
    temp.setheading(45)
    # temp.color('red')
    temp.forward(unVar2)
    temp.left(135)
    # temp.color('blue')
    temp.forward(unVar6)
    temp.left(135)
    # temp.color('pink')
    temp.forward(unVar2)
'''
XCursors()

circle = turtle.Turtle()
circle.shape("circle")
circle.shapesize(0.5)

black_X = turtle.Turtle(shape = "X_turtle")
red_X = turtle.Turtle(shape = "X_turtle_red")

#solely for testing the shapes' ability to move
for t in [black_X, red_X]:
    t.penup()
    # t.forward(100)
    # t.backward(100)

    # t.shapesize(2)
    # t.left(90)
    # t.forward(100)
    # t.left(45)
    # t.forward(100)
    t.right(360)
print(globals())

turtle.done()


