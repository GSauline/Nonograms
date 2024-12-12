#V1.1 This version has all the intializations in the original order, so it is not ready for functionalizing the setup 
#This version is slightly less optimized than V1.2
#This version does not have a working create_random_answer() function 

import turtle as t
import random

##############      Variable and Turtle Setup      ###############

#Assign Variables
turtle_gap = 30      #the gap between turtles on the gameboard
turt_in_row = 5     #the number of block turtles in 1 row/column of the board
num_shift = 5          # amount to shift numbers down to be centered on each row/col
font_setup = ("Verdana", 12, "normal")
block_state = True    #When true, clicking on a blank will draw a block. When false, it will draw an x
block_color_tuple = ((0.8941176470588236, 0.9254901960784314, 0.9294117647058824), (0.8941176470588236, 0.9254901960784314, 0.9294117647058824))

x_img_small = "X-for-nonogram-game.gif"
x_img_large = "X-for-nonogram-game larger.gif"
x_bg = "X-for-nonogram-game-with-bg.gif"   #this one has the neutral background color
heart_img_empty = 'empty-heart.gif' #found from https://www.shutterstock.com/image-vector/set-pixelated-heart-icons-digital-260nw-2320764891.jpg
heart_img_full = 'full-heart.gif' #found from https://www.shutterstock.com/image-vector/set-pixelated-heart-icons-digital-260nw-2320764891.jpg

#creating a blank board to begin
globals()[f'game_board_{turt_in_row}'] = [['-' for column in range(turt_in_row)] for row in range(turt_in_row)] 


# print ('game board has', len(globals()[f'game_board_{turt_in_row}']), 'rows and', len(globals()[f'game_board_{turt_in_row}'][0]), 'columns')


#conditional setup based on 5, 10, 15, or 20-board size
if turt_in_row ==5:
    width, height = 450, 450
    board_shift = 50  #amount by which the board will be shifted left and down to center it
    switch_y = -100
elif turt_in_row==10:
    width, height = 600, 600
    board_shift = 100
    switch_y = -150
elif turt_in_row == 15:
    width, height = 750,750
    board_shift = 200
    switch_y = -250   
elif turt_in_row == 20:
    width, height = 950, 950
    board_shift = 300
    switch_y = -360

#create the screen object, set up screen, add images
t.title('Nonagrams Game!')
wn = t.Screen()
wn.setup(width, height)
wn.tracer(False)
#These images will be used later
wn.addshape(x_img_small)
wn.addshape(x_img_large)
wn.addshape(x_bg)

#Creating the turtle to draw the border of the gameboard, numbers, and switch border
drawer = t.Turtle()
drawer.hideturtle()
drawer.penup()
#turtle for circling correct switch
circler = t.Turtle()
circler.penup()
circler.hideturtle()


##############      Gameboard    ###############

#dynamically create the turtles for the screen
#block0_0 through 0_4 should be in column 0 (first column-- x val of 0)
#block0_0 through 4_0 should be in row 0 (first row-- y val of 0)
for j in range(turt_in_row):
    for i in range(turt_in_row):
        globals()[f'block{i}_{j}'] = t.Turtle(shape="square")
        globals()[f'block{i}_{j}'].color('#E4ECED')
        globals()[f'block{i}_{j}'].penup()
        globals()[f'block{i}_{j}'].goto(i*turtle_gap-board_shift, j*turtle_gap-board_shift)
        print(f'block{i}_{j}', 'go to',i*turtle_gap,j*turtle_gap)
'''
#testing how to reference individual turtles that were dynamically created
globals()['block1_1'].color('purple')
'''

#### Comment out lines 88 - 152 if you want a "blank" board with no turtles besides the grid.
'''
#drawing vertical lines
drawer.setheading(90)
for i in range(turt_in_row + 1):
    drawer.goto(i*turtle_gap-.5*turtle_gap-board_shift,-.5*turtle_gap-board_shift)
    drawer.pendown()
    if i %5 == 0:
        drawer.pensize(4)
    else:
        drawer.pensize(1)
    drawer.forward(turt_in_row*turtle_gap)
    drawer.penup()

#drawing horizontal lines
drawer.setheading(0)
for i in range(turt_in_row+1):
    drawer.goto(-.5*turtle_gap-board_shift, i*turtle_gap-.5*turtle_gap-board_shift)
    drawer.pendown()
    if i %5 == 0:
        drawer.pensize(4)
    else:
        drawer.pensize(1)
    drawer.forward(turt_in_row*turtle_gap)
    drawer.penup()

#setting the numbers to be placed on the top and left of the screen
    #left
for i in range(turt_in_row):
    drawer.goto(-.75*turtle_gap-board_shift, i*turtle_gap-board_shift-num_shift)
    drawer.write('7 8 1 2 3', align = 'right', font = font_setup)
    #top
for i in range(turt_in_row):
    drawer.goto(i*turtle_gap-board_shift-num_shift, turt_in_row*turtle_gap-num_shift-board_shift)
    drawer.write('1\n1\n1', align = 'left', font = font_setup)

#Drawing the border around the "switch" to Switch from Solid blocks to X's
drawer.goto(-25,switch_y - 15)
drawer.showturtle()
drawer.pendown()
drawer.pensize(1)
drawer.fillcolor('#E4ECED')
drawer.begin_fill()
drawer.forward(50)
drawer.circle(15,180)
drawer.forward(50)
drawer.circle(15,180)
drawer.end_fill()
drawer.hideturtle()
'''

