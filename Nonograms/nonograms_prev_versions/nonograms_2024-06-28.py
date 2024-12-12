import turtle as t
import tkinter as tk
import random
import math

############################################
###    I.  VARIABLE AND TURTLE SETUP     ###
############################################
''' Variable and Turtle Setup - TABLE OF CONTENTS:
A. Variables
-These are variables that need to be defined globally, but not dynamically.

B. Turtle, Screen Object Setup
-These are the turtles/screen objects that need to be defined globally and used throughout the program. 
-Some turtles, such as block_i_j for each cell of the game, need to be created dynamically later in the code and cannot be created here.
    -This is because the blocks are created based on the variable turt_in_row, or how many turtles are in the row. So, we cannot make 
    the blocks in advance (here), because we don't know how many we'll need. 
    -Also, the blocks need to be created and destroyed each level, but the turtles here (drawer, set_block, set_x, and circler) are used
    throughout every level of the program.
'''

######################
# A. Variables
######################

#Variables for turtles on the game_board, writing on game_board screen
turtle_gap = 28      #the gap between turtles on the gameboard
turt_in_row = 5     #the number of block turtles in 1 row/column of the board
num_shift = 5          # amount to shift numbers down to be centered on each row/col
font_setup = ("Verdana", 12, "normal")
block_color_tuple = ((0.8941176470588236, 0.9254901960784314, 0.9294117647058824), (0.8941176470588236, 0.9254901960784314, 0.9294117647058824))
default_delay = 5

t_switch_resize = 1.2    #amount to resize the turtle switches when switching from blocks to X's
t_switch_rotate = 90    #amount to rotate the turtle switches when switching from blocks to X's

#Globals to keep track of winning and level
current_level = 1   #the game starts with level 1.
max_levels = 2
level_list = [5,5]     #This is supposed to be empty and populated with functions. Hard coded for debugging purposes.
#This variable is here so that the first time through the first level, we call screen_setup. 
screen_setup_needed = True   #If we end up replaying level 1 due to a game over, we DO NOT need to call screen_seup again.
  

#all variables for lives
max_lives = 3
current_lives = max_lives       #Max_lives is a constant that does not change. But current_lives will be the "life meter," changing per level
shift_for_hearts = 30   #amount to shift the switch, messages due to the hearts' placement.
heart_horiz_shift = 1.2 #amount to shift subsequent hearts horizontally
heart_img_empty = 'nonograms_images/empty-heart.gif' #found from https://www.shutterstock.com/image-vector/set-pixelated-heart-icons-digital-260nw-2320764891.jpg
heart_img_full = 'nonograms_images/full-heart.gif' #found from https://www.shutterstock.com/image-vector/set-pixelated-heart-icons-digital-260nw-2320764891.jpg
lives_reduction = 1     #global to be called within lose_a_life

#Variables for XCursors and polyRectangle functions 
bar_len = 25
bar_width = 2
X_horiz = bar_len *math.sqrt(2)

#Variables for tkinter screens or difficulty selection
select_diffs_per_level = False

######################
# B. Turtle, Screen Object Setup 
######################

#Create screen object
wn = t.Screen()
t.title('Nonograms Game!')
wn.delay(default_delay)
# wn.screensize(800, 800)

#Add heart images (used for lives functionality)
wn.addshape(heart_img_empty)
wn.addshape(heart_img_full)

'''#Creating the turtles that are never destroyed/ reassigned. Since they all need to be created, penup, and hidden, I did this in a loop.
1. drawer--draws the lines of the gameboard, numbers, and switch border
2. circler--used for circling the correct value on the switch at bottom of screen
3. set_block--turtle that represents the "block" part of the switch
4. set_x--turtle that represents the "x" part of the switch'''
#creating a list to iterate over
turt_names = ['drawer', 'circler', 'set_block', 'set_x']

for name in turt_names:
    globals()[name] = t.Turtle()
    globals()[name].penup()
    globals()[name].hideturtle()

#delete these variables, since they're no longer needed.
del name, turt_names

##############################################
###             II.  FUNCTIONS             ###
##############################################

