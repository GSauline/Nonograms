import tkinter as tk
import time
import tkinter.messagebox as mb
#Messagebox module and showerror were both found in PLTW 3.1.5, as well as this website: https://docs.python.org/3/library/tkinter.messagebox.html


###### GLOBALS TO ADD TO MAIN CODE
max_levels = 5 #already added
level_list = [] #already added
current_level = 1 #already added
select_diffs_per_level = False #already added

# Variable needed when clicking BEGIN button on Settings frame.
# When we use lst_difficulty.curselection(), it returns a list of indexes that were selected within the listbox.
# So, this is initialized as an empty list because NO SELECTION has been made yet.
difficulty_mode = [] #NOT added

#Variable needed when clicking "Play Level _" button on frame_select_diff
#Same logic for this variable as difficulty_mode above, initialized as empty list.
diff_current_level = [] #NOT added


##############################
# H. tkinter functions. Non-dummy functions can be directly added to existing code.
##############################
'''Notation: 
B1 functions are called by buttons
B2 functions are functions called by B1 buttons
B3 functions are functions called by B2 functions'''

##### 1.  Functions called on Screen 1, the TITLE Screen #####
# B1 Function
# called by the btn_settings, or "SETTINGS" button
# Go to settings screen
def raise_settings():
    root.title("Settings Screen")
    frame_settings.tkraise()

##### 2.  Functions called for the first time on Screen 2, the SETTINGS Screen #####
# B1 function
# called by the btn_begin, or "BEGIN GAME" button
# Checks that selection was made in listbox, calls the functions for difficulty mode, calls play_one_level() to begin actual gameplay
def begin_game():
    global difficulty_mode
    difficulty_mode = lst_difficulty.curselection() 
    if len(difficulty_mode) == 0:         #Can add other Booleans to this condition to allow for other optional selections on this screen.
        mb.showerror("Validation Error!", "Please enter a response for each question.")
    else:
        btn_begin.state = tk.DISABLED  # to avoid cliking this button twice, which may crash the program. Got this idea from 3.1.5
        time.sleep(1)
        root.withdraw() #this withdraw is for the settings screen to be hidden
        print('difficulty mode is', difficulty_mode)
        if 0 in difficulty_mode:
            random_diffs()
        elif 1 in difficulty_mode:
            increasing_diffs()
        elif 2 in difficulty_mode:
            diffs_per_level()
        else: 
            print ("none of the difficulty mode functions called.")
        play_one_level()

# B2 function
# Called within begin_game() function
#DUMMY function
def random_diffs():
    print('random_diffs called')

# B2 function
# Called within begin_game() function
#DUMMY function
def increasing_diffs():
    print('increasing_diffs called')

# B2 function
#Called within begin_game() function
#almost DUMMY function, but does have functionality to conditionally raise the frame_select_diff.
def diffs_per_level():
    global select_diffs_per_level
    select_diffs_per_level = True
    print('diffs_per_level called')

# B2 function
# Called the first time at the end of begin_game()
# Also called on game_over screen, when user clickx a button to replay a new version of the "current level"
# Also called on win_level screen, when user clicks button to play next level.
#partial DUMMY FUNCTION currently. Doesn't have actual gameplay functionality yet, only screen fucntionality
def play_one_level():
    global current_level, level_list
    print('dummy playing level function')
    select_diff_screen()
    print('within play_one_level(), level_list is currently', level_list)
    print(f"playing level {current_level}...")
    
    #assume win
    print('assuming win, we will increment current_level for testing')
    current_level += 1

    # ####### What's between is just for testing. The real play_one_level goes straight into playing now. #########
    # current_level = int(input("change the current_level to..."))
    # time.sleep(1)

    # print('assume win, raise win screen, WHICH DOES NOT EXIST YET')
    # #raise win screen--DOES NOT EXIST YET
    # root.deiconify()
    # ####### What's between is just for testing. The real play_one_level goes straight into playing now. #########


    #rest of play_one_level functionality--copied from main code
    '''global current_level, level_list, screen_setup_needed
    print('in play_one_level, current level is', current_level)

    if current_level==1 and screen_setup_needed:
        screen_setup(current_level, level_list[current_level-1])
        screen_setup_needed = False
    else:
        clear_screen_and_restart(current_level, level_list[current_level-1])

    wn.onkeypress(block_or_x,'x')
    turn_on_clicks(level_list[current_level-1])''' 