#Creating the turtles to act as the switches at the bottom of the screen
    #block switch
set_block = t.Turtle(shape="square")
set_block.penup()
set_block.goto(-15, switch_y)
set_block.shapesize(1.2)
#circling the Block switch, because block_state is true to start program
circler.goto(-15,switch_y-18)
circler.pendown()
circler.circle(18)
circler.penup()

    #X switch
set_x = t.Turtle(shape=x_img_small)
set_x.penup()
set_x.goto(15,switch_y)


##############      End Gameboard    ###############
    

##############      Functions       ###############

#This function does several things:
        #1) loops over all blank blocks on the board, only checking ones that have not yet been clicked (using original color tuple) 
        #2) Finds which block the click is closest to by finding the distance from x and y to all blank block coordinates
        #3) once we've found the correct block, check if block_state is true. If so, turn the block blue! If not, turn the block to x
        #4) If blank block --> full block, set  game_board at that cell = 1; if blank block --> x, set game_board at that cell = 0
        #5) print the game_board
def clicked(x,y):
    global block_state
    for j in range(turt_in_row):
        for i in range(turt_in_row):
            if globals()[f'block{i}_{j}'].color()==block_color_tuple:                       #only want to alter unclicked blocks
                if abs(x-globals()[f'block{i}_{j}'].xcor()) < 15 and abs(y-globals()[f'block{i}_{j}'].ycor()) < 15:     #finding the block we've clicked near 
                    print(f'block{i}_{j} clicked!')
                    if block_state==True:                      
                        globals()[f'block{i}_{j}'].color('blue')
                        globals()[f'game_board_{turt_in_row}'][j][i]='1'              #change the gameboard at that spot to a 1, for filled
                        print('Printing game_board...')
                        print_game_board(globals()[f'game_board_{turt_in_row}'])          

                    else:
                        globals()[f'block{i}_{j}'].shape(x_bg)
                        globals()[f'game_board_{turt_in_row}'][j][i]='0'              #change the gameboard at that spot to a 0, for x
                        print_game_board(globals()[f'game_board_{turt_in_row}'])

#this function either circles the Block Button or the X button at the bottom of the screen
def circler_fun(x_or_b):
    if x_or_b == "block":
        wn.tracer(False)
        circler.clear()
        circler.penup()
        circler.goto(-15,switch_y-18)
        circler.pendown()
        circler.circle(18)
        wn.tracer(True)
    if x_or_b == "x":
        wn.tracer(False)
        circler.clear()
        circler.penup()
        circler.goto(15,switch_y-18)
        circler.pendown()
        circler.circle(18)
        wn.tracer(True)

#this function controls the value of block_state and changes the look of the key at the bottom of the screen, based on block_state
def block_or_x():
    global block_state
    if block_state==True:
        block_state=False
        set_block.shapesize(1)
        set_x.shape(x_img_large)
        circler_fun("x")
    
    else:
        block_state=True
        set_block.shapesize(1.2)
        set_x.shape(x_img_small)
        circler_fun("block")        

'''This function is for debugging purposes. It prints the all the values of the matrix "game_board," such that row 0 
is the "bottom row," all the way up to the last row being printed on the top of the printed screen. To do this,
I had to reverse the order of the rows of the matrix when they get printed. That is why on line 223, the range 
function has the -1's in it.

The 3 possible values of game_board are '-', meaning that cell has not yet been clicked, '1', meaning a block has been 
placed in that cell, or '0', meaning an X has been placed in that cell.
'''

def print_game_board(game_board):
    for row in range(len(game_board)-1,-1,-1):
        print (' '.join(game_board[row]) )
        # print(globals()[f'game_board_{turt_in_row}'][row]) 

#This function is used to create a random answer board of 1's and 0's.
def create_random_answer():
    global turt_in_row
    answer_row = []
    answer = []
    #create each row of the answer
    for i in range(turt_in_row):
        answer_row.append(str(random.randint(0,1)))
    #put the rows together in one board
    for i in range(turt_in_row):
        answer.append(answer_row)
    
    
    

###############     Events      #################
#Handle the on_click events for each block turtle
for j in range(turt_in_row):
        for i in range(turt_in_row):
            globals()[f'block{i}_{j}'].onclick(clicked)


create_random_answer()
wn.listen()
wn.onkeypress(block_or_x,'x')

wn.tracer(True)
wn.mainloop()
