#V2.4 
#From 2.3:
    #clear works NEARLY PERFECTLY!! (after clearing, I need to use x to switch the block_state, then all the turtles "wake up")
    #setup function now works correctly!
    #decentralized functions
#new: working on the correct answer engine
#Working: the check_cell value function, the check_row function, check_col function. 
    #Issue: I want the X's to rotate in a pretty way, but they presently do not. Need to find a solution so they actually appear to rotate.
#Working: the numbers on the left of the screen. Two functions make this happen:
    #get_row_numbers()
    #I modified write_numbers to write the row numbers
#Then, add in lives (not done at all yet)
#Then, add in intentional images!
#Features to add:
    #The game should self-correct (take a life)
    #You should not need to add X's to complete a row (only blocks)
        #Once you have correct blocks in correct spot, fill in rest of row with X's

import turtle as t
import random

##############      Variable and Turtle Setup      ###############

#Assign Variables
turtle_gap = 30      #the gap between turtles on the gameboard
turt_in_row = 5     #the number of block turtles in 1 row/column of the board
num_shift = 5          # amount to shift numbers down to be centered on each row/col
font_setup = ("Verdana", 12, "normal")
block_color_tuple = ((0.8941176470588236, 0.9254901960784314, 0.9294117647058824), (0.8941176470588236, 0.9254901960784314, 0.9294117647058824))

x_img_small = "images/X-for-nonogram-game-with-color-bg.gif"
x_img_large = "images/X-for-nonogram-game larger.gif"
x_bg = "images/X-for-nonogram-game-with-bg.gif"   #this one has the neutral background color
heart_img_empty = 'empty-heart.gif' #found from https://www.shutterstock.com/image-vector/set-pixelated-heart-icons-digital-260nw-2320764891.jpg
heart_img_full = 'full-heart.gif' #found from https://www.shutterstock.com/image-vector/set-pixelated-heart-icons-digital-260nw-2320764891.jpg

#Create turtle and screen objects that will not need to be recreated when redrawing the board. 
#Assign values that need assigned only once. 
wn = t.Screen()
t.title('Nonograms Game!')
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
set_x.penup()




##############      Functions       ###############
'''Function set #1: setup functions
They are needed once per level to format/ draw/ create the functionality of the board. 
clear_screen_and_restart
screen_setup
switch_setup
draw_lines
create_random_answer
create_custom_5_answer_testing
get_row_numbers
get_col_numbers
write_numbers
turn_on_clicks'''
#This function is to be used to reset the screen and variables. It then restarts the game. Goal: use it to reset after a level change.
def clear_screen_and_restart():
    choice = input("Are you sure you want to clear the screen and start again? Type 'y' or 'yes'. Type anything else for no.")
    global turt_in_row, game_board, drawer, circler, set_x, set_block, wn
    #delete the turtles in the gameboard
    if choice == 'yes' or choice == 'y':
        wn.tracer(False)
        for j in range(turt_in_row):
            for i in range(turt_in_row):
                globals()[f'block{i}_{j}'].clear()
                globals()[f'block{i}_{j}'].hideturtle()
                del globals()[f'block{i}_{j}']
        #delete the writings of any other turtles
        drawer.clear()
        circler.clear()

        #hide these turtles
        set_x.hideturtle()
        set_block.hideturtle()

        #reassign the gameboard and answer to be blank
        game_board = []
        answer = []
        print('globals after deletion', globals())

        wn.tracer(True)
        #restart the game
        screen_setup()
        block_or_x()

#This function:
    #1) formats the screen based on the number of turtles in the row, 
    #2) creates the turtles for the board
    #3) draws the lines for the board
    #4) sets up/places the turtles to act as switches at the bottom of the screen
    #5) draws the border (and initial circle) around the switches at the bottom of the screen 
    #6) Turns on the onclick() for each turtle on game board by calling turn_on_clicks() 
def screen_setup():
    ##Finishing screen, variable setup###
    global turt_in_row, width, height, switch_y, board_shift, turtle_gap, font_setup
    turt_in_row = int(input("How many turtles do you want in the row? You may select 5, 10, 15, or 20\n"))

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
        switch_y = -350
    else:
        print("That is an invalid entry")
        screen_setup()
    print('switch_y', switch_y)
    #creating/redefining a blank board to begin
    globals()[f'game_board'] = [['-' for column in range(turt_in_row)] for row in range(turt_in_row)] 
    
    
    #creating a random answer
    create_random_answer()
    
    '''
    #create a custom 5-by-5 (only for testing)
    create_custom_5_answer_testing()
    '''

    ''' will be done in the write_rows function
    #get row nums
    print(get_row_numbers())
    '''

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

    #draw lines for gameboard
    draw_lines()

    #draw the numbers along the top and left of the board, based on answer (function in progress)
    write_numbers()

    #Drawing the switch and setting up the turtles for the "switch" at the bottom of the screen.
    #The switch is used to change the clicks from X's to blocks.
    switch_setup()

    #turn on click functionality for the already-created turtles on the board
    turn_on_clicks(turt_in_row)

