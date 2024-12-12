turt_in_row = 5
globals()[f'game_board_{turt_in_row}'] = [['-' for column in range(turt_in_row)] for row in range(turt_in_row)] 
print(globals()[f'game_board_{turt_in_row}'])