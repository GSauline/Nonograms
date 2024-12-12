##This code is from my nonograms project. It is just making the X shape for the cursor.
import turtle as t
import math


#variables for XCursors
default_delay = 5
wn = t.Screen()

#variables for PolyRectangle
bar_len = 25                    #Used for rectangle is polyRectangle (part of X cursor)
bar_width = 2                   #Used for rectangle is polyRectangle (part of X cursor)
X_horiz = bar_len *math.sqrt(2) #Used for XCursors to place 2nd rectangle at correct spot


######################
# C. Setup only once per coding
######################


#Function for drawing the bar of the X's
#Adapted from a post at https://stackoverflow.com/questions/35834691/change-appearance-of-turtle/35837569#35837569
#Called within XCursors
def polyRectangle(turt, x, y, slant, length1, length2):
    turt.goto(x, y)
    turt.setheading(slant)

    turt.begin_poly()

    for count in range(2):
        turt.forward(length1)
        turt.left(90)
        turt.forward(length2)
        turt.left(90)

    turt.end_poly()
    print(turt.get_poly())
    return turt.get_poly()

#Function to create the red and black X turtle shapes, for use on the gameboard and on the bottom of the screen
#Adapted from a post at https://stackoverflow.com/questions/35834691/change-appearance-of-turtle/35837569#35837569
#Called presently at the top level, before screen_setup()
def XCursors():
    temporary = t.Turtle()
    screen = t.getscreen()

    delay = screen.delay()
    screen.delay(0)

    temporary.hideturtle()
    temporary.penup()


    X_turtle = t.Shape("compound")
    X_turtle_red = t.Shape("compound")

    left_side = polyRectangle(temporary, 0.35*bar_len, -0.375*bar_len, 45, bar_width, bar_len)  # left_side of X
    X_turtle.addcomponent(left_side, "black", "black")
    X_turtle_red.addcomponent(left_side, "red", "red")

    right_side = polyRectangle(temporary, 0.35*bar_len, 0.325*bar_len, 135, bar_width, bar_len)  #right side of X
    X_turtle.addcomponent(right_side, "black", "black")
    X_turtle_red.addcomponent(right_side, "red", "red")
    
    t.register_shape("X_turtle", X_turtle)
    t.register_shape("X_turtle_red", X_turtle_red)
    
    screen.delay(default_delay)
    del temporary

    for turt in t.turtles():
        turt.hideturtle()


#####Main code
XCursors()
turt_x = t.Turtle(shape = "X_turtle")
turt_x.goto(-100, 0)
turt_x.right(360)
turt_x_red = t.Turtle(shape = "X_turtle_red")
turt_x_red.goto(100,0)
turt_x_red.left(360)

wn.mainloop()