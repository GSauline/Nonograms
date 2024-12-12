import turtle as t

wn = t.Screen()
wn.bgcolor("red")
wn.setup(300, 200)
color = input("what is your favorite color?")
wn.bgcolor(color)
wn.setup(400, 500)

wn.mainloop()