#B3 function
#Called as the first line within play_one_level(). 
#This is because, if the user has opted to select their own difficulties, this needs to happen before each level's gamaplay begins.
def select_diff_screen():
    if not(select_diffs_per_level):
        print('pass thru select_diff_screen')
        pass
    else:
        root.title("Select Difficulty Screen")
        lbl_diff_select_var.set(f'Select the difficulty for level {current_level}:')
        btn_diff_select_and_play_var.set(f'Play Level {current_level}')
        frame_select_diff.tkraise()
        root.deiconify() #means show the tk window again

##### 3.  Functions called on Screen 2.5, the SELECT DIFFICULTY Screen #####
'''Recall that frame_select_diff is only CONDITIONALLY shown, based on Boolean select_diffs_per_level.
When the Bool is true, frame_select_diff is raised by the select_diff_screen() function.'''

# B1 function
#Called by btn_diff_select_and_play, or "Play Level _"
#This function needs handle difficulty selection and then disable the button, wait, and withdraw the tk.
# Why does it not need to call play_one_level?
    #The reason is because select_diff_screen(), which raised this frame, is called within play_one_level().
    #Therefore, once this screen is withdrawn, the gameplay should resume via the rest of play_one_level()

def diff_select_and_play():
    global diff_current_level, level_list
    diff_current_level = lst_diff_select.curselection() 
    if len(diff_current_level) == 0:         
        mb.showerror("Validation Error!", "Please enter a response for each question.")
    else:
        btn_diff_select_and_play.state = tk.DISABLED  # to avoid cliking this button twice, which will crash the program
        time.sleep(1)
        root.withdraw() #this withdraw is for the settings screen to be hidden
        print('diff_current_level is', diff_current_level)
        print('level_list is', level_list)
        print('current_level is', current_level)
        if 0 in diff_current_level:
            level_list.append(5)
        elif 1 in diff_current_level:
            level_list.append(10)
        elif 2 in diff_current_level:
            level_list.append(15)
        elif 3 in diff_current_level:
            level_list.append(20)
        else:
            print("none of the valid difficulties have been selected")
        print("after diff selection, level_list is", level_list)
        diff_current_level = []
        print("after resetting, diff_current_level is", diff_current_level)


##############################
# main program
##############################

# start the GUI screens
root = tk.Tk()
root.wm_geometry("800x500")
root.title("Title Screen")


##############################
# 1. create frame for title screen
##############################
frame_title = tk.Frame(root, height=500, width=800)
frame_title.grid_propagate(0)
frame_title.grid(row=0, column=0)

# Create the title Label
lbl_title = tk.Label(frame_title, 
                      text='Nonograms Game!', 
                      anchor = tk.CENTER,
                      bg = "lightblue",
                      width = 50,
                      bd = 3,
                      font = ("Arial", 25, "bold"),
                      justify = tk.CENTER,
                      relief = tk.RAISED)
lbl_title.grid(row=0, column=0, padx=20, pady=20)

'''Optional--cool title written with .stamp() method of turtle? '''

#Create Button to lead to settings screen
btn_settings = tk.Button(frame_title, text='SETTINGS', command=raise_settings, padx=10, pady=10, bd=3)
btn_settings.grid(row=5, column=0)

##############################
# 2. create frame for settings screen
##############################
frame_settings = tk.Frame(root, height=500, width=800)
frame_settings.grid_propagate(0)
frame_settings.grid(row=0, column=0)

# Directions Label
lbl_settings_directions = tk.Label(frame_settings, text='Welcome to Nonograms Settings. Please select your settings. \
Then, click "BEGIN GAME."',
                                   font = ("Arial", 20, "bold"),
                                   wraplength = 500)
lbl_settings_directions.grid(row=0, column=0, padx=10, pady=20, columnspan = 2)


