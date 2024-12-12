#testing_global_vs_local_turtles.py
'''
I’m thinking about how I create all the turtles for the gameboard. Presently, I have a nested loop that 
creates each turtle like this:
globals()[f'block_{i}_{j}'] = t.Turtle()
I create them all with globals, which returns a dictionary of all globals within a file. 
On the surface, it appears that creating my turtles with the globals() dictionary is necessary. 
The reason I thought it was necessary is because this is what I need to be able to do 
(to avoid using the globals() dictionary):
    Step 1: have a global dictionary to house all of the turtles that will live on the gameboard
    Step 2: inside a turtle_setup function, create all the uniquely named turtles, and append them to 
    the global dictionary.
    Step 3: after the function, the individual turtles need to still exist and be referenceable. 
    (For example, I need to reference them all when I turn on clicks). In other words, I need the turtles 
    created within the setup function to have global scope.

I knew that if I created the turtles "normally" within the setup function, they would only have local scope.
For example, 
turt_1 = t.Turtle()
turt_2 = t.Turtle()
...
I originally thought that I HAD to create the turtles as individual globals because 
I was not sure that step 3 above would still work without forcing my turtles to be globals. 
In other words, I thought that if I created those turtles within a function, they would only have local scope. 
What I did NOT know is that I could get around this issue of the turtles having local scope: if I 
APPEND those LOCAL turtle objects to a GLOBAL list/dictionary, then the turtle 
objects become GLOBAL and are referenceable outside of the initial function.
'''

import turtle as t

#with parameter identical to global
def turt_create(turt_list):
    colors = ['red', 'blue', 'green']
    for i in range(3):
        bob = t.Turtle()
        bob.color(colors[i])
        bob.goto(i*10, i*20)
        turt_list.append(bob)
        
    print(turt_list, 'in function')

def turt_create_no_param():
    colors = ['red', 'blue', 'green']
    for i in range(3):
        bob = t.Turtle()
        bob.color(colors[i])
        bob.goto(i*10, i*20)
        turt_list.append(bob)
        
    print(turt_list, 'in function')

wn = t.Screen()
turt_list = []
print('\n\n\n', turt_list, 'before function')
# turt_create(turt_list)
turt_create_no_param()
print(turt_list, 'after function')
wn.mainloop()