''' ***FUNCTIONS - TABLE OF CONTENTS***

A. LEVEL SETUP FUNCTIONS
#These functions are called once per level. They format/ draw/ create the board. 

2: screen_setup
    3: switch_setup
    4: draw_lines
    5: create_random_answer
    6: create_custom_5_answer_testing      ##TESTING ONLY
    10: write_numbers
        7: get_row_numbers
        9: get_col_numbers
            8: col_to_row_matrix
        get_row_and_col_sums
    11: turn_on_clicks
    14 - place lives

    
B. RESET FUNCTIONS
#These functions are called to restart the level/ reset something so it can be played again.

15: reset_current_level
    16 reset_switch
    ?: reset_lives(reduction)
1: clear_screen_and_restart
?: test_reset_lives    ##TESTING ONLY


C. SETUP ONLY ONCE PER CODE RUNNING
#These functions are only called once per running of the code, to create the polygon X image to be used for the X's in the game

13: XCursors -- moved out of setup function, called only once before setup() function (but listed in events section)
    12: polyRectangle
    

D. SWITCH FUNCTIONS
#These functions are called multiple times per level. They make the functionality of the switch at the bottom of the screen.
block_or_x()
    circler_fun(x_or_b)


E. CLICKING AND CHECK FUNCTIONS
#These functions are all called whenever a block is clicked. Some of the things they handle: seeing which block we've clicked, 
changing its appearance, checking that the cell is correct with the puzzle, checking that the row/column/ puzzle is correct, 
handling what happens when a cell is incorrect or a row/col is correct, etc.

clicked()
    check_cell(current_row_num,current_col_num)
        lose_a_life()
    new_check_row(current_row_num)
        turt_dance(turt)
    new_check_col(current_col_num)
        turt_dance(turt)
    check_win()
    print_game_board(gameboard)     ##repeat from earlier, DEBUGGING ONLY

""" N.B: Two functions in this section are no longer called, check_row(j) and check_col(i).
These two functions did not "fill in" the x's when the blocks for a row/ col are correct.
If I ever decide to make "classic mode" (where the user has to check their own cells) a thing, 
I will need these functions. """


F. DEBUGGING FUNCTIONS  
#This section is for functions that will not be used in the "final" version of the game, but are used now
while I'm debugging. This currently has 1 function in it, print_board(gameboard), which is used to print 
both the answer board and current game_board, to make sure that the "behind the scenes" changes match 
the on-screen changes.


G. WIN/ LOSE/ GAMEPLAY FUNCTIONS
#these functions are necessary for playing multiple levels, winning, losing functionality

play_one_level() -- this function is now the "top_level" function of the game. it calls screen_setup or clear_screen_and_restart

win_level() --called within check_win (check_win is called within clicked)
    turn_off_turtle_events()
    win_whole_game()

game_over()--called within lose_a_life(), which is also called within clicked

'''
######################
# A. Game Level Setup functions
######################

'''screen_setup is the 'brains' of this operation. It does many things:
    1) formats the screen based on the number of turtles in the row, 
    2) creates the turtles for the board
    3) draws the lines for the board
    4) sets up/places the turtles to act as switches at the bottom of the screen
    5) draws the border (and initial circle) around the switches at the bottom of the screen 
    6) Turns on the onclick() for each turtle on game board by calling turn_on_clicks() '''
def screen_setup(current_lev, t_in_row):
    ####
    # 1. Setup for "behind the scenes" variables and screen
    ###
    global turt_in_row, width, height, switch_y, board_shift, turtle_gap, font_setup, shift_for_hearts

    #Screen_setup will be used to override the default value of turt_in_row. This will be necessary for when we pick a different diffulty per level.
    turt_in_row = t_in_row      

    #conditional setup based on 5, 10, 15, or 20-board size
    if turt_in_row ==5:
        width, height = 450, 450
        board_shift = 50  #amount by which the board will be shifted left and down to center it
        switch_y = -125
    elif turt_in_row==10:
        width, height = 600, 600
        board_shift = 100
        switch_y = -175
    elif turt_in_row == 15:
        width, height = 750,750
        board_shift = 200
        switch_y = -275   
    elif turt_in_row == 20:
        width, height = 950, 950
        board_shift = 270
        switch_y = -350
    else:
        print("That is an invalid entry. Here is a 5-by-5")
        screen_setup(current_level, 5)
    # print('switch_y', switch_y)       Debugging statement
        
    #creating/redefining a blank board to begin
    globals()[f'game_board'] = [['-' for column in range(turt_in_row)] for row in range(turt_in_row)] 
    
    #creating a random answer
    create_random_answer()
  
    '''
    #create a custom 5-by-5 (only for testing)
    create_custom_5_answer_testing()
    '''

    #set up screen, add images
    wn.setup(width, height)
    wn.tracer(False)

    ###
    #2.  Setup for the visual aspects of the screen.
    ###

    '''#dynamically create the turtles for the screen
    block0_0 through 0_4 should be in column 0 (first column-- x val of 0)
    block0_0 through 4_0 should be in row 0 (first row-- y val of 0)'''
    for j in range(turt_in_row):
        for i in range(turt_in_row):
            globals()[f'block{i}_{j}'] = t.Turtle(shape="square")
            globals()[f'block{i}_{j}'].color('#E4ECED')
            globals()[f'block{i}_{j}'].penup()
            globals()[f'block{i}_{j}'].goto(i*turtle_gap-board_shift, j*turtle_gap-board_shift)
            # print(f'block{i}_{j}', 'go to',i*turtle_gap,j*turtle_gap)     Debugging statement

    #In case there is any writing on the screen already made by the turtle drawer, clear it.
    drawer.clear()

    #draw lines for gameboard
    draw_lines()

    #draw the numbers along the top and left of the board, based on answer (function in progress)
    write_numbers()

    #Drawing the switch and setting up the turtles for the "switch" at the bottom of the screen.
    #The switch is used to change the clicks from X's to blocks.
    switch_setup()

    #turn on click functionality for the already-created turtles on the board
    turn_on_clicks(turt_in_row)

    #place hearts on the screen for the lives, equal to the global variable max_lives
    place_lives()

    write_level_num()
    
    wn.tracer(True)

