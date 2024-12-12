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

#creating a blank board to begin
globals()[f'game_board_{turt_in_row}'] = [['-' for column in range(turt_in_row)] for row in range(turt_in_row)] 

#conditional setup based on 5, 10, 15, or 20-board size
width, height = 450, 450
board_shift = 50  #amount by which the board will be shifted left and down to center it
switch_y = -100

#create the screen object, set up screen, add images
wn = t.Screen()
wn.setup(width, height)
wn.tracer(False)



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


'''
The function below, print_game_board(), is for debugging purposes. It prints the all the values of the matrix "game_board," such that row 0 
is the "bottom row," all the way up to the last row being printed on the top of the printed screen. To do this,
I had to reverse the order of the rows of the matrix when they get printed. That is why on line 223, the range 
function has the -1's in it.

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

wn.tracer(True)
wn.mainloop()