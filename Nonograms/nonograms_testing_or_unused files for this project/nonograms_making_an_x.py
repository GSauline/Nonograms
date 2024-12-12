import turtle as t

wn = t.Screen()

block = t.Turtle(shape="square")
block.color("#E4ECED")
drawer = t.Turtle()
drawer.hideturtle()
drawer.penup()
drawer.pencolor("black")
drawer.goto(block.xcor()-10,block.ycor()-10)
drawer.pendown()
drawer.goto(block.xcor()+10,block.ycor()+10)
drawer.penup()
drawer.goto(block.xcor()-10,block.ycor()+10)
drawer.pendown()
drawer.goto(block.xcor()+10,block.ycor()-10)


wn.mainloop()