#Formats the "switch" at the bottom of the screen and its turtles
def switch_setup():
    global switch_y, drawer, set_block, circler, set_x, font_setup
    #Drawing the border around the "switch" to Switch from Solid blocks to X's
    drawer.goto(-25,switch_y - 15-shift_for_hearts)
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
    
    set_block.goto(-15, switch_y-shift_for_hearts)
    set_block.showturtle()
    set_block.shape("square")
    set_block.shapesize(1.2)
    set_block.right(360)
    #circling the Block switch, because block_state is true to start program
    circler.goto(-15,switch_y-18-shift_for_hearts)
    circler.pendown()
    circler.circle(18)
    circler.penup()

        #X switch
    set_x.goto(15,switch_y-shift_for_hearts)
    set_x.showturtle() 
    set_x.shape("turtle")               #changing to arbitrary shape and back to X will move the X to the "top" above oval
    set_x.shape("X_turtle")

        #A message to indicate how to change from X to block
    drawer.penup()
    drawer.goto(0,switch_y-40-shift_for_hearts)
    drawer.write("Use the 'x' key to change your click from blocks to X's.", align = 'center', font=font_setup)

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
    globals()['answer_row_2'] = ['0', '1', '1', '1', '1']
    globals()['answer_row_3'] = ['0', '0', '0', '0', '0']
    globals()['answer_row_4'] = ['0', '0', '1', '0', '1']

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

#Using answer, returns the numbers that will be displayed on the left of the screen
#Called within write_numbers
def get_row_numbers(board):
    global turt_in_row
    
    row_nums = []
    #creating one number list per row of answer. This will start at row 0, the bottom of the image.
    for j in range(len(board)):
        globals()[f'row_nums_list_{j}'] = []
    
    for j in range(len(board)):        #loop over every row
        temp_sum = 0
        # print('new row')      Debugging statement
        for i in range(len(board)):        #loop over every index in the row
            # print("current cell value is", globals()['answer'][j][i])     Debugging statement

            if board[j][i]=='1' and i != (turt_in_row - 1):     #when there is a 1 not at the end of row/ col
                temp_sum += 1
                # print('there is a 1 here. temp_sum =', temp_sum)  debug
            elif board[j][i]=='1' and i == (turt_in_row -1):    #when there is a 1 at the end of row/ col
                temp_sum += 1
                # print('there is a 1 at the end of the row') debug
                globals()[f'row_nums_list_{j}'].append(str(temp_sum))
                temp_sum = 0
            elif board[j][i] == '0' and temp_sum != 0:         #when there is a 0 throughout a row/col
                globals()[f'row_nums_list_{j}'].append(str(temp_sum))
                temp_sum = 0
            elif i == (turt_in_row-1) and temp_sum == 0 and globals()[f'row_nums_list_{j}']==[]:    #when there is a 0 at the end of row/ col of all 0's
                globals()[f'row_nums_list_{j}'].append(str(temp_sum))
        
        # print('nums for row', j, globals()[f'row_nums_list_{j}'])     Debugging statement
        row_nums.append(globals()[f'row_nums_list_{j}'])
        del globals()[f'row_nums_list_{j}']
    return row_nums

#returns a matrix where the row and columns are switched.
#Called within get_col_numbers
def col_to_row_matrix(board):
    col_to_row_list = []
    #create one list for each column of the original board
    for col_num in range(len(board)):
        globals()[f'col_to_row_{col_num}'] = []
    
    #iterate through the rows and append each value to the correct column list
    for j in range(len(board)):        #j is row number of original board (y value)
        for i in range(len(board[j])): #i is col number of original board (x value)
            globals()[f'col_to_row_{i}'].append(board[j][i]) #append this value to correct col list
    
    #printing each column, appending to col_to_row_list
    for col_num in range(len(board)):
        # print("column",col_num,"becomes the list",globals()[f'col_to_row_{col_num}'])     Debugging statement
        col_to_row_list.append(globals()[f'col_to_row_{col_num}'])
        del globals()[f'col_to_row_{col_num}']
    # print_game_board(col_to_row_list)     Debugging statement
    return col_to_row_list

