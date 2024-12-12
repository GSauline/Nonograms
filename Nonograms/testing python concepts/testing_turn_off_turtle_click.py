import turtle as t

yo = t.Turtle()
wn = t.Screen()
count = 0

def fun1(x,y):
    global count
    count += 1
    print('fun1 count', count)

def turn_off_click():
    print('you typed "b" to turn off clicks on yo')
    yo.onclick(None)

wn.listen()
wn.onkeypress(turn_off_click,'b')
yo.onclick(fun1)

t.mainloop()