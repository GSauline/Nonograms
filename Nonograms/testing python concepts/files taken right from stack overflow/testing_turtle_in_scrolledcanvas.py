#found from https://stackoverflow.com/questions/14730475/python-turtle-window-with-scrollbars
#copied verbatim from that site

# import turtle

# win_width, win_height, bg_color = 2000, 2000, 'black'

# turtle.setup()
# turtle.screensize(win_width, win_height, bg_color)

# t = turtle.Turtle()
# #t.hideturtle()
# #t.speed(0)
# t.color('white')

# for _ in range(4):
#     t.forward(500)
#     t.right(90)

# turtle.done()

import turtle
import tkinter as tkinter

root = tkinter.Tk()
root.geometry('500x500-5+40') #added by me
cv = turtle.ScrolledCanvas(root, width=900, height=900)
cv.pack()

screen = turtle.TurtleScreen(cv)
screen.screensize(2000,1500) #added by me
t = turtle.RawTurtle(screen)
t.hideturtle()
t.circle(100)

root.mainloop()