#Using answer, returns the column numbers that will be displayed on the top of the screen
#Called within write_numbers
def get_col_numbers():

    #First, switch the x and y of the matrix.    
    transposed_answer_matrix = col_to_row_matrix(globals()['answer'])

    #Then, use get_row_numbers to get the row numbers of the transposed matrix. 
    #Thus, getting the column numbers of the actual matrix.

    col_nums = get_row_numbers(transposed_answer_matrix)
    return col_nums

#Writes the numbers (from get_col_numbers and get_row_numbers) that go on the left and top of the screen.
def write_numbers(): 
    row_nums = get_row_numbers(globals()['answer'])
    col_nums = get_col_numbers()

    '''The following function is not needed for writing the numbers, but this was a good place to call it.
    It is used to create two globals lists, row_sums and col_sums, that are necessary for new_check_row 
    new_check_col. I decided to call this function here because it is only needed once per level, even
    though new_check_row and new_check_col will be called multiple times per level.    
    '''
    get_row_and_col_sums(row_nums, col_nums)

    #actually drawing the row numbers on the left
    for j in range(len(row_nums)):
        drawer.goto(-.75*turtle_gap-board_shift, j*turtle_gap-board_shift-num_shift)
        drawer.write(" ".join(row_nums[j]), align = 'right', font = font_setup)
        
        #top column numbers
    for i in range(len(col_nums)):
        #When I didn't reverse each list in col_nums, it printed the numbers for a given column upside-down
        reversed_nums = [col_nums[i][val] for val in range(len(col_nums[i])-1,-1,-1)]
        drawer.goto(i*turtle_gap-board_shift-num_shift, turt_in_row*turtle_gap-num_shift-board_shift)
        drawer.write('\n'.join(reversed_nums), align = 'left', font = font_setup)

#Used to get the numerical sums of the number of blocks in each row. Does this by changing row_nums and col_nums, 
#which are lists of lists of stringed integers, into a list of integers.
def get_row_and_col_sums(row_n, col_n):
    #For this algorithm, I got input from https://www.geeksforgeeks.org/python-get-summation-of-numbers-in-string-list/
    #I sought help because I needed help with changing a list of lists of stringed integers into a list of integer sums
    global row_sums, col_sums

    print('calling get_row_and_col_sums')

    #getting the sum of the 1's for each row of row_nums
    row_sums = [sum(int(ele) for ele in sub) for sub in row_n] #borrowed from the above website

    col_sums = [sum(int(ele) for ele in sub) for sub in col_n] #borrowed from the above website
    #all below were for debugging
    # print('row_n, or original list of lists of strings, is', row_n)       
    # print('row_sums, or the list of sums of row values, is', row_sums)

    # print('\n\n col_n, or original list of lists of strings, is', col_n)
    # print('col_sums, or the list of sums of column values, is', col_sums)

#Handle the on_click events for each block turtle
def turn_on_clicks(num_in_row):
    for j in range(num_in_row):
        for i in range(num_in_row):
            globals()[f'block{i}_{j}'].onclick(clicked)

#This function places the lives images on the screen. Based on the global current_lives, it places that many full hearts on the screen.
def place_lives():
    '''this function is used to initially create the lives turtles (based on global variable max_lives). It places them at the bottom 
    of the screen. It gives them the "full heart" image. '''
    global current_lives
    current_lives = max_lives  #for the new level, reset the global current_lives to be equal to max_lives
    for i in range(max_lives):
        globals()[f'heart_{i}'] = t.Turtle()
        globals()[f'heart_{i}'].shape(heart_img_full)
        globals()[f'heart_{i}'].penup()
        globals()[f'heart_{i}'].goto(-35+i*heart_horiz_shift*turtle_gap, switch_y+10)     

#This function places the current level number on the screen.
def write_level_num():
    global current_level
    drawer.goto(-35, switch_y+30)
    drawer.write(f"Level {current_level}", align = 'left', font=("Arial", 18, 'normal', 'bold', 'underline'))


######################
# B. Reset functions
######################

#This function is used to leave the gameboard as is, but allow for the user to replay the curernt level. This is to be one of the options after game over.
def reset_current_level():
    '''used to reset current level after a game_over. Should be called within the game_over function, eventually. Currently called with "q." '''
    print('reset current_level called')
    wn.tracer(False)
    #reset the colors of the blocks to be a square in the neutral color again.
    for j in range(turt_in_row):
        for i in range(turt_in_row):
            globals()[f'block{i}_{j}'].clear()
            globals()[f'block{i}_{j}'].shape("square")
            globals()[f'block{i}_{j}'].color('#E4ECED')
    
    #recreating a blank board
    globals()[f'game_board'] = [['-' for column in range(turt_in_row)] for row in range(turt_in_row)]

    #should reset the switch to "square"
    reset_switch()
    #rest the lives, decreased by 1 life.
    reset_lives(lives_reduction)
    wn.tracer(True)
   
    #These 4 statements were debugging
    # print('\n\n answer is...')
    # print_game_board(answer)

    # print('\n\n game board is...')
    # print_game_board(game_board)

    turn_on_clicks(turt_in_row)   #turn on clicks of the gameboard turtles, to fix bug where some turtles couldn't be clicked after this function.  

