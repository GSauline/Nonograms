#NONOGRAMS - TESTING INCREASING DIFFS

import random

level_list = []
max_levels = 6
def increasing_diffs(m_levels):
    global level_list
    print('increasing_diffs called')

    if m_levels == 3:                   #When testing, m_levels = 3 made the list [10,15,20]. I wanted there to always be at least 1 easy level.
        level_list = [5,10,15]
    elif m_levels == 6:
        level_list = [5,10,10,15,15,20] #When testing, m_levels = 6 made the list [10,10,15,15,20,20]. I wanted there to always be at least 1 easy level.
    else:
        num_levels_per_diff = round(m_levels/ 4) #we want to basically divide the number of total levels by 4, to approximately get an equal number of levels for each diff
        print("number of levels per difficulty is", num_levels_per_diff)
        
        num_easy_levels = m_levels - 3*num_levels_per_diff  #we want all the "rest" of the levels to be easy levels. (if we select 1 or 2 levels, they will be easy.)
        for i in range(num_easy_levels):
            level_list.append(5)

        
        for j in [10,15,20]:
            for i in range(num_levels_per_diff):
                level_list.append(j)
    
    print(f'with max_levels of {m_levels}, level_list is {level_list}\n\n')

def random_diffs(m_levels):
    global level_list
    level_list = [random.choice([5,10,15,20]) for level in range(m_levels)]
    print(f'after random_diffs, with max_levels of {m_levels}, level_list is {level_list}')

for i in range(1,21):
    random_diffs(i)
    level_list = []