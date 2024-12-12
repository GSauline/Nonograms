def random_diffs():
    print('random_diffs called')

def increasing_diffs():
    print('increasing_diffs called')

def select_diffs_per_level():
    print('select_diffs_per_level called')


max_levels = 0
def welcome_and_settings():
    global max_levels
    
    #part of the welcome message was from this website: https://swadge.com/super2023/picross/
    welcome_message = '''
Welcome to Nonograms!!

Nonograms, commonly known as "Picross", is a puzzle game in the family of Sudoku. The objective is to correctly fill in the grid according to 
the clues. Spaces will either be empty or filled, and when all of the squares are correctly set, you will have won, revealing the picture. 

In a typical picross game, you are trying to reveal an image. In this version, however, the "answers" are all randomly generated. Also, 
this version has 4 difficulties: 

Easy (5 x 5 grid) 
Medium (10 x 10 grid) 
Hard (15 x 15 grid) 
Very Hard (20 x 20 grid)

Once the game window pops up, use the numbers along the top and left of the screen to tell you how many spaces to fill. You will click on each 
of the squares to set them as blocks or X's. You will also be able to type 'x' on the keyboard to switch between laying blocks and X's on the 
nonograms board.
But before we begin, we need some information from YOU...
'''
    difficulty_message = '''
\nNow that you've selected the number of levels to play, the next thing to do is select your difficulty mode. 

1. Random difficulties--the game will randomly select the difficulty of each level for you.
2. Increasing difficulties--the game will make the levels get harder as you go. 
(Remember, there are only 4 difficulty levels: Easy, Medium, Hard, or Very Hard)
3. Pick difficulty per level--this puts YOU in the driver seat! You will be prompted to select the difficulty of each level before it begins.

'''
    
    print(welcome_message)
    while True:
        try:
            choice_levels = int(input('To begin, please enter an integer (at least 1) to represent the number of levels you\'d like to play\n'))
        except ValueError:
            print("You did not input a valid integer")
        else:
            if choice_levels <= 0:
                print("Try again, your number must be greater than or equal to 1.")
            else:
                break
    print("You've chosen to play", choice_levels, "levels today.")
    print(difficulty_message)
    while True:
        try:
                choice_diff_mode = int(input('Please enter the number of your selection for difficulty mode.\n'))
        except ValueError:
            print("You did not input a valid integer")
        else:
            if choice_levels not in [1,2,3]:
                print("Try again, you must select 1, 2, or 3.")
            else:
                break
    if choice_diff_mode == 1:
        random_diffs()
    elif choice_diff_mode == 2:
        increasing_diffs()
    elif choice_diff_mode == 3:
        select_diffs_per_level()

welcome_and_settings()