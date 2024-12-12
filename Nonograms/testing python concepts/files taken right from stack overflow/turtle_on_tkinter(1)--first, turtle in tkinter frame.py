#taken from this url: https://stackoverflow.com/questions/44634947/how-to-set-a-turtle-to-a-turtle-screen/44639041#44639041
#post had this title: how to set a turtle to a turtle screen
#This python code was the first in a response made by cdlane to the post. Here's what he said:
'''Python turtle was designed to either be embedded in a Tk window of your own making or 
in a Tk window of it's making. The two choices are invoked differently, but by mixing the 
commands you end up with both. Taking the custom Tk window approach that you started:
'''
from random import randint
from tkinter import *
from turtle import ScrolledCanvas, RawTurtle, TurtleScreen

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
    enemy = RawTurtle(canvas)
    enemy.up()
    eHealth = randint(20, 100)
    eDamage = randint(10, 20)

root = Tk()
canvas = ScrolledCanvas(root)
canvas.pack(side=LEFT)
screen = TurtleScreen(canvas)
turtle = RawTurtle(canvas)
turtle.up()

screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen()

screen.mainloop()