#testing_random_color_string.py

import turtle as t
import random as r

hex_characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
rand_color_char_list = [r.choice(hex_characters) for i in range(6)]
color_str = '#' +''.join(rand_color_char_list)

wn = t.Screen()
bob = t.Turtle()
bob.color(color_str)
default_delay = 5

#Optional function version of this code
#This funciton will make a given turtle's color change to a random color, then back to blue.
#This will be called across a column/ row when it is called.
def turt_random_color(turt):
    hex_characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    rand_color_char_list = [r.choice(hex_characters) for i in range(6)]
    color_str = '#' +''.join(rand_color_char_list)
    turt.color(color_str)
    wn.delay(50)
    turt.color("blue")
    wn.delay(default_delay)



t.mainloop()