#Formats the "switch" at the bottom of the screen and its turtles
def switch_setup():
    global switch_y, drawer, set_block, circler, set_x, font_setup
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


    #This variable will control the switch at the bottom of the screen (T = blocks drawn, F = X's drawn)
    globals()['block_state'] =  True
    #Setting up the turtles to act as the switches at the bottom of the screen
        #block switch
    set_block.goto(-15, switch_y)
    set_block.showturtle()
    set_block.shapesize(1.2)
    #circling the Block switch, because block_state is true to start program
    circler.goto(-15,switch_y-18)
    circler.pendown()
    circler.circle(18)
    circler.penup()

        #X switch
    set_x.goto(15,switch_y)
    set_x.showturtle() 
    set_x.shape("turtle")               #changing to arbitrary shape and back to X will move the X to the "top" above oval
    set_x.shape(x_img_small)

        #A message to indicate how to change from X to block
    drawer.penup()
    drawer.goto(0,switch_y-55)
    drawer.write("Use the 'x' key to change your click from blocks to X's.\n Use the 'c' key to clear the board and restart.", align = 'center', font=font_setup)

#Draws the horizontal and vertical lines
def draw_lines():
    global drawer, turtle_gap, board_shift, turt_in_row
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

#Creates a random grid answer, based on turt_in_row
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

#Creates a custom 5-by-5 game board
def create_custom_5_answer_testing():
    globals()['answer'] = []
    
    #create each row of the answer
    for j in range(5):        #making each uniquely named row: answer_row_0, answer_row_1, etc.
        globals()[f'answer_row_{j}'] = []       
    
    globals()['answer_row_0'] = ['0', '1', '0', '1', '0']
    globals()['answer_row_1'] = ['0', '0', '0', '0', '1']
    globals()['answer_row_2'] = ['1', '1', '1', '1', '1']
    globals()['answer_row_3'] = ['0', '0', '0', '0', '0']
    globals()['answer_row_4'] = ['1', '0', '1', '0', '1']

    #putting the rows together in one answer board
    for j in range(5):
        globals()[f'answer'].append(globals()[f'answer_row_{j}'])    
    
    #deleting the answer_row_{j} variables
    for j in range(5):
        del globals()[f'answer_row_{j}']

    #print this ANSWER board
    print('printing CUSTOM ANSWER board...')
    print_game_board(globals()[f'answer'])
    return globals()[f'answer']

#gets the numbers that will be displayed on the left of the screen
def get_row_numbers():
    global turt_in_row
    
    globals()['row_nums'] = []
    #creating one number list per row of answer. This will start at row 0, the bottom of the image.
    for j in range(turt_in_row):
        globals()[f'row_nums_list_{j}'] = []
    
    for j in range(turt_in_row):        #loop over every row
        temp_sum = 0
        # print('new row')
        for i in range(turt_in_row):        #loop over every index in the row
            # print("current cell value is", globals()['answer'][j][i])

            if globals()['answer'][j][i]=='1' and i != (turt_in_row - 1):
                temp_sum += 1
                # print('there is a 1 here. temp_sum =', temp_sum)
            elif globals()['answer'][j][i]=='1' and i == (turt_in_row -1):
                temp_sum += 1
                # print('there is a 1 at the end of the row')
                globals()[f'row_nums_list_{j}'].append(str(temp_sum))
                temp_sum = 0
            elif globals()['answer'][j][i] == '0' and temp_sum != 0:
                globals()[f'row_nums_list_{j}'].append(str(temp_sum))
                temp_sum = 0
        
        # print('nums for row', j, globals()[f'row_nums_list_{j}'])
        globals()['row_nums'].append(globals()[f'row_nums_list_{j}'])
        del globals()[f'row_nums_list_{j}']
    return globals()['row_nums']

#gets the numbers that will be displayed on the top of the screen
def get_col_numbers():
    pass
    '''pseudocode:
    First, create empty col_nums_list{i} for each column
    Then, loop over every value in each column to create temp_col_list for each column of the answer

    Then, given a col of the answer:
        for each cell in the column:
            if a given cell is a 1, 
                add 1 to a temp_sum
            if a given cell is 0 and the temp_sum is non-zero
                append temp_sum to the col_nums_list{i} 
    '''

###Function in progress###
#based on the answer, this function will eventually determine all the numbers that go on the left and top of the screen and write them.
def write_numbers(): 
    row_nums = get_row_numbers()

    #actually drawing the row numbers on the left
    for j in range(len(row_nums)):
        drawer.goto(-.75*turtle_gap-board_shift, j*turtle_gap-board_shift-num_shift)
        drawer.write(" ".join(row_nums[j]), align = 'right', font = font_setup)
        
        #top column numbers
    for i in range(turt_in_row):
        drawer.goto(i*turtle_gap-board_shift-num_shift, turt_in_row*turtle_gap-num_shift-board_shift)
        drawer.write('1\n1\n1', align = 'left', font = font_setup)
####In progress###

