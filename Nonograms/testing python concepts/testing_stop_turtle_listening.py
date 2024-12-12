#borrowed entirely from a post about stopping turtle listening

from turtle import *

listening = False

def listen(listen_original=listen):
    global listening
    listen_original()
    listening = True

def unlisten():
    global listening
    listening = False

def setChar1():
    if not listening:
        return

    reset()
    for i in range(2):
        forward(200)
        left(170)

def setChar2():
    unlisten()

def setChar3():
    listen() 

onkey(setChar1, '1')
onkey(setChar2, '2')
onkey(setChar3, '3')
listen()

done()