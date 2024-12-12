#taken from this url: https://stackoverflow.com/questions/44634947/how-to-set-a-turtle-to-a-turtle-screen/44639041#44639041
#post had this title: how to set a turtle to a turtle screen
#This python code was the second in a response made by cdlane to the post. Here's what he said:
'''Or, we can simplify things a bit by letting the turtle module create the window, though we can shape 
it as needed through its method calls:
'''

from random import randint
from turtle import Turtle, Screen

health = 50
damage = 10
fight = randint(10, 20)
step = 0

def up():
    global step

    if step == fight:
        combat()
    step += 1
    turtle.seth(90)
    turtle.forward(10)

def down():
    global step

    if step == fight:
        combat()
    step += 1
    turtle.seth(-90)
    turtle.forward(10)

def left():
    global step

    if step == fight:
        combat()
    step += 1
    turtle.seth(180)
    turtle.forward(10)

def right():
    global step

    if step == fight:
        combat()
    step += 1
    turtle.seth(0)
    turtle.forward(10)

def combat():
    enemy = Turtle()
    enemy.up()
    eHealth = randint(20, 100)
    eDamage = randint(10, 20)

screen = Screen()
screen.setup(500, 350)  # visible portion of screen area
screen.screensize(600, 600)  # scrollable extent of screen area
turtle = Turtle()
turtle.up()

screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen()

screen.mainloop()