#This function is to be used to reset the screen and variables. It then restarts the game. Goal: use it to reset after a level change, or game over.
def clear_screen_and_restart(cur_lev, t_in_r):
    # choice = input("Are you sure you want to clear the screen and start again? Type 'y' or 'yes'. Type anything else for no.")
    global turt_in_row, game_board, drawer, circler, set_x, set_block, wn, answer
    #delete the turtles in the gameboard
    # if choice == 'yes' or choice == 'y':
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

    #make the hearts disappear
    for i in range(max_lives):
        globals()[f'heart_{i}'].hideturtle()

    #reassign the gameboard and answer to be blank
    game_board = []
    answer = []
    print('globals after deletion', globals())      #debugging

    wn.tracer(True)

    #restart the game
    screen_setup(cur_lev, t_in_r)
    block_or_x()
    reset_switch()

#This function is to be called within reset_current_level. Note, it does NOT move the switches to a new location
#It resets the switch to being set to "block".
def reset_switch():
    global switch_y, set_block, circler, set_x, block_state

    #Resetting global block_state to True, because we want to reset the "click block" functionality
    block_state =  True


    #Recircling, resizing block switch (it needs to be large again)
    set_block.shape("square")
    set_block.shapesize(1.2)
    set_block.showturtle()
    #circling the Block switch, because block_state is true again
    circler.clear()     #clear any old writings of circler
    circler.goto(-15,switch_y-18-shift_for_hearts)
    circler.pendown()
    circler.circle(18)
    circler.penup()

    #resizing X switch back to regular size
    set_x.shape("X_turtle")
    set_x.shapesize(1)
    set_x.showturtle()

#This function is used to reset the number of lives, based on a reduction. This is to be used to reset the lives after a game over. 
#If reduction = 0, then the same number of lives are replaced.
def reset_lives(reduction):
    """this function is used to reset the lives when the level is reset. It does NOT create turtles, but it loops over the existing turtles
    and resets current_lives.
    reduction is an integer <= max lives. Otherwise, the function passes.
    This function is to be used for resetting after a game over (functionality not fully created yet.)"""
    print('reset lives has been called')
    global current_lives
    
    if reduction >= max_lives:
        print('life reduction must be less than maximum life number of:', max_lives)
        pass
    else:
        print('reduction is less than max_lives')
        current_lives = max_lives - reduction
        print('current_lives will now be', current_lives)
        for i in range(current_lives):
            globals()[f'heart_{i}'].shape(heart_img_full)
        for i in range(current_lives, max_lives):
            globals()[f'heart_{i}'].shape(heart_img_empty)

#TESTING ONLY This function was created only because I wanted button click functionality with reset_lives, which can't do when there's a parameter.
def test_reset_lives():
    #funciton only here so I can test reset_lives with the keyboard, r.
    reset_lives(2)


######################
# C. Setup only once per coding
######################

#Function for drawing the bar of the X's
#Adapted from a post at https://stackoverflow.com/questions/35834691/change-appearance-of-turtle/35837569#35837569
#Called within XCursors
def polyRectangle(turt, x, y, slant, length1, length2):
    turt.goto(x, y)
    turt.setheading(slant)

    turt.begin_poly()

    for count in range(2):
        turt.forward(length1)
        turt.left(90)
        turt.forward(length2)
        turt.left(90)

    turt.end_poly()

    return turt.get_poly()

#Function to create the red and black X turtle shapes, for use on the gameboard and on the bottom of the screen
#Adapted from a post at https://stackoverflow.com/questions/35834691/change-appearance-of-turtle/35837569#35837569
#Called presently at the top level, before screen_setup()
def XCursors():
    temporary = t.Turtle()
    screen = t.getscreen()

    delay = screen.delay()
    screen.delay(0)

    temporary.hideturtle()
    temporary.penup()


    X_turtle = t.Shape("compound")
    X_turtle_red = t.Shape("compound")

    left_side = polyRectangle(temporary, 0.35*bar_len, -0.375*bar_len, 45, bar_width, bar_len)  # left_side of X
    X_turtle.addcomponent(left_side, "black", "black")
    X_turtle_red.addcomponent(left_side, "red", "red")

    right_side = polyRectangle(temporary, 0.35*bar_len, 0.325*bar_len, 135, bar_width, bar_len)  #right side of X
    X_turtle.addcomponent(right_side, "black", "black")
    X_turtle_red.addcomponent(right_side, "red", "red")
    
    t.register_shape("X_turtle", X_turtle)
    t.register_shape("X_turtle_red", X_turtle_red)
    
    screen.delay(default_delay)
    del temporary

    for turt in t.turtles():
        turt.hideturtle()


######################
# D. Switch functions
######################

