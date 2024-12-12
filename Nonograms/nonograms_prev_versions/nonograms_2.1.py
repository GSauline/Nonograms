#V2.1
#Clear function is buggy and don't use. This version does not have clear function as a possible choice under the onclicks. 
#The setup function appears to work, but there is an issue with the x for the switch at the bottom. Consider moving the X to the front? (see comment in vsn 2.2)


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

x_img_small = "images/X-for-nonagram-game.gif"
x_img_large = "images/X-for-nonagram-game larger.gif"
x_bg = "images/X-for-nonagram-game-with-bg.gif"   #this one has the neutral background color
heart_img_empty = 'empty-heart.gif' #found from https://www.shutterstock.com/image-vector/set-pixelated-heart-icons-digital-260nw-2320764891.jpg
heart_img_full = 'full-heart.gif' #found from https://www.shutterstock.com/image-vector/set-pixelated-heart-icons-digital-260nw-2320764891.jpg

#Create turtle and screen objects that will not need to be recreated when redrawing the board. 
#Assign values that need assigned only once. 
wn = t.Screen()
t.title('Nonagrams Game!')
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
#turtles to act as switches at the bottom of the screen
    #block switch
set_block = t.Turtle(shape="square")
set_block.penup()
    #X switch
set_x = t.Turtle(shape=x_img_small)
set_x.goto(50,50)
set_x.penup()


##############      End Variable and Turtle Setup      ###############




    

##############      Functions       ###############

#This function is to be used to reset the screen and variables. It then restarts the game.
####Clear function is buggy and don't use. I removed the clear function from the onclicks in this version.
def clear_screen_and_restart():
    choice = input("Are you sure you want to clear the screen and start again? Type 'y' or 'yes'. Type 'n' or 'no'.")
    global turt_in_row, game_board
    #delete the turtles in the gameboard
    if choice == 'yes' or choice == 'y':
        for j in range(turt_in_row):
            for i in range(turt_in_row):
                globals()[f'block{i}_{j}'].clear()
                globals()[f'block{i}_{j}'].hideturtle()
                del globals()[f'block{i}_{j}']
        #delete the writings of any turtles
        drawer.clear()
        circler.clear()

        #reassign the gameboard to be blank
        game_board = []
        print('globals after deletion', globals())

        #restart the game
        screen_setup()


#This function:
    #1) formats the screen based on the number of turtles in the row, 
    #2) creates the turtles for the board
    #3) draws the lines for the board
    #4) sets up/places the turtles to act as switches at the bottom of the screen
    #5) draws the border (and initial circle) around the switches at the bottom of the screen  
def screen_setup():
    ##Finishing screen, variable setup###
    global turt_in_row, width, height, switch_y, board_shift, turtle_gap, font_setup
    turt_in_row = int(input("How many turtles do you want in the row? You may select 5, 10, 15, or 20"))

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
    else:
        print("That is an invalid entry")
        screen_setup()
    print('switch_y', switch_y)
    #creating/redefining a blank board to begin
    globals()[f'game_board'] = [['-' for column in range(turt_in_row)] for row in range(turt_in_row)] 
    
    #creating a random answer
    create_random_answer()

    #set up screen, add images
    wn.setup(width, height)
    wn.tracer(False)


    ##Gameboard##

    #dynamically create the turtles for the screen
    #block0_0 through 0_4 should be in column 0 (first column-- x val of 0)
    #block0_0 through 4_0 should be in row 0 (first row-- y val of 0)
    for j in range(turt_in_row):
        for i in range(turt_in_row):
            globals()[f'block{i}_{j}'] = t.Turtle(shape="square")
            globals()[f'block{i}_{j}'].color('#E4ECED')
            globals()[f'block{i}_{j}'].penup()
            globals()[f'block{i}_{j}'].goto(i*turtle_gap-board_shift, j*turtle_gap-board_shift)
            # print(f'block{i}_{j}', 'go to',i*turtle_gap,j*turtle_gap)

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
    drawer.penup()


    #Setting up the turtles to act as the switches at the bottom of the screen
        #block switch
    set_block.goto(-15, switch_y)
    set_block.shapesize(1.2)
    #circling the Block switch, because block_state is true to start program
    circler.goto(-15,switch_y-18)
    circler.pendown()
    circler.circle(18)
    circler.penup()

        #X switch
    set_x.showturtle()
    set_x.goto(100,switch_y)

        #A message to indicate how to change from X to block
    drawer.penup()
    drawer.goto(0,switch_y-40)
    drawer.write("Use the 'x' key to change your click from blocks to X's.", align = 'center', font=font_setup)
    #This is to be added to the write function if I want to add back in the clear functionality. 
    #\n Use the 'c' key to clear the board and restart.
    #Also, need to change shift after switch_y to -55



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
            if globals()[f'block{i}_{j}'].color()==block_color_tuple:                       #only want to alter unclicked (whitish-blue blocks)
                if abs(x-globals()[f'block{i}_{j}'].xcor()) < 15 and abs(y-globals()[f'block{i}_{j}'].ycor()) < 15:     #finding the block we've clicked near 
                    print(f'block{i}_{j} clicked!')
                    if block_state==True:                      
                        globals()[f'block{i}_{j}'].color('blue')
                        globals()[f'game_board'][j][i]='1'              #change the gameboard at that spot to a 1, for filled
                        

                    else:
                        globals()[f'block{i}_{j}'].shape(x_bg)
                        globals()[f'game_board'][j][i]='0'              #change the gameboard at that spot to a 0, for x
                    print('Printing game_board...')
                    print_game_board(globals()[f'game_board'])          

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

#prints whatever game_board is input into this function (used to print both the current game_board and the answer_board)
def print_game_board(game_board):
    for row in range(len(game_board)-1,-1,-1):
        print (' '.join(game_board[row]) )
        # print(globals()[f'game_board_{turt_in_row}'][row]) 

def create_random_answer():
    global turt_in_row
    globals()['answer'] = []
    
    #create each row of the answer
    for j in range(turt_in_row):        #making each uniquely named row: answer_row_0, answer_row_1, etc.
        globals()[f'answer_row_{j}'] = []       
        for i in range(turt_in_row):     #for each row, appending 0's and 1's to fill out the row       
            globals()[f'answer_row_{j}'].append(str(random.randint(0,1)))
    
    #putting the rows together in one answer board
    for j in range(turt_in_row):
        globals()[f'answer'].append(globals()[f'answer_row_{j}'])    
    
    #deleting the answer_row_{j} variables
    for j in range(turt_in_row):
        del globals()[f'answer_row_{j}']

    #print this ANSWER board
    print('printing ANSWER board...')
    print_game_board(globals()[f'answer'])
    return globals()[f'answer']

###############     Events      #################
screen_setup()

#Handle the on_click events for each block turtle
for j in range(turt_in_row):
        for i in range(turt_in_row):
            globals()[f'block{i}_{j}'].onclick(clicked)


wn.listen()
wn.onkeypress(block_or_x,'x')
#wn.onkeypress(clear_screen_and_restart, 'c')

wn.tracer(True)
wn.mainloop()