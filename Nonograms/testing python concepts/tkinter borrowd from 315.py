import tkinter as tk

def back():
    pass
def submit_data():
    pass

def play_game():
    pass

##############################
# main program
##############################

# start the GUI forms
root = tk.Tk()
root.wm_geometry("800x500")
root.title("Data Collection")

screen_selection = int(input("Select which screen you'd like to see.\nType 1 for physiology\n \
2 for habits \n \
or 3 for confirmation message screen"))
if screen_selection == 1:

    ##############################
    # create frame for physiology
    ##############################
    frame_physiology = tk.Frame(root, height=500, width=800)

    frame_physiology.grid_propagate(0)
    frame_physiology.grid(row=0, column=0)

    # create the text boxes
    # height label
    lbl_height = tk.Label(frame_physiology, text='Enter your height:')
    lbl_height.grid(row=0, column=0, padx=20, pady=20)

    # text box for feet measurement
    ent_feet = tk.Entry(frame_physiology, width=5, bd=3)
    ent_feet.grid(row=0, column=1)

    # label for feet '
    lbl_feet = tk.Label(frame_physiology, text="'")  # feet
    lbl_feet.grid(row=0, column=2)

    # text box for inches measurement
    ent_inches = tk.Entry(frame_physiology, width=5, bd=3)
    ent_inches.grid(row=0, column=3)

    # label for inches "
    lbl_inches = tk.Label(frame_physiology, text='"')  # inches
    lbl_inches.grid(row=0, column=4)

    # hand length label
    lbl_hand_length = tk.Label(frame_physiology, text='Enter the length of your hand:' )
    lbl_hand_length.grid(row=1, column=0, padx=20, pady=10)

    # text box for inches measurement
    ent_hand_length = tk.Entry(frame_physiology, width=5, bd=3)
    ent_hand_length.grid(row=1, column=1)

    # label for inches "
    lbl_hand_inches = tk.Label(frame_physiology, text='"')  # inches
    lbl_hand_inches.grid(row=1, column=2)

    # hand injuries label
    lbl_injuries = tk.Label(frame_physiology, text='How many times have you injured your dominant hand?')
    lbl_injuries.grid(row=2, column=0, padx=20, pady=10)

    # text box for injuries
    ent_injuries = tk.Entry(frame_physiology, width=5, bd=3)
    ent_injuries.grid(row=2, column=1)

    # age label
    lbl_age = tk.Label(frame_physiology, text='How old are you?' )
    lbl_age.grid(row=3, column=0, padx=20, pady=10)

    # text box for age
    ent_age = tk.Entry(frame_physiology, width=5, bd=3)
    ent_age.grid(row=3, column=1)

    # handedness label
    lbl_handedness = tk.Label(frame_physiology, text='Are you right or left handed?')
    lbl_handedness.grid(row=4, column=0, padx=20, pady=10)

    # list box for handedness
    lst_handedness = tk.Listbox(frame_physiology, width=5, height=2, bd=3)
    lst_handedness.insert(0, "Right")
    lst_handedness.insert(1, "Left")
    lst_handedness.selectmode = tk.SINGLE
    lst_handedness.grid(row=4, column=1)

    # create Next button
    btn_next = tk.Button(frame_physiology, text='Next >>', command=next, padx=10, pady=10, bd=3)
    btn_next.grid(row=5, column=5)

elif screen_selection == 2:
    ##############################
    # create frame for habits data 
    ##############################
    frame_habits = tk.Frame(root, height=550, width=550)
    frame_habits.grid_propagate(0)
    frame_habits.grid(row=0, column=0)

    # hours of sleep label
    lbl_sleep = tk.Label(frame_habits, text='How many hours of sleep do you get per night?' )
    lbl_sleep.grid(row=0, column=0, padx=20, pady=20)

    # text box for sleep
    ent_hours_sleep = tk.Entry(frame_habits, width=5, bd=3)
    ent_hours_sleep.grid(row=0, column=1)

    # hours of activity label
    lbl_active = tk.Label(frame_habits, text='How many hours of exercise do you do per day?' )
    lbl_active.grid(row=1, column=0, padx=20, pady=20)

    # text box for activity
    ent_hours_active = tk.Entry(frame_habits, width=5, bd=3)
    ent_hours_active.grid(row=1, column=1)

    # glasses of milk label
    lbl_milk = tk.Label(frame_habits, text='How many glasses of milk do you drink per day?')
    lbl_milk.grid(row=2, column=0, padx=20, pady=20)

    # text box for milk
    ent_glasses_milk = tk.Entry(frame_habits, width=5, bd=3)
    ent_glasses_milk.grid(row=2, column=1)

    # create the buttons
    btn_back = tk.Button(frame_habits, text='<< Back', command=back,  padx=10, pady=10, bd=3)
    btn_back.grid(row=3, column=0, pady=20)
    btn_submit = tk.Button(frame_habits, text='Submit', command=submit_data, padx=10, pady=10, bd=3)
    btn_submit.grid(row=3, column=1)

elif screen_selection == 3:
    ##############################
    # create frame for confirmation message and launch of the turtle/sensor screen
    ##############################
    frame_confirmation = tk.Frame(root, height=550, width=550)
    frame_confirmation.grid_propagate(0)
    frame_confirmation.grid(row=0, column=0)
    msg_confirmation = tk.Message(frame_confirmation, 
                                text="Excellent! \n\n" +
                                    "It's time to test your grip strength by playing a game! \n\n" +
                                    "Hold the Hand Dynamometer in your dominant hand with its power button facing left. In the game, you must: \n" +
                                    "  a) Tilt the Dynamometer left and right to move the lander and collect the sensors that fell out of the spacecraft! \n" +
                                    "  b) Squeeze the sensor to slow down the lander's vertical speed. The stronger the squeeze, the slower the lander will fall. \n\n" +
                                    "Are you ready to play?", 
                                foreground="green",
                                width=450)
    msg_confirmation.grid(row=0, column=0, padx=20, pady=20)
    btn_play = tk.Button(frame_confirmation, text='Play the Game!', command=play_game, padx=10, pady=10, bd=3)
    btn_play.grid(row=1, column=0)

    # load = Image.open("csp315_sensor_hold.png")
    # render = ImageTk.PhotoImage(load)
    canvas = tk.Canvas(frame_confirmation, width = 195, height = 260)
    canvas.grid(row=2, column=0)
    # canvas.create_image(0,0,image=render,anchor=tk.NW)

root.mainloop()