# difficulty label
lbl_difficulty_mode = tk.Label(frame_settings, text='Select the difficulty settings for the levels:')
lbl_difficulty_mode.grid(row=1, column=0, padx=20)

# list box for difficutly selection
lst_difficulty_choices = ["1. Random difficulty for each level", "2. Progressively harder", "3. Pick difficulty before each level"]
lst_difficulty_choices_var = tk.StringVar(value = lst_difficulty_choices)
lst_difficulty = tk.Listbox(frame_settings, width=25, height=3, bd=3, listvariable=lst_difficulty_choices_var)
lst_difficulty.selectmode = tk.BROWSE
lst_difficulty.grid(row=2, column=0)

#Label to explain how the difficulty levels work.
lbl_difficulty_explain = tk.Label(frame_settings, text='Each level, there are 4 possible difficulties: \n \
Easy        (5 x 5 grid)\n \
Medium      (10 x 10 grid)\n \
Hard        (15 x 15 grid)\n \
Very Hard   (20 x 20 grid)')
lbl_difficulty_explain.grid(row=1, column=1, padx=20, rowspan = 2)

'''Optional features that could go here:
1. Select number of lives--need label and entry box
2. Select Lives Mode--need 2 labels(1 is a title, and other explains how the lives modes work) and a listbox
3. Gameplay Mode--need 2 labels and listbox (standard--it corrects you, or classic--it does not correct you/ you can keep clicking/ undo moves)
    For classic mode: 
        A. turn off check_cell(), check_row(), check_col(); keep check_win()
        B. give user ability to keep changing a block's state using .onclick(). (So, would remove if statement that checks for correct color.)
4. Select number of Levels--need label and entry box'''

#Create Button to play game
btn_begin = tk.Button(frame_settings, text='BEGIN GAME', command=begin_game, padx=10, pady=10, bd=3)
btn_begin.grid(row=5, column=0, pady = 20, columnspan = 2)


##############################
# 3. create frame for difficulty select
##############################
frame_select_diff = tk.Frame(root, height=500, width=800)
frame_select_diff.grid_propagate(0)
frame_select_diff.grid(row=0, column=0)

#In order to center the widgets on this screen, I'd like ot configure the columns. 
# Found on https://www.geeksforgeeks.org/horizontally-center-a-widget-using-tkinter/
frame_select_diff.columnconfigure(0, weight=1)
frame_select_diff.columnconfigure(1, weight=1)
frame_select_diff.columnconfigure(2, weight=1)


#Label for the top of this screen, to tell the user to select their difficulty for this level
lbl_diff_select_var = tk.StringVar(value = f'Select the difficulty for level {current_level}:')
lbl_diff_select = tk.Label(frame_select_diff, textvariable = lbl_diff_select_var,
                           font = ("Arial", 20, "bold"))
lbl_diff_select.grid(row=0, column=1, padx=20)

# list box for difficulty setting on one level
lst_diff_select_choices = ["Easy\t\t(5 x 5 puzzle)", "Medium\t\t(10 x 10 puzzle)", "Hard\t\t(15 x 15 puzzle)", "Very Hard\t(20 x 20 puzzle)"]
lst_diff_select_choices_var = tk.StringVar(value = lst_diff_select_choices)
lst_diff_select = tk.Listbox(frame_select_diff, width=22, height=4, bd=3, listvariable=lst_diff_select_choices_var)
lst_diff_select.selectmode = tk.BROWSE
lst_diff_select.grid(row=2, column=1)

#Create Button to play current level
btn_diff_select_and_play_var = tk.StringVar(value = f'Play Level {current_level}')
btn_diff_select_and_play = tk.Button(frame_select_diff, command=diff_select_and_play, padx=10, pady=10, bd=3, textvariable=btn_diff_select_and_play_var)
btn_diff_select_and_play.grid(row=5, column=1, pady = 20)





##############################
# Event Section--These two things need to be the last things in the tk code: 
##############################

#Make the title frame the top frame and keep the tk frame open
frame_title.tkraise()
root.mainloop()




