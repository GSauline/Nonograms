#nonograms_functions_needed_for_classic_mode.py

'''
A lot of functions from the main file will be reused as they are for classic mode. Below are the functions 
where we would need DIFFERENT VERSIONS of them for classic mode.

The following functions are the ORIGINAL versions of new_check_row and new_check_col.
These functions did NOT fill in X's when the "blocks" were finished in a given row/ column.
Instead, they required the user to put in an entire row/ column before checking the row/column.

Why this is needed for classic mode: 
In classic mode, the user will be able to make a selection of block or X, just like standard mode.
However, they can also CHANGE their selection for a cell as many times as they want.
They will NOT be "locked in" to one choice or another. So, there will be no check_cell() function. 
Basically, the user has to check their own cells.

But we DO want to let the user know (as they go) if they're on the right track. 
Hence, we need these versions of check_row and check_col, so that we can let the user know when 
their row or column is correct.
'''

def check_row(current_row_num):  #current_row_num should be a value from 0 to turt_in_row - 1.
    global turt_in_row
    match_count = 0
    if '-' not in globals()['game_board'][current_row_num]:
        for i in range(turt_in_row):
            if globals()[f'game_board'][current_row_num][i]==globals()['answer'][current_row_num][i]:
                match_count+=1  
                if match_count == turt_in_row:
                    for i in range(turt_in_row):            #make the turtles in that row dance, if you're not dead.
                        if current_lives != 0:
                            turt_dance(globals()[f'block{i}_{current_row_num}'])            
            else:
                break

def check_col(current_col_num):  #current_row_num should be a value from 0 to turt_in_row - 1.
    global turt_in_row
    match_count = 0
    
    for j in range(turt_in_row):
        if '-' != globals()['game_board'][j][current_col_num]:
            if globals()[f'game_board'][j][current_col_num]==globals()['answer'][j][current_col_num]:
                match_count+=1  
                if match_count == turt_in_row:
                    for j in range(turt_in_row):            #make the turtles in that row dance, if you're not dead.
                        if current_lives != 0:
                            turt_dance(globals()[f'block{current_col_num}_{j}'])            
            else:
                break
        else:           #If there are still '-' in the column, we don't want to give the user any info, because they haven't yet finished the column!
            break
