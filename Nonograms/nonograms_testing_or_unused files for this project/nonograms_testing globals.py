choice = input("choose 1a, 1b, 2, 3, 4, or 5")
if choice == '1a':

    #1a. I want to test using globals() to define a variable, then redefining it the traditional way. 
    globals()['y'] = 5 
    print(y) 
    y=7 
    print(y) 
    print(globals())

elif choice == '1b':
    #1b.I want to test defining a variable, then redefining it using globals().  the traditional way
    z = 8
    print(z) 
    globals()['z'] = 5  
    print(z) 
    print(globals())

elif choice == '2':
    #2. testing defining and redefining with globals()
    globals()['x'] = 5 
    print(x) 
    globals()['x'] = 7 
    print(globals()) 

elif choice == '3':
    #3. I want to test defining a variable with globals() in a function.
    def define_with_globals():
        globals()['w'] = 10

    # print(w)
    define_with_globals()
    print(globals()['w'])
    print(w)
    print(globals())

elif choice == '4':
    #4. I want to test deleting a variable, and then redefining the variable with the same name. Does it work? 
    v = 8 
    print (globals()) 
    del v 
    print(globals()) 
    v =12 
    print(globals()) 

elif choice == '5':
    #5. I also want to test this same thing, but with the globals() keyword. 
    globals()['s'] = 9 
    print (globals()) 
    del s 
    print(globals()) 
    globals()['s'] =13 
    print(globals())

else:
    print('invalid choice.')