#Based on the parameter x_or_b, this function either circles the Block Button or the X button at the bottom of the screen
#Called within block_or_x()
def circler_fun(x_or_b):
    if x_or_b == "block":
        wn.tracer(False)
        circler.clear()
        circler.penup()
        circler.goto(-15,switch_y-18-shift_for_hearts)
        circler.pendown()
        circler.circle(18)
        circler.penup()
        wn.tracer(True)
    if x_or_b == "x":
        wn.tracer(False)
        circler.clear()
        circler.penup()
        circler.goto(15,switch_y-18-shift_for_hearts)
        circler.pendown()
        circler.circle(18)
        circler.penup()
        wn.tracer(True)

#this function controls the value of the Boolean block_state and changes the look of the turtles set_x and set_block at the bottom of the screen.
#called multiple times per level, via onkeypress ('x')
def block_or_x():
    print('block_or_x has been called.')
    global block_state
    if block_state==True:
        block_state=False
        set_block.shapesize(1)
        set_x.shapesize(t_switch_resize)
        # set_x.right(t_switch_rotate)
        circler_fun("x")
    
    else:
        block_state=True
        set_block.shapesize(t_switch_resize)
        set_x.shapesize(1)
        # set_block.right(t_switch_rotate)
        circler_fun("block")        


######################
# E. Clicking and Check Functions
######################

'''clicking function
The brain of the game! This function controls everything that happens each time we click on one of the turtles on the board

This function does several things:
        1) loops over all blank blocks on the board, only checking ones that have not yet been clicked (using original color tuple) 
        2) Finds which block the click is closest to by finding the distance from x and y to all blank block coordinates
        3) once we've found the correct block, check if block_state is true. If so, turn the block blue! If not, turn the block to x
        4) If blank block --> full block, set  game_board at that cell = 1; if blank block --> x, set game_board at that cell = 0
        5) print the game_board
'''
def clicked(x,y):
    global block_state, turt_in_row, block_color_tuple, answer
    for j in range(turt_in_row):        #go through all rows
        for i in range(turt_in_row):    #go through all turtles within a row
            if globals()[f'block{i}_{j}'].color()==block_color_tuple:                       #only want to alter unclicked (whitish-blue blocks)
                if abs(x-globals()[f'block{i}_{j}'].xcor()) < 15 and abs(y-globals()[f'block{i}_{j}'].ycor()) < 15:     #finding the block we've clicked near 
                    # print(f'block{i}_{j} clicked!')     #debugging statement
                    if block_state==True:                      
                        globals()[f'block{i}_{j}'].color('blue')
                        globals()[f'game_board'][j][i]='1'              #change the gameboard at that spot to a 1, for filled

                    else:
                        globals()[f'block{i}_{j}'].shape("X_turtle")
                        globals()[f'game_board'][j][i]='0'              #change the gameboard at that spot to a 0, for x
                    
                    #The following should happen whether block_state is true or not. 
                    #It needs to happen every time we have clicked on a cell and changed it to an X or block.
                    check_cell(j,i)                                 #this should check that the cell has been entered correctly
                    new_check_row(j)                                    #this should check that the whole row has been entered correctly
                    new_check_col(i)                                    #this should check that the whole column has been entered correctly
                    check_win()
                    

                    # print('\n\nPrinting answer...')           Debugging statement
                    # print_game_board(globals()[f'answer'])    Debugging statement
                    # print('Printing game_board...')             #Debugging
                    # print_game_board(globals()[f'game_board'])  #Debugging

def check_cell(current_row_num, current_col_num):
    if globals()['game_board'][current_row_num][current_col_num]== globals()['answer'][current_row_num][current_col_num]:
        # print("Congrats! This was the correct thing to put in this cell!")
        pass
    else:
        # print("Boo! Wrong thing in this cell!")

        if globals()['answer'][current_row_num][current_col_num] == '0':
            wn.delay(200)
            globals()[f'game_board'][current_row_num][current_col_num]='0'
            globals()[f'block{current_col_num}_{current_row_num}'].shapesize(1.5)
            globals()[f'block{current_col_num}_{current_row_num}'].shape("X_turtle_red")
        else:
            wn.delay(200)
            globals()[f'game_board'][current_row_num][current_col_num]='1'
            globals()[f'block{current_col_num}_{current_row_num}'].shapesize(1.5)
            globals()[f'block{current_col_num}_{current_row_num}'].color("red")
            globals()[f'block{current_col_num}_{current_row_num}'].shape("square")

        wn.delay(200)
        globals()[f'block{current_col_num}_{current_row_num}'].shapesize(1)
        wn.delay(default_delay)
        lose_a_life()

