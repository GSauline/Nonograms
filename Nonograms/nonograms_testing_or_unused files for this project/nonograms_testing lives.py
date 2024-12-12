import turtle as t

#new variables
lives = 3
heart_shift = 2 #amount to shift the hearts horizontally

#old variables
heart_img_empty = 'nonograms_images/empty-heart.gif' #found from https://www.shutterstock.com/image-vector/set-pixelated-heart-icons-digital-260nw-2320764891.jpg
heart_img_full = 'nonograms_images/full-heart.gif' #found from https://www.shutterstock.com/image-vector/set-pixelated-heart-icons-digital-260nw-2320764891.jpg
board_shift = 50        #amount is different based on size of screen
turtle_gap = 30 #gap between turtles on screen, fixed for whole program

#Make the screen, add the shapes
wn = t.Screen()
wn.addshape(heart_img_empty)
wn.addshape(heart_img_full)



##functions - per level
def place_lives():
    for i in range(lives):
        globals()[f'heart_{i}'] = t.Turtle(shape=heart_img_full)
        globals()[f'heart_{i}'].penup()
        globals()[f'heart_{i}'].goto(i*2*turtle_gap-board_shift, turtle_gap-board_shift)


place_lives()
wn.mainloop()
