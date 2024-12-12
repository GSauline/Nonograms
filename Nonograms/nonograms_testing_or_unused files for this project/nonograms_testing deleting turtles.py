import turtle as t

#testing deleting turtles
turt_in_row = 5
width, height = 450, 450
board_shift = 50  #amount by which the board will be shifted left and down to center it
switch_y = -100
turtle_gap = 30
for j in range(turt_in_row):
    for i in range(turt_in_row):
        globals()[f'block{i}_{j}'] = t.Turtle(shape="square")
        globals()[f'block{i}_{j}'].color('#E4ECED')
        globals()[f'block{i}_{j}'].penup()
        globals()[f'block{i}_{j}'].goto(i*turtle_gap-board_shift, j*turtle_gap-board_shift)
        # print(f'block{i}_{j}', 'go to',i*turtle_gap,j*turtle_gap)
globals()['block0_0'].color("red")
print("globals before deletion")
print(globals())
delay = input('type something and press enter\n')

for j in range(turt_in_row):
    for i in range(turt_in_row):
        globals()[f'block{i}_{j}'].clear()
        globals()[f'block{i}_{j}'].hideturtle()
        del globals()[f'block{i}_{j}']

print(globals())
globals()['block0_0'].goto(5,5)