def check_row(current_row_num):  #current_row_num should be a value from 0 to turt_in_row - 1.
    global turt_in_row
    match_count = 0
    if '-' not in globals()['game_board'][current_row_num]:
        for i in range(turt_in_row):
            if globals()[f'game_board'][current_row_num][i]==globals()['answer'][current_row_num][i]:
                match_count+=1  
                if match_count == turt_in_row:
                    # print("Your whole row is correct!")
                    for i in range(turt_in_row):            #make the turtles in that row dance, if you're not dead.
                        if current_lives != 0:
                            turt_dance(globals()[f'block{i}_{current_row_num}'])            
            else:
                # print("your row is not correct")
                break

def new_check_row(current_row_num):   
    global turt_in_row

    '''This variable will be used to determine how many 1's (blocks) are currently filled in on the gameboard.
    If this variable matches the row_sum, then the row is correct.'''
    count_1s_in_gameboard = 0   

    # print('\n\ncalling new_check_row on row', current_row_num) #debugging
    # print(f'row_sums[{current_row_num}] = ', row_sums[current_row_num]) #debugging

    #This loop is getting the value of count_1s_in_gameboard. Do count when the 1's match. 
    #Don't count when there is a 1 in answer, but a - in gameboard.
    for i in range(turt_in_row):
        if globals()[f'game_board'][current_row_num][i] == '1' and globals()['answer'][current_row_num][i] == '1':
            count_1s_in_gameboard += 1
            # print(f'game_board has a 1 at index{i}, and answer has a 1. increment.')
            # print('count_1s_in_gameboard', count_1s_in_gameboard)
        
        #if our gameboard is a - and our answer board is a 1, do nothing. not yet answered.
        elif globals()[f'game_board'][current_row_num][i] == '-' and globals()['answer'][current_row_num][i] == '1':
            # print(f'game_board has a - at index{i}, and answer has a 1. break.')
            break

    '''if we don't yet have all the 1's in our game_board matching the 1's in answer board, do nothing. 
    If they do match (and you're not dead)
    a) change every - in gameboard to 0
    b) change every blank turtle to the x turtle
    c) make the turtles dance '''
    if count_1s_in_gameboard != row_sums[current_row_num]:
        # print('do not yet have the same count for our row num and our 1s for this row. pass')
        pass
    else:
        # print(f'row {current_row_num} is correct!')
        
        #only fix the rest of the row and make the turtles dance if you're not dead.
        if current_lives != 0:      
            for i in range(turt_in_row):           
                turt_dance(globals()[f'block{i}_{current_row_num}'])
                if globals()[f'game_board'][current_row_num][i] == '-': #change the blanks to x's
                    globals()[f'block{i}_{current_row_num}'].shape("X_turtle")
                    globals()[f'game_board'][current_row_num][i]='0'              #change the gameboard at that spot to a 0, for x            

def check_col(current_col_num):  #current_row_num should be a value from 0 to turt_in_row - 1.
    global turt_in_row
    match_count = 0
    
    for j in range(turt_in_row):
        if '-' != globals()['game_board'][j][current_col_num]:
            if globals()[f'game_board'][j][current_col_num]==globals()['answer'][j][current_col_num]:
                match_count+=1  
                if match_count == turt_in_row:
                    # print("Your whole column is correct!")    #Debugging
                    for j in range(turt_in_row):            #make the turtles in that row dance, if you're not dead.
                        if current_lives != 0:
                            turt_dance(globals()[f'block{current_col_num}_{j}'])            
            else:
                # print("your column is not correct")       #debugging
                break
        else:           #If there are still '-' in the column, we don't want to give the user any info, because they haven't yet finished the column!
            break

def new_check_col(current_col_num): #I needed a new function, now that the cells are checked for correctness
    global turt_in_row

    '''This variable will be used to determine how many 1's (blocks) are currently filled in on the gameboard.
    If this variable matches the col_sum, then the col is correct.'''
    count_1s_in_gameboard = 0   

    # print('\n\ncalling new_check_col on col', current_col_num) #debugging
    # print(f'col_sums[{current_col_num}] = ', col_sums[current_col_num]) #debugging

    #This loop is getting the value of count_1s_in_gameboard. Do count when the 1's match. 
    #Don't count when there is a 1 in answer, but a - in gameboard.
    for j in range(turt_in_row):
        if globals()[f'game_board'][j][current_col_num] == '1' and globals()['answer'][j][current_col_num] == '1':
            count_1s_in_gameboard += 1
            # print(f'game_board has a 1 at index{j}, and answer has a 1. increment.')  debugging
            # print('count_1s_in_gameboard', count_1s_in_gameboard)                     debugging
        
        #if our gameboard is a - and our answer board is a 1, do nothing. not yet answered.
        elif globals()[f'game_board'][j][current_col_num] == '-' and globals()['answer'][j][current_col_num] == '1':
            #print(f'game_board has a - at index{j}, and answer has a 1. break.')
            break

    '''if we don't yet have all the 1's in our game_board matching the 1's in answer board, do nothing. 
    If they do match (and you're not dead)
    a) change every - in gameboard to 0
    b) change every blank turtle to the x turtle
    c) make the turtles dance '''
    if count_1s_in_gameboard != col_sums[current_col_num]:
        # print('do not yet have the same count for our col num and our 1s for this col. pass')
        pass
    else:
        # print(f'col {current_col_num} is correct!')
        
        #only fix the rest of the row and make the turtles dance if you're not dead.
        if current_lives != 0:      
            for j in range(turt_in_row):           
                turt_dance(globals()[f'block{current_col_num}_{j}'])
                if globals()[f'game_board'][j][current_col_num] == '-': #change the blanks to x's
                    globals()[f'block{current_col_num}_{j}'].shape("X_turtle")
                    globals()[f'game_board'][j][current_col_num]='0'              #change the gameboard at that spot to a 0, for x            

