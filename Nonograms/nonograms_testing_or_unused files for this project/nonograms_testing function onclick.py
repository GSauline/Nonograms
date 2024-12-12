import turtle as t

def clicked(x,y):
    print("the turtle has been clicked")
def turn_on_click():
    turty.onclick(clicked)

turty = t.Turtle(shape = 'turtle')
wn = t.Screen()

turn_on_click()
wn.mainloop()