#Handle the on_click events for each block turtle
def turn_on_clicks(num_in_row):
    for j in range(num_in_row):
        for i in range(num_in_row):
            globals()[f'block{i}_{j}'].onclick(clicked)



'''Function set #2: switch functions
The following two functions are used multiple times per level, and they control the ability to use 'x' to switch from clicking blocks to 
clicking X's. They also control the visuals of the "switch" at the bottom of the screen.'''
#this function either circles the Block Button or the X button at the bottom of the screen
def circler_fun(x_or_b):
    if x_or_b == "block":
        wn.tracer(False)
        circler.clear()
        circler.penup()
        circler.goto(-15,switch_y-18)
        circler.pendown()
        circler.circle(18)
        circler.penup()
        wn.tracer(True)
    if x_or_b == "x":
        wn.tracer(False)
        circler.clear()
        circler.penup()
        circler.goto(15,switch_y-18)
        circler.pendown()
        circler.circle(18)
        circler.penup()
        wn.tracer(True)

#this function controls the value of block_state and changes the look of the "switch" at the bottom of the screen, based on block_state
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



'''Function set #3: clicking function
The brain of the game! This function controls everything that happens each time we click on one of the turtles on the board'''
#This function does several things:
        #1) loops over all blank blocks on the board, only checking ones that have not yet been clicked (using original color tuple) 
        #2) Finds which block the click is closest to by finding the distance from x and y to all blank block coordinates
        #3) once we've found the correct block, check if block_state is true. If so, turn the block blue! If not, turn the block to x
        #4) If blank block --> full block, set  game_board at that cell = 1; if blank block --> x, set game_board at that cell = 0
        #5) print the game_board
def clicked(x,y):
    global block_state, turt_in_row, block_color_tuple, answer
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
                    
                    #The following should happen whether block_state is true or not. 
                    #It needs to happen every time we have clicked on a cell and changed it to an X or block.
                    check_cell(j,i)                                 #this should check that the cell has been entered correctly
                    check_row(j)                                    #this should check that the whole row has been entered correctly
                    check_col(i)                                    #this should check that the whole column has been entered correctly
                    #debugging print statements
                    # print('\n\nPrinting answer...')
                    # print_game_board(globals()[f'answer'])
                    print('Printing game_board...')
                    print_game_board(globals()[f'game_board'])
                              


'''Function set #4: checking correct
These functions will check that the rows/ columns have correctly been filled in
check_cell
check_row
check_col
turt_dance (used to move the turtles a bit when a row/ column is correct)'''
def check_cell(current_row_num, current_col_num):
    if globals()['game_board'][current_row_num][current_col_num]== globals()['answer'][current_row_num][current_col_num]:
        print("Congrats! This was the correct thing to put in this cell!")
    else:
        print("Boo! Wrong thing in this cell!")

def check_row(current_row_num):  #current_row_num should be a value from 0 to turt_in_row - 1.
    global turt_in_row
    match_count = 0
    if '-' not in globals()['game_board'][current_row_num]:
        for i in range(turt_in_row):
            if globals()[f'game_board'][current_row_num][i]==globals()['answer'][current_row_num][i]:
                match_count+=1  
                if match_count == turt_in_row:
                    print("Your whole row is correct!")
                    for i in range(turt_in_row):            #make the turtles in that row dance!
                        turt_dance(globals()[f'block{i}_{current_row_num}'])            
            else:
                print("your row is not correct")
                break

def check_col(current_col_num):  #current_row_num should be a value from 0 to turt_in_row - 1.
    global turt_in_row
    match_count = 0
    
    for j in range(turt_in_row):
        if '-' != globals()['game_board'][j][current_col_num]:
            if globals()[f'game_board'][j][current_col_num]==globals()['answer'][j][current_col_num]:
                match_count+=1  
                if match_count == turt_in_row:
                    print("Your whole column is correct!")
                    for j in range(turt_in_row):            #make the turtles in that row dance!
                        turt_dance(globals()[f'block{current_col_num}_{j}'])            
            else:
                print("your column is not correct")
                break
        else:           #If there are still '-' in the column, we don't want to give the user any info, because they haven't yet finished the column!
            break

#this function will make a given turtle dance, when the row/ column has been correctly solved. NEED: to write the X's as polygons, so they can turn!
def turt_dance(turt):   
    turt.speed(4)
    turt.setheading(90)
    turt.forward(30)
    turt.back(30)



'''Function set #5: debugging functions
used to print the correct gameboard and the current gameboard as 0's and 1's. '''
#prints whatever game_board is input into this function (used to print both the current game_board and the answer_board)
def print_game_board(game_board):
    for row in range(len(game_board)-1,-1,-1):
        print (' '.join(game_board[row]) )
        # print(globals()[f'game_board_{turt_in_row}'][row]) 



###############     Events      #################
screen_setup()

wn.listen()
wn.onkeypress(block_or_x,'x')
wn.onkeypress(clear_screen_and_restart, 'c')

wn.tracer(True)
wn.mainloop()