def check_win():
    global win, current_level
    if game_board == answer:
        win_level()

#this function will make a given turtle dance, when the row/ column has been correctly solved. NEED: to write the X's as polygons, so they can turn!
def turt_dance(turt):   
    turt.speed(6)
    turt.setheading(90)
    turt.forward(30)
    turt.back(30)

def lose_a_life():
    global current_lives
    
    globals()[f'heart_{current_lives - 1}'].shape(heart_img_empty) #if we have 3 lives, heart_2 must be changed
    current_lives -= 1
    print('current lives after losing one', current_lives)

    if current_lives == 0:
        print('you lost all lives, game over')
        game_over()
    

######################
# F. Debugging Functions
######################

#prints whatever game_board is input into this function (used to print both the current game_board and the answer_board)
#Function created so that the output would not be a list of lists. Also, so the top of the output matched the top of the board.
def print_game_board(game_board):
    for row in range(len(game_board)-1,-1,-1):
        print (' '.join(game_board[row]) )
        # print(globals()[f'game_board_{turt_in_row}'][row])    Debugging statement

######################
# G. WIN/ LOSE/ GAMEPLAY FUNCTIONS
######################

# Should turn off wn.onkeypress and turtle.onclick() functionality. (Note, it will not disable wn.listen() 
# it will merely reassign the click and key ‘x’ to the function None).
# See https://stackoverflow.com/questions/36924609/python-turtle-stop-listening and 
# https://docs.python.org/3/library/turtle.html#turtle.onclick under “events”
def turn_off_turtle_events():
    print('turning off "x" and turtles...')
    global turt_in_row
    wn.onkeypress(None, 'x')
    for j in range(turt_in_row):
        for i in range(turt_in_row):
            globals()[f'block{i}_{j}'].onclick(None)
            # print(f"turtle called block{i}_{j} should not be clickable")

###### win_level, win_whole_game, game_over, play_one_level - In progresss......#######

#Some of the functionality, like incrementing current_level, should be handled by tkinter screen, eventually
def win_level():
    global current_level, max_levels
    turn_off_turtle_events()
    print('YOU WON!')
    if current_level != max_levels:
        #still need to create this screen
        print('trigger win level screen')
        current_level += 1 #but the incrementing needs to happen later (via the button on win_screen)
        choice = input('do you want to play the next level? "y" or "n"')
        if choice == "y":
            play_one_level() #should happen via a button, eventually
    else:
        #Still need to finish this function
        print('call win_whole_game()')
        win_whole_game()

def win_whole_game():
    global max_levels
    print('win_whole_game() should trigger an ending screen')
    #trigger end screen
    print(f'you beat all {max_levels} levels! Yay for you!')

def game_over():
    turn_off_turtle_events()
    print('game over.')
    print(f"You have two options:\n\n1. Replay the exact level you just played, but with {lives_reduction} less lives. \
\n2. Play a brand new level #{current_level}, with all your lives back.")
    choice = int(input(f'Type 1 for the first option, 2 for the second option.   '))
    if choice==1:
        reset_current_level()
    elif choice==2:
        play_one_level()

def play_one_level():
    global current_level, level_list, screen_setup_needed
    print('in play_one_level, current level is', current_level)

    if current_level==1 and screen_setup_needed:
        screen_setup(current_level, level_list[current_level-1])
        screen_setup_needed = False
    else:
        clear_screen_and_restart(current_level, level_list[current_level-1])

    wn.onkeypress(block_or_x,'x')
    turn_on_clicks(level_list[current_level-1])
    #It will start with calling select_dif_screen() -- nonexistant function yet

###### win_level, win_whole_game, game_over, play_one_level - In progresss......#######

    

################################################
###          III. Events--Main code          ###
################################################
XCursors()

play_one_level()
wn.listen()
# wn.onkeypress(clear_screen_and_restart, 'c')

# wn.onkeypress(test_reset_lives, 'r')        #debugging
# wn.onkeypress(test_get_row_and_col_sums, 't')

# wn.onkeypress(reset_current_level, 'q')     #debugging

wn.onkeypress(turn_off_turtle_events, 'z') #debugging

wn.mainloop()
