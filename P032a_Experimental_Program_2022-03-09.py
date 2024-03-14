#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sunday, March 06 @ 14:00:56 2022

This script is the final version of the pigeon insight training task. It is well-
annotated and covers the four phases (and nine subphases) of training (detailed
below). The phase number/subnumber (for example, "1.a") is provided, along
with the count number (0-8) of each phase on the left. An explanatory flowchart
of each trial of each phase is also provided below the table. Note that the phase 
numbers used here differ from those used in the final manuscript; the order and 
descriptions remain equatable.

This code is entirely self-contained and requires no additional data or dependencies
other than Python3 and an empty "data" folder at the same directory as this
Python script. All graphics are built from scratch using Python's tkinter library.

This code was generated piece-by-piece, starting with phases 1-3. The order of
several components (e.g., functions) is reflected by this.

 Description
------------------------------------------------------------------------------   
  Phase 1: Single peck on the pacman is reinforced. 
      1.a - Location of pacman is fixed in the center of the screen for
            every trial. After a reinforced peck, everything onscreen will
            disappear as the hopper is activated (true across all phases).
      1.b - Same as 1.a, but the location of pacman is variable.    
      
  Phase 2: Reinforcement requires peck on pacman, then on pop-up cursor.
      2.a - Pacman location is variable at the start of the first trial. After
            a peck on the pacman, a cursor appears in one of four available 
            slots around the pacman (North. East, South, or West). A second 
            peck on the cursor will cause the cursor to dissapear and the 
            pacman to move in that direction, then lead to reinforcement.
      2.b - Same as 2.b, but all four ovals will appear around the pacman. A
            single peck on any cursor will cause the pacman to move in that
            direction, then reinforcement.
          
  Phase 3: Introduction of the goal (banana)
      3.a - Pacman start location is variable each trial. The banana goal 
            will be a single "move" away (e.g., the move distance away from
            the pacman). A peck on the pacman will cause one cursor to appear
            (in the direction of the banana). After a peck on that cursor,
            the pacman will move to the banana and "eat" it, pause, then 
            will lead to reinforcement.
      3.b - Similar to 3.a, but after a peck to the pacman all four cursors 
            will appear around the pacman. A correct choice (e.g., a peck on
            the cursor between the pacman and banana) will lead to
            reinforcement, while a peck on an incorrect cursor (one of the
            three that lead away from the banana) will be punished with a TO
            and no reinforcement before the next trial. This is the first 
            phase with an "incorrect" choice that is punished with a TO.
      3.c - The pacman and banana will now be two "moves" away from each
            other (randomly placed) at the start of each trial. Similar to
            3.a, only a single cursor will appear. This time, however, a
            second peck to the available cursor is required to reach the
            banana and be reinforced. For both 3.c and 3.d, the banana will
            be randomly placed to movements in the same direction (along
            vertical or horizontal axes), such that two of the same
            response-types are required to reach the banana. Note that a
            second peck to the pacman is not required to "activate" the
            cursor.
      3.d - A combination of 3.c and 3.b, the pacman and banana will be
            randomly placed two movement intervals away from each other. An 
            initial peck to the pacman will cause all four cursors to
            appear. The pigeon must peck the "correct" cursor twice to reach
            the banana goal. If the pacman has not reached the banana after
            two cursor pecks, there will be a TO interval followed by a the 
            next trial.

  Phase 4: Intuition test
      4.a - Similar to 3.d, but the goal and the banana are now aligned two  
            moves away along diagnal axes, such that two different moves are
            required for the pacman to reach the goal. For example: if the
            banana is to the northeast of the pacman, the pigeon must move
            either 1) north then east or 2) east then north to reach the 
            banana. If the pacman has not reached the target after two 
            moves, then the trial ends and is followed by a timeout. This is 
            the first time two seperate moves are required to reach the 
            banana AND the pigeon cannot just choose the cursor closest to 
            the banana.
      4.a TEST - Identical to 4.a (diagnal orientation of pacman and banana)
            with no punishment of exceeding trial par.
      4.b - This is a free-moving test in which the banana and the pacman
            are placed randomly anywhere on the screen. Efficiency was 
            tested by comparing the "par" for a trial to the number of 
            moves made in that session. This was the capstone test for
            the movement trainings (1 - 4).
            
            
  Phase 5: Barrier training
      5.a - Introduction of the barrier. In this training, the barrier was
            only a single "block" high and always appeared in a column that
            seperated the pacman (left) and banana (right) locations. The 
            location of the barrier was variable both in horizontal plane
            (2-5) and vertical plane (1-3), and pacman/banana were randomly
            placed on the vertical plane (ex. below)
      
           _____________         _____________          _____________
       1  |            |     1  |  |__|      |       1  |      P __  |
       2  |     ___    | OR  2  |P      B    | OR    2  |       |__| |
       3  |   P | | B  |     3  |            |       3  |           B|
           ------------          ------------            ------------  
            1 2 3 4 5 6          1 2 3 4 5 6             1 2 3 4 5 6  

      5.b - The same as 5.a, but with the location of the pacman (right) and 
            banana (left) were reversed 
      5.c - Very similar to both 5.a and 5.b, but the barrier was now two
            two blocks high instead of one (examples below). Pacman and 
            banana location varied left/right, but always ajacent to the barrier.
          _____________         _____________          _____________
       1  |     ___ B |     1  |  |__|      |       1  |      B| |P |
       2  |     | |   | OR  2  |P  __  B    | OR    2  |       |_|  |
       3  |   P | |   |     3  |  |  |      |       3  |            |
           ------------          ------------            ------------  
            1 2 3 4 5 6          1 2 3 4 5 6             1 2 3 4 5 6  

      5.d - The same as 5.c, but with the location of the pacman (right) and 
            banana (left) were reversed.
            
      5 TEST - Similar to 5.c and 5.d, but the pacman and banana locations 
            are randomized L/R and can be in any position left/right of the
            border. Additionally, the barrier can be one OR two units
          _____________         _____________          _____________
       1  |B    ___   |     1  |  |__|    B |       1  |       ___  |
       2  |     | |   | OR  2  |P           | OR    2  |  B    |_|  |
       3  |     | |  P|     3  |            |       3  |           P|
           ------------          ------------            ------------  
            1 2 3 4 5 6          1 2 3 4 5 6             1 2 3 4 5 6  
            
   Phase 6: Portal training
      6.a - The portal stimulus is first introduced. There are always TWO 
            portals (one to enter and one to exit), but they go both ways. 
            Each portal is inlaid into the border and is made up of two visual
            parts: 1. a square black "tunnel" that is moved through and 2. a 
            blue oval at the end where the pacman dissapears. This visual 
            stimulus was chosen in the hopes of relating an abstract concept
            to something that was already known, as well as facilitating the
            rules that only pecks on the guides moved the pacman (so we needed
            a stimulus where guides never overlapped with the portal).
            In the 6.a phase, the two portal locations were randomly placed 
            in two side or bottom border locations. The pacman and banana
            were directly placed at the entrance/exits to each portal (such 
            that only a single move was required for reinforcement). However,
            during this phase only a single guide appeared around the pacman
            in the direction of the nearest portal (so pigeons were forced to
            use the portal for reinforcement.)
                 _________________            _________________   
                |  _______________|          |  ____________   |   
               1|  |          B _0|         1|  |           |  |
               2|  |           |  |   OR    2|  |           |  | 
               3|  |    P      |  |         3|  |  B       P|  |      
                |  ---|  |------  |          |  -|  |----|  |  |
                -------0-----------          ------0-------0----  
                   1 2 3 4 5 6                   1 2 3 4 5 6    
               
    Phase 7: Insight test
        7 TEST - After the barrier and portal stimuli (and their rules) were
            each trained, we combined them together to see whether subjects
            showed insight-like behavior. This was done by introducing an 
            impassible barrier (3 vertical moves high) in between pacman and
            banana goal locations within the arena along with a portal on
            either side, such that the only way for the pacman to move to 
            the banana was through the portal.

                 _________________            _________________   
                |  _____  ________|          |  ______   ____  |   
               1|  |   |  |   P _0|         1|  |    |  |   |  |
               2|__|   |  |    |  |   OR    2|  |    |  |   |  | 
               3|0  B  |  |    |  |         3|  |  P |  |  B|  |      
                |-------  ------  |          |  -|  |-  -|  |  |
                -------------------          ------0-------0----  
                   1 2 3 4 5 6                   1 2 3 4 5 6    
                   
    Phase 8: Effeciency test
        8 TEST - After the insight test, we were curious whether pigeons had 
            only learned to solve the task by using the portal every trial. We
            then gave a series of trials that were solvable by BOTH using a 
            portal or navigation, but the EFFICIENCY of using either option
            differed by trial (e.g., the "par" for using the portal vs. just 
            cursor-based movement varied). We compared preference of portal
            vs. non-portal navigation across different trial types.
            
            
                 _________________            _________________   
                |  _____  ________|          |  ____________  |   
               1|  |   |  |   B _0|         1|  |         P|  |
               2|__|   |__|    |  |   OR    2|__|          |  | 
               3|0  P          |  |         3|0        B   |  |    
                |---------------  |          |-----| |-----|  |
                -------------------          -------0---------- 
                   1 2 3 4 5 6                   1 2 3 4 5 6    
_______________________________________________________________________________

                          *** TRIAL FLOWCHARTS ***
          
     I.    Training Phases 1.a and 1.b:    
            
            ITI ------------------------> Peck the  
             ^                             Pacman      
             |                               |
         Sets up the               Reinforcement of peck 
         next trial             via timed hopper access
             |                               |
             L_______________________________|
        ​
        ​
    II.    Training Phases 2.a and 2.b:
            
            ITI ----> Peck the  -------> Peck the Pacman 
             ^         Pacman       Guides to move the Pacman    
             |                                 |
         Sets up the               Reinforcement after pacman
         next screen              reaches movement destination              
             |                         
             L_________________________________|
        ​
        ​
     III.    Training Phases 3.a, 3.c, and 4.a:
            
            ITI ----> Peck the  ---> Peck the Pacman -----------> Reach the
             ^         Pacman         Guides to move             Goal (banana)
             |                             |                          |
         Sets up the               (1) If incorrect        (2) Reinforcement if the
         next trial (w/               move, trial is           goal is reached in the 
         random start)                punished with a         allocated 1 or 2 moves
             |                        unreinforced TO                 |
             |                               |                        |
             L________________________________________________________|
             
             
     IV.    Training Phases 3.b, 3.d, 4.a TEST, 4.b, and all of phase 5:
            
            ITI ----> Peck the  ---> Peck the Pacman ---> Reach the
             ^         Pacman         Guides to move     Goal (banana)
             |                                                 |
         Sets up the                                  Reinforcement when the
         next trial (w/                             goal is reached regardless
         random start)                                   of num. of moves
             |                                                  |          
             |                                                  |
             L__________________________________________________|     
        
     
    V.    Training Phases 6a through Test Phase 8:
            
            ITI --> Peck the --> Peck the Pacman --> Use the portals---> Reach the
             ^       Pacman      Guides to move        (if required)    Goal (banana)
             |                                                              |
         Sets up the                                                        |
         next trial (w/                                             Reinforcement when
         random start                                                 goal is reached
          location)                                                         |          
             |                                                              |
             L______________________________________________________________|
     

@authors: Cyrus Kirkman, Rafael Rodrigues, and Michael Nirula.
"""
# The first variable declared is whether the program is the operant box version
# for pigeons, or the test version for humans to view. The variable below is 
# a T/F boolean that will be referenced many times throughout the program 
# when the two options differ (for example, when the Hopper is accessed or
# for onscreen text, etc.). It needs to be changed manually based on whether
# the program is running in operant boxes (True) or not (False).
operant_box_version = False

# Then, import the necessary libraries to run:
from tkinter import Tk, Label, Button, StringVar, OptionMenu, IntVar, \
    Radiobutton, Toplevel, Canvas, PIESLICE, BOTH
from math import copysign
from datetime import datetime, date
from csv import writer, QUOTE_MINIMAL
from random import randint, choice
from os import getcwd, mkdir, path as os_path
from sys import setrecursionlimit, path as sys_path

# Import hopper/other specific libraries from files on operant box computers
if operant_box_version:
    cwd = getcwd()
    sys_path.insert(0, str(os_path.expanduser('~')+"/OneDrive/Desktop/Hopper_Software"))
    try:
        import random_pigeon_paint
        from hopper import HopperObject
    except ModuleNotFoundError:
        print("ERROR: Hopper software not found!\n You may be running the operant box version of this program on accident?")
        input("Press <enter> to continue...")
# Below  is just a safety measure to prevent too many recursive loops). It
# doesn't need to be changed.
setrecursionlimit(5000)

# Then, introduce the first control panel object. This object is a pop-up
# window that takes experimental inputs for the current session (for example:
# subject number, training phase, etc.)
class ExperimenterControlPanel(object):
    # The init function declares the inherent variables within that object...
    def __init__(self):
        # First set up the operant box specific varaiables
        if operant_box_version:
            # Setup the data directory in "Documents"
            self.doc_directory = str(os_path.expanduser('~'))+"/Documents/"
            self.data_folder = "P032a_data" # The folder within Documents where subject data is kept
            self.data_folder_directory = str(os_path.expanduser('~'))+"/OneDrive/Desktop/Data/" + self.data_folder
        # Set hopper object to be a variable of self, so it can be referenced...
            self.Hopper = HopperObject()
        else:
            self.data_folder_directory = getcwd() + "/data/"
            self.Hopper = None
            
        # Setup the root Tkinter window that will appear onscreen
        self.control_window = Tk()
        self.control_window.title("Experimental Control Panel")

        ##  Next, setup variables within the control panel
        # Subject ID
        self.pigeon_name_list = ["Darwin", "Athena", "Estelle",
                                 "Bowser", "Wario", "Herriot",
                                 "Mario", "Yoshi"]
        self.pigeon_name_list.sort() # This alphabetizes the list
        self.pigeon_name_list.insert(0, "TEST")
        Label(self.control_window,
              text="Pigeon Name:").pack()
        self.subject_ID_variable = StringVar(self.control_window)
        self.subject_ID_variable.set("Select")
        self.subject_ID_menu = OptionMenu(self.control_window,
                                          self.subject_ID_variable,
                                          *self.pigeon_name_list,
                                          command=self.set_pigeon_ID).pack()
        
        # Choice/simple task
        Label(self.control_window,
              text = "Select training").pack()
        self.training_phase_variable = IntVar()
        self.training_phase_name_list = ["1.a: Fixed pacman position",
                                    "1.b: Variable pacman position",
                                    "2.a: Single cursor",
                                    "2.b: Multiple cursors",
                                    "3.a: Single cursor, one move",
                                    "3.b: Multiple cursors, one move",
                                    "3.b TEST",
                                    "3.c: Single cursor, two moves",
                                    "3.d: Multiple cursors, two moves",
                                    "3.d TEST",
                                    "4.a: Diagnal",
                                    "4.a TEST",
                                    "4.b: Random locations",
                                    "5.a: Left single barrier",
                                    "5.b: Right single barrier",
                                    "5.c: Left double barrier",
                                    "5.d: Right double barrier",
                                    "5 TEST",
                                    # "6.a: Portal training, one move",
                                    # "6.b: Portal training, multiple moves",
                                    # "6.c: Portal training, barrier (OPTIONAL)",
                                    "6: Portal, green dot",
                                    "7 TEST: Insight"
                                    ]
        self.training_phase_variable = StringVar(self.control_window)
        self.training_phase_menu = OptionMenu(self.control_window,
                                  self.training_phase_variable,
                                  *self.training_phase_name_list).pack()
        self.training_phase_variable.set(self.training_phase_name_list[18]) # Default set to first training phase
        
        # Record data variable
        Label(self.control_window,
              text = "Record data in seperate data sheet?").pack()
        self.record_data_variable = IntVar()
        Radiobutton(self.control_window,
                    variable = self.record_data_variable,
                    text = "Yes",
                    value = True).pack()
        Radiobutton(self.control_window,
                    variable = self.record_data_variable,
                    text = "No",
                    value = False).pack()
        self.record_data_variable.set(True) # CHANGE Default set to True
        # Start/exit buttons
        Button(self.control_window,
               text = 'Start program',
               bg = "green2",
               command = self.build_chamber_screen).pack()
        self.control_window.mainloop() # This loops around the CP object
        self.MS = None # This will be the mainscreen object
    
    def set_pigeon_ID(self,pigeon_name):
        # This function checks to see if a pigeon's data folder currently 
        # exists in the respective "data" folder within the Documents
        # folder and, if not, creates one.
        if operant_box_version:
            try:
                if not os_path.isdir(self.data_folder_directory + pigeon_name):
                    mkdir(os_path.join(self.data_folder_directory, pigeon_name))
                    print("\n ** NEW DATA FOLDER FOR %s CREATED **" % pigeon_name.upper())
            except FileExistsError:
                print("Data folder for %s exists." % pigeon_name) 
            except FileNotFoundError:
                print("\n ERROR: Data folder not found")
        else: # If on non-lab computer...
            try:
                parent_directory = getcwd() + "/data/"
                if not os_path.isdir(parent_directory + pigeon_name):
                    mkdir(os_path.join(parent_directory, pigeon_name))
                    print("\n ** NEW DATA FOLDER FOR %s CREATED **" % pigeon_name.upper())
            except FileNotFoundError:
               print("\n ERROR: Data folder not found")
    
    def build_chamber_screen(self):
        # Once the green "start program" button is pressed, then the mainscreen
        # object is created and pops up in a new window. It gets passed the
        # important inputs from the control panel.
        if self.subject_ID_variable.get() in self.pigeon_name_list and os_path.isdir(self.data_folder_directory):
            training_phase_str = self.training_phase_variable.get().split(":")[0]
            print(f"\n - SESSION STARTED for {training_phase_str}")
            self.MS = MainScreen(
                self.Hopper, # Hopper object
                str(self.subject_ID_variable.get()), # subject_ID
                training_phase_str, # Which training phase (as string)
                self.record_data_variable.get(), # T/F to record data
                self.data_folder_directory, # Directory to data folder
                )
        else:
            if not self.subject_ID_variable.get() in self.pigeon_name_list:
                print("\n ERROR: Input Correct Pigeon ID Before Starting Session")
            elif not os_path.isdir(self.data_folder_directory):
                print("\n ERROR: Data folder not found")

#%% Mainscreen object

class MainScreen(object):
    # The Mainscreen object is passed the Hopper object, subject_ID (string),
    # training phase (number 0 - 1), and the record data value (T/F) in that
    # order.
    def __init__(self, Hopper, ID, training_phase, record_data, data_folder_directory):
        # First set the passed variables to be inherent variables within the
        # newly created MainScreen object
        self.Hopper = Hopper
        self.training_phase = training_phase
        self.record_data = record_data
        self.data_folder_directory = data_folder_directory
        self.subject = ID # Name of each subject
        # Then, set up the required tkinter objects/variables required to build
        # the GUI screen and to keybind any functions
        self.root = Toplevel()
        self.root.title("P032a: Insight Task Training") # this is the title of the windows
        self.mainscreen_height = 600 # height of the experimental canvas screen
        self.mainscreen_width = 800 # width of the experimental canvas screen
        self.root.bind("<Escape>", self.exit_program) # bind exit program to the "esc" key
        if operant_box_version: 
            # Keybind relevant keys
            self.cursor_visible = True # Cursor starts on...
            self.change_cursor_state("event") # turn off cursor UNCOMMENT
            self.root.bind("<c>", self.change_cursor_state) # bind cursor on/off state to "c" key
            # Then fullscreen (on a 800x600p screen)
            self.root.attributes('-fullscreen', True)
            self.mastercanvas = Canvas(self.root,
                                   bg="black")
            self.mastercanvas.pack(fill = BOTH, expand = True)
        else: 
            # No keybinds and  800x600p fixed window
            self.mastercanvas = Canvas(self.root,
                                   bg="black",
                                   height=self.mainscreen_height,
                                   width = self.mainscreen_width)
            self.mastercanvas.pack()
        ## STATE VARIABLES:
        # This is where any variables (subject to change) are initially stated prior to 
        # running any complex code; these variables can be changed without affecting 
        # the calculation of other variables later on. These values have been
        # constructed as changeable variables so that they can be tweaked 
        # throughout the pilot and future studies.
        self.trial_number= 1 # Number of the corresponding trial
        self.reinforcers_provided = 0 # Number of reinforcers provided (i.e., reinforced trials);
        self.max_reinforcers_per_session = 75 # Total completed reinforcers provided  before the session ends
        # Movement or cursor oval-specific variables
        self.oval_tags = ["north_oval_pacman",
                          "east_oval_pacman",
                          "south_oval_pacman",
                          "west_oval_pacman"]
        self.oval_width = 30 # This is the number of pixels wide & tall  (diameter) each oval is
        self.oval_pacman_gap = 8 # The gap between outside of square pacman and closest oval point
        self.ovals_onscreen = False # This binary tracks whether the ovals are already visible
        self.banana_direction = None # this is the banana direction (NESW) from the pacman for phases 4 and 6
        self.move_keys = ["w", "d","s","a"] # Keybound arrows to move pacman N/E/S/W
        self.move_distance = 120 # this is the distance (in pixels) the pacman moves
        self.movement_resolution = 2 # The number of pixels moved per loop iteration
        self.ms_per_pixel_speed = 8 * self.movement_resolution # This is the pacman movement speed in ms per pixel
        # Pacman-specific variables
        self.pacman_color = "red" # the color of the pacman object
        self.pacman_size = 60 # length and width of pacman object
        self.pacman_move_delay = 600 # Delay in ms for pacman after oval is pecked
        self.goal_coords = None # The coordinates for the goal will be reset later
        self.green_dot_coords = None
        # Timing variables (in milliseconds)
        self.reinforcer_interval = 3 * 1000 # Length of reinforcer access
        self.ITI_duration = 5 * 1000 # Inter-trial interval duration
        if self.subject == "TEST":
            self.ITI_duration = 5
        self.TO_duration = 8 * 1000 # Timeout duration (after "incorrect" choice)
        
        # Determine the trial par (or the minimum number of moves it will take
        # the pacman to reach the banana goal. During training, par will be
        # the same across trials within each session type
        if self.training_phase in ["1.a", "1.b", "2.a", "2.b", "6.a","6.b", "6.c", "6"]: # If there's no goal
            self.trial_par = None
        self._ideal_strategy = "nonportal" # Default strategy is not to use a portal
    
        # Below is a counter for the current moves in each trial. If it exceeds 
        # the trial_par value declared above, then the trial ends and results
        # in a punishment. The self.current_trial_moves variable is incremented
        # by 1 for each move, and is reset to zero at the start of each new trial.
        self.current_trial_moves = 0
        
        ## All the code related to data collection is seted bellow. By the end of each
        # trial, a different csv document is created, with the corresponding data. 
        self.start_time = datetime.now() # This is where the beggining time of the trial is seted 
        self.local_trial_timer = datetime.now() # Tracks time w/in each trial
        # The following matrix corresponds to the initial and empty matrix that will be
        # completed with the data from the trial. The first list (or "row" in
        # the matrix are the column header values).
        self.session_data_matrix =  [["Time", "EventType", "Xcord", "Ycord",
                                    "TransformedXcord", "TransformedYcord",
                                    "PacmanXcord", "PacmanYcord",
                                    "TrialNum", "MoveCounter","TrialPar",
                                    "TrialTime", "Subject", "TrainingPhase",
                                    "Date", "InsightTrialType"]]
        
        ## BARRIERS AND BORDERS:
        # This is where any barrier dimensions are stated in the matrix below, or 
        # borders of the screen are given. The pacman will not be able to overlap with
        # any of these. 
        self.barrier_dimension_matrix = []
        self.border_depth_dict = {
            "left":65,
            "right":65,
            "bottom":60,
            "top":225} #Left, right, bottom, top border depths (pixels)
        self.border_dimensions_matrix = [[0,
                                          0,
                                          self.border_depth_dict["left"],
                                          self.mainscreen_height], #left border
                                    [self.mainscreen_width - self.border_depth_dict["right"],
                                     0,
                                     self.mainscreen_width,
                                     self.mainscreen_height], #right border
                                    [0,
                                     self.mainscreen_height - self.border_depth_dict["bottom"],
                                     self.mainscreen_width,
                                     self.mainscreen_height], # bottom border
                                    [0,
                                     0,
                                     self.mainscreen_width,
                                     self.border_depth_dict["top"]]] # top border
        # Once these active "arena" dimensions are established, we can calculate
        # the number of vertical and horizontal moves that are possible in 
        # each dimension. These values will later correspond to the grid
        # used to assign locations of objects.
        self.horizontal_moves_in_arena = (self.mainscreen_width - self.border_depth_dict["left"] - self.border_depth_dict["right"] - self.pacman_size) // self.move_distance
        self.vertical_moves_in_arena = (self.mainscreen_height - self.border_depth_dict["bottom"] - self.border_depth_dict["top"]- self.pacman_size) // self.move_distance
        # These are the base banana dimensions. They are further calculated
        # from the goal coordinates (when determined)
        self.base_banana_dimensions = [11, 0, 12, 1, 13, 2, 12, 4, 12, 5, 11,
                                       7, 11, 9, 11, 12, 12, 15, 13, 19, 16, 22,
                                       18, 24, 24, 27, 29, 28, 34, 30, 36, 31,
                                       38, 32, 38, 34, 38, 34, 38, 35, 34, 38,
                                       28, 38, 23, 38, 17, 36, 10, 32, 6, 28, 4,
                                       25, 1, 19, 1, 16, 1, 14, 1, 11, 2, 10, 3,
                                       8, 5, 6, 6, 6, 8, 6, 9, 2, 9, 1, 10, 0]
        # These are the stain on banana dimensions
        self.base_banana_brown_dimensions = [6, 12, 5, 14, 5, 16, 6, 18, 7, 21,
                                             9, 23, 11, 26, 13, 28, 15, 30, 18,
                                             31, 21, 33, 24, 33, 26, 34, 27, 33,
                                             26, 32, 24, 32, 22, 31, 19, 29, 17,
                                             28, 14, 25, 12, 23, 10, 20, 8, 16,
                                            7, 14]
        # A list of all the objects in "preset" insight levels
        self.insight_trial_dictionaries = [{"Trial Type": 7.1,
                                            "Pacman Grid Location":[0,2],
                                                "Banana Grid Location": [5,0],
                                                "Barrier Grid Matrix":[[1,2],[4,0],[4,1], [4,2]],
                                                "Portal Grid Matrix":[[2,3],[6,1]]},
                                           {"Trial Type": 7.2,
                                                "Pacman Grid Location":[5,0],
                                                "Banana Grid Location": [0,2],
                                                "Barrier Grid Matrix":[[1,2], [3,0],[3,1],[3,2]],
                                                "Portal Grid Matrix":[[2,3],[6,2]]},
                                           {"Trial Type": 7.3,
                                                "Pacman Grid Location":[2,2],
                                                "Banana Grid Location": [5,0],
                                                "Barrier Grid Matrix":[[1,2], [4,0],[4,1],[4,2]],
                                                "Portal Grid Matrix":[[0,3],[6,1]]},
                                           {"Trial Type": 7.4,
                                                "Pacman Grid Location":[5,0],
                                                "Banana Grid Location": [2,2],
                                                "Barrier Grid Matrix":[[1,2], [3,0],[3,1],[3,2]],
                                                "Portal Grid Matrix":[[0,3],[6,2]]},
                                           {"Trial Type": 7.5,
                                                "Pacman Grid Location":[2,1],
                                                "Banana Grid Location": [5,2],
                                                "Barrier Grid Matrix":[[1,2],[3,1],[3,2]],
                                                "Portal Grid Matrix":[[0,3],[-1,0]]}
                                           ]
        self.insight_trial_type = None # This will be changed
        self.portal_accessed = False
        # Below is are the functions that are called to first kick-off the 
        # program for the first trial. 
        self.place_birds_in_box()
        # Lastly, this root.mainloop() line is ESSENTIAL to ensuring that the Canvas 
        # object keeps running. Note that you are only able to have one of these
        # lines, and the location of can be difficult to locate.
        self.root.mainloop()
        
    def place_birds_in_box(self):
        # This is the default screen run until the birds are placed into the
        # box and the space bar is pressed. It then proceedes to the ITI. It only
        # runs in the operant box version. After the space bar is pressed, the
        # "first_ITI" function is called for the only time prior to the first trial
        
        def first_ITI(event):
            # Is initial delay before first trial starts. It first deletes all the
            # objects off the mnainscreen (making it blank), unbinds the spacebar to 
            # the first_ITI link, followed by a 30s pause before the first trial to 
            # let birds settle in and acclimate.
            self.start_time = datetime.now() # reset when first trial actually starts
            self.mastercanvas.delete("all")
            self.root.unbind("<space>")
            # After that's established, we can start setting up the first trial
            if self.subject == "TEST": # If test, don't worry about first ITI delay
                self.root.after(3, lambda: self.set_up_trial())
            else:
                self.root.after(30000, lambda: self.set_up_trial())
        
        if operant_box_version:
            self.root.bind("<space>", first_ITI) # bind cursor state to "space" key
            self.mastercanvas.create_text(350,300,
                                          fill="white",
                                          font="Times 20 italic bold",
                                          text=f"Place bird in box, then press space \n Subject: {self.subject} \n Training Phase: {self.training_phase}")
        else:
            first_ITI("event")
        
    def change_cursor_state(self, event):
        # This function toggles the cursor state on/off. It is only run during
        # the operant box version of the program. Note that when the "c" key is
        # pressed, it sends an "event" details argument to the function (which
        # we don't need to do anything with in this context), but we still 
        # have to account for it.
        if self.cursor_visible: # If cursor currently on...
            self.root.config(cursor="none") # Turn off cursor
            print("### Cursor turned off ###")
            self.cursor_visible = False
        else: # If cursor currently off...
            self.root.config(cursor="") # Turn on cursor
            print("### Cursor turned on ###")
            self.cursor_visible = True
    
    def convert_grid_to_coordinate(self, xgrid, ygrid):
        # This function converts grid coordinates (ex. [0, 4]) and converts
        # them to four literal pixel coordinates (x1, y1, x2, and y2) based
        # upon the orientation of several other key variables. Throughout 
        # this program, we will conceptualize locations in terms of the grid
        # location first, then convert them to physical pixel coordinates 
        # using this function. We do this because:
        #   1)  a small two-dimensional 9 x 5 grid is much easier to
        #       conceptualize and add objects to (especially when controlling
        #       for move distance) compared to the massive 800 x 600p Canvas
        #       grid that is the actual background
        #   2)  The grid system should be easy to replicate across different
        #       screen sizes and visual systems, as well as when using different
        #       stimulus sizes and movement distances. For example, one could 
        #       easily convert the program to 150% pacman move distance (6x2)
        #       or run on a 1800 x 600p screen.
        xcoord = self.border_depth_dict["left"] + self.oval_pacman_gap + (self.move_distance * xgrid)
        ycoord = self.border_depth_dict["top"] + self.oval_pacman_gap + (self.move_distance * ygrid)
        return ([xcoord,
                 ycoord,
                 xcoord + self.pacman_size,
                 ycoord + self.pacman_size])
    
    def portal_grid_to_coordinate(self, xgrid, ygrid):
        # This function takes a "grid-like" input of where the portal will
        # appear in extended reference to the pacman/banana grid. The x and 
        # y grid portal coordinates will ALWAYS be on the perimeter of 
        # the active arena. In our case, there are six horizontal positions
        # (so the xgrid value is either 0 OR 7 OR...) and three vertical locations
        # (...OR the ygrid is 3). Note there are no portals built on top
        # of the arena because the pigeons couldn't reach them easily.
        
        # It returns two lists: the first is the black square "tunnel" that
        # overlaps the barrier, the second is the oval for the actual portal
        # on the edge of the screen.
        
        # First, we calculate the vertical and horizontal dimensions of the arena
        arena_height = self.mainscreen_height - self.border_depth_dict["bottom"] - self.border_depth_dict["top"]
        arena_width = self.mainscreen_width - self.border_depth_dict["left"] - self.border_depth_dict["right"]
        # Next, we divide the vertical and horizontal dimensions by the 
        # the number of possible locations to find the size of each portal.
        # Note that vertical and horizontal portals differ in size very 
        # slightly b/c of the difference in location/moves (not square)
        vertical_portal_dims = arena_height/(self.vertical_moves_in_arena + 1)
        horizontal_portal_dims = arena_width/(self.horizontal_moves_in_arena + 1)
        # Then we can give the radius of the portal oval
        portal_radius = 15
        
        # First we have to figure out if the portal appears to the left
        # of the arena, the right, or below:
        if xgrid < 0: # If true, we're dealing with a vertical portal on the left
            # First calculate the black background (or "tunnel") through the
            # barrier to the portal.
            bkgrd = [0,
                    self.border_depth_dict["top"] + ygrid * vertical_portal_dims + 1,
                    self.border_depth_dict["left"] + 1,
                    self.border_depth_dict["top"] + (ygrid+1) * vertical_portal_dims]
            # Then the dimensions of the portal oval.
            portal = [bkgrd[0] - portal_radius,
                      bkgrd[1],
                      bkgrd[0] + portal_radius,
                      bkgrd[3]]

        elif xgrid > self.horizontal_moves_in_arena: # Vertical portal on right
           bkgrd = [self.mainscreen_width - self.border_depth_dict["right"],
                   self.border_depth_dict["top"] + ygrid * vertical_portal_dims + 1,
                   self.mainscreen_width,
                   self.border_depth_dict["top"] + (ygrid+1) * vertical_portal_dims -1]
           portal = [bkgrd[2] - portal_radius,
                      bkgrd[1],
                      bkgrd[2] + portal_radius,
                      bkgrd[3]]
          
        elif ygrid > self.vertical_moves_in_arena: # horizontal portal
            bkgrd = [self.border_depth_dict["left"] + xgrid * horizontal_portal_dims + 1,
                    self.mainscreen_height - self.border_depth_dict["bottom"],
                    self.border_depth_dict["left"] + (xgrid + 1) * horizontal_portal_dims - 1,
                    self.mainscreen_height]
            portal = [bkgrd[0],
                      bkgrd[3] - portal_radius,
                      bkgrd[2],
                      bkgrd[3] + portal_radius]

        return [bkgrd, portal]
        
    def set_up_trial (self):
        # This is the first function called to set up each trial. It builds
        # all the objects for each trial and is pretty lengthy. Note that it
        # asks for the self.training_phase to determine which objects should
        # be built.
        
        def rand_grid_location():
            # This just returns a random x/y location on the 6x3 grid of
            # active space.
            return ([randint(0, self.horizontal_moves_in_arena),
                     randint(0, self.vertical_moves_in_arena)
                ])
        
        def calculate_banana_dims(x, y, coordinate_list):
            # This function calculates the new banana dimensions based on the 
            # randomly determined grid locations for both "banana_dimensions"
            # and "banana_brown_dimensions." The original banana dimensions
            # provided in the "init" function are static and based upon a 
            # original pacman size of 40p in diameter. Therefore, whenever
            # the pacman size is changed, the banana dimensions should shift
            # with it to match the pacman ratio size
            is_x = True
            new_dimensions = []
            for dim in coordinate_list:
                if is_x:
                    new_dimensions.append(dim*(self.pacman_size/40-.1) + x)
                else:
                    new_dimensions.append(dim*(self.pacman_size/40-.1) + y)
                is_x = not is_x
            return new_dimensions
        
        def banana_location_from_pacman():
            # This function randomly determines the orientation of banana to
            # the goal based on the number of steps between them. It takes the
            # training phase and returns the grid location of the banana.
            location_determined = False
            if self.training_phase in ["3.a","3.b","3.b TEST"]:
                # This is true for phases in which the banana is a single step
                # away from the pacman.
                number_of_steps = 1
            elif self.training_phase in ["3.c", "3.d", "3.d TEST"]:
                # This is true for phases in which the banana is a two steps
                # away from the pacman. 
                number_of_steps = 2
            while not location_determined:
                banana_location = [0,0]
                # As long as the projected location of the banana is not
                # negative (e.g., it is within the bounds of the active space)
                if self.training_phase in ["4.a","4.a TEST"]:
                    # When the banana is at a diagnal from the pacman
                    random_direction = choice(["northeast",
                                               "southeast",
                                               "southwest",
                                               "northwest"])
                else:
                    random_direction = choice(["north",
                                                "east",
                                                "south",
                                                "west"])
                # Test if that direction is within the bounds...
                if random_direction == "north":
                    banana_location[0] = pacman_grid_location[0]
                    banana_location[1] = pacman_grid_location[1] - number_of_steps
                elif random_direction == "east":
                    banana_location[0] = pacman_grid_location[0] + number_of_steps
                    banana_location[1] = pacman_grid_location[1]
                elif random_direction == "south":
                    banana_location[0] = pacman_grid_location[0]
                    banana_location[1] = pacman_grid_location[1] + number_of_steps
                elif random_direction == "west":
                    banana_location[0] = pacman_grid_location[0] - number_of_steps
                    banana_location[1] = pacman_grid_location[1]
                elif random_direction == "northeast":
                    banana_location[0] = pacman_grid_location[0] + 1
                    banana_location[1] = pacman_grid_location[1] - 1
                elif random_direction == "southeast":
                    banana_location[0] = pacman_grid_location[0] + 1
                    banana_location[1] = pacman_grid_location[1] + 1
                elif random_direction == "southwest":
                    banana_location[0] = pacman_grid_location[0] - 1
                    banana_location[1] = pacman_grid_location[1] + 1
                elif random_direction == "northwest":
                    banana_location[0] = pacman_grid_location[0] - 1
                    banana_location[1] = pacman_grid_location[1] - 1
                    
                if 0 <= banana_location[0] <= self.horizontal_moves_in_arena and 0 <= banana_location[1] <= self.vertical_moves_in_arena:
                    self.banana_direction = random_direction
                    location_determined = True  
        
            return banana_location

        def get_trial_par(pac_grid_list, ban_grid_list, bar_grid_list, portal_grid_matrix):
            
            # First, we build a matrix that represents all the possible moves in the arena.
            # Dimensions of the arena matrix are calculated as the num. of columns equal
            # to the number of possible horizontal moves plus two (to account for left/right
            # borders) and rows equal to verical moves plus two (top/bottom borders).
            # Each cell in this matrix will either be a 1 (representing a border or wall)
            # or a 0 (open or "moveable" space). Below is an example of a 8c x 5r arena
            # matrix representing a 6 x 3 movement arena.
            # 
            #         [[1, 1, 1, 1, 1, 1, 1, 1],
            #          [1, 0, 0, 0, 0, 0, 0, 1], 
            #          [1, 0, 0, 0, 0, 0, 0, 1], 
            #          [1, 0, 0, 0, 0, 0, 0, 1],
            #          [1, 1, 1, 1, 1, 1, 1, 1]]
            # 
            arena_matrix = [
                 [1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 0, 0, 0, 0, 0, 0, 1], 
                 [1, 0, 0, 0, 0, 0, 0, 1], 
                 [1, 0, 0, 0, 0, 0, 0, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1]
                 ]
            
            # Next up, lets create a function just prints a matrix passed to it
            # (for testing)
            def print_m(m):
                for i in range(len(m)):
                    for j in range(len(m[i])):
                        print( str(m[i][j]).ljust(2),end=' ')
                    print()
            
            # Next, we can add "barriers" into the arena. For example, let's put two
            # barriers into the arena  at grid locations (x: 3, y: 2) and (x: 3, y: 3).
            # Note that, for the arena matrix, this would actually be changing values at
            # [2+1][3 + 1] and [3+1][3+1] because of the borders.
            # 
            #         [[1, 1, 1, 1, 1, 1, 1],
            #          [1, 0, 0, 0, 0, 0, 1], 
            #          [1, 0, 0, 1, 0, 0, 1], 
            #          [1, 0, 0, 1, 0, 0, 1],
            #          [1, 1, 1, 1, 1, 1, 1]]
            # 
            # Note that this algorithm will only work if there is a solution to the 
            # maze (e.g., a path from pacman --> banana).
            for c_list in bar_grid_list:
                arena_matrix[c_list[1]+1][c_list[0]+1] = 1
            
            # print(" Arena matrix with borders/barriers:")
            # print_m(arena_matrix)
            # After we declare the arena matrix for this trial, we can declare the
            # start location of the pacman and banana goal. For this example, we can place
            # the pacman at (3,2)--bottom left side of the barrier--and the banana goal
            # at (3,4)--bottom right of the barrier. For purely visualizition sake,
            # locations of each are given below (note that these values are not actually
            # changed in the matrix, which is always made up of zeros and ones):
            #
            #         1  1  1  1  1  1  1
            #         1  0  0  0  0  0  1 
            #         1  0  0  1  0  0  1 
            #         1  0  P  1  B  0  1
            #         1  1  1  1  1  1  1
            #
            # Additionally note that the xy coordinate order is reversed when 
            # indicing a matrix when compared to our grid randomizer
            
            pacman_location = (pac_grid_list[1] + 1, pac_grid_list[0] + 1)
            banana_location = (ban_grid_list[1] + 1, ban_grid_list[0] + 1)
            
            
            # This code below builds another matrix that is full of zeros, except for the
            # pacman starting point location that is filled in with a "1". It looks like: 
            # 
            #       0  0  0  0  0  0  0  
            #       0  0  0  0  0  0  0   
            #       0  0  0  0  0  0  0  
            #       0  0  1  0  0  0  0  
            #       0  0  0  0  0  0  0  
            
            move_matrix = []
            for i in range(len(arena_matrix)):
                move_matrix.append([])
                for j in range(len(arena_matrix[i])):
                    move_matrix[-1].append(0)
            i,j = pacman_location
            move_matrix[i][j] = 1
            
            # Next, we define a function that "makes a move" from the pacman starting
            # point. The function starts by taking the new matrix above with a "1" pacman 
            # starting point. Each point surrounding that start point that is not a 
            # border/barrier in the original arena matrix (e.g., a potential "move") is
            # then labeled with a "2." Next, every potential move surrounding those "2"s
            # that are not a border/barrier or already filled will be filled in with a "3."
            #  3's are then surrounded with 4's, etc. until finally a number is placed in
            # the provided banana location. A visual representation of the end of this
            # process for the matrix example above is:
            #   
            #       0  0  0  0  0  0  0  
            #       0  4  3  4  5  6  0  
            #       0  3  2  0  6  7  0  
            #       0  2  1  0  7  0  0  
            #       0  0  0  0  0  0  0  
            
            def make_move(k):
              for i in range(len(move_matrix)): # For each row
                for j in range(len(move_matrix[i])): # For each column
                  if move_matrix[i][j] == k:
                    if i>0 and move_matrix[i-1][j] == 0 and arena_matrix[i-1][j] == 0:
                      move_matrix[i-1][j] = k + 1
                    if j>0 and move_matrix[i][j-1] == 0 and arena_matrix[i][j-1] == 0:
                      move_matrix[i][j-1] = k + 1
                    if i<len(move_matrix)-1 and move_matrix[i+1][j] == 0 and arena_matrix[i+1][j] == 0:
                      move_matrix[i+1][j] = k + 1
                    if j<len(move_matrix[i])-1 and move_matrix[i][j+1] == 0 and arena_matrix[i][j+1] == 0:
                       move_matrix[i][j+1] = k + 1
            
            # The k variable below the "move" count that we are currently on. It
            # incrementally cycles through the make_move() function above until the 
            # banana goal location value is changed from zero to another value.
            # Also, there's a safety counter that will break the loop if 
            # there's no solution.
            k = 1
            safety_counter = self.vertical_moves_in_arena * self.horizontal_moves_in_arena
            while move_matrix[banana_location[0]][banana_location[1]] == 0:
                make_move(k)
                k += 1
                safety_counter -= 1
                if safety_counter < 0:
                    print("No non-portal solution to maze")
                    break
            
            if safety_counter > 0:    
                print(f"Par (n = {k-1}) non-portal solution as matrix:")
                print_m(move_matrix)
                
            # If the phase does NOT include portals, then we're done...
            if portal_grid_matrix == None:
                    return k-1
            # if it does have portals, we perform the same thing EXCEPT now we
            # include the portals in the arena matrix 
            else:
                portal1_location = (portal_grid_matrix[0][1] + 1,
                                    portal_grid_matrix[0][0] + 1)
                portal2_location = (portal_grid_matrix[1][1] + 1,
                    portal_grid_matrix[1][0] + 1)
                    
                arena_matrix[portal1_location[0]][portal1_location[1]] = 2
                arena_matrix[portal2_location[0]][portal2_location[1]] = 2
    
                
                p_move_matrix = []
                for i in range(len(arena_matrix)):
                    p_move_matrix.append([])
                    for j in range(len(arena_matrix[i])):
                        p_move_matrix[-1].append(0)
                i,j = pacman_location
                p_move_matrix[i][j] = 1
                
                
                def make_move_with_portal(m):
                    p = False # tracks if portal was moved into
                    for i in range(len(p_move_matrix)): # For each row
                        for j in range(len(p_move_matrix[i])): # For each column
                            if p_move_matrix[i][j] == m:
                                if i>0 and p_move_matrix[i-1][j] == 0 and arena_matrix[i-1][j] != 1:
                                    p_move_matrix[i-1][j] = m + 1
                                    if arena_matrix[i-1][j] == 2:
                                        p = True
                                        coords = (i -1, j)
                                if j>0 and p_move_matrix[i][j-1] == 0 and arena_matrix[i][j-1] != 1:
                                    p_move_matrix[i][j-1] = m + 1
                                    if arena_matrix[i][j-1] == 2:
                                        p = True
                                        coords = (i, j - 1)
                                if i<len(p_move_matrix)-1 and p_move_matrix[i+1][j] == 0 and arena_matrix[i+1][j] != 1:
                                    p_move_matrix[i+1][j] = m + 1
                                    if arena_matrix[i+1][j] == 2:
                                        p = True
                                        coords = (i + 1, j)
                                if j<len(p_move_matrix[i])-1 and p_move_matrix[i][j+1] == 0 and arena_matrix[i][j+1] != 1:
                                    p_move_matrix[i][j+1] = m + 1
                                    if arena_matrix[i][j+1] == 2:
                                        p = True
                                        coords = (i, j + 1)
                                # Change portal values (if needed)        
                                if p:
                                    if coords == portal1_location:
                                        p_move_matrix[portal2_location[0]][portal2_location[1]] = m 
                                    elif coords == portal2_location:
                                        p_move_matrix[portal1_location[0]][portal1_location[1]] = m 
                    return p # True or false if portal was accessed
                
                # The m variable below the "move" count that we are currently on. It
                # incrementally cycles through the make_move() function above until the 
                # banana goal location value is changed from zero to another value.
                # Also, there's a safety counter that will break the loop if 
                # there's no solution.
                m = 1
                safety_counter = self.vertical_moves_in_arena * self.horizontal_moves_in_arena
                while p_move_matrix[banana_location[0]][banana_location[1]] == 0:
                    portal_accessed = make_move_with_portal(m)
                    if not portal_accessed:
                        m += 1
                    safety_counter -= 1
                    if safety_counter < 1:
                        print("ERROR: Actually no solution to maze")
                        break
                    
                # Then print...
                if safety_counter > 0:    
                    print(f"Par (n = {m-1}) solution as matrix:")
                    print_m(p_move_matrix)
                
                # Determine ideal strategy (non-portal vs. portal)
                if m < k: 
                    self.ideal_strategy = "portal"
                else:
                    self.ideal_strategy = "nonportal"

            # Now that we've found all the potential paths from the banana to the pacman,
            # we could potentially  isolate the shortest path form the banana to 
            # the pacman. This isn't required of the current experiment (so is 
            # commented out), but may be useful in the future! Note that the current 
            # form isn't compatible with the portals (just a navigation maze), so it
            # may need to be tweaked to work correctly. We can do this by working backwards
            # from the banana goal: similarly to the make_move() function, we first look 
            # around the end point for a value equal to the endpoint value minus one (in 
            # the example matrix, it would be the "6" value north of (3, 4) at (2, 4).
            # This will repeat until the k variable reaches the pacman start location. 
            # A visual representaiton of this shortest path is below:
            # 
            #       0  0  0  0  0  0  0  
            #       0  0  3  4  5  0  0  
            #       0  0  2  0  6  0  0  
            #       0  0  1  0  7  0  0  
            #       0  0  0  0  0  0  0  
            #
            # As each step of the shortest path is found, the respective coordinate is
            # appended to the "the_path" list. Additionally, a number of moves counter
            # "n_moves" will incrementally increase by 1. After this while loop ends, the 
            # "the_path" list holds each of the points in the path and the n_moves 
            # counter will equal the par for that arena setup. 
            # i, j = banana_location
            # k = move_matrix[i][j]
            # the_path = [(i,j)]
            # n_moves = 0
            # while k > 1:
            #  if i > 0 and move_matrix[i - 1][j] == k-1:
            #    i, j = i-1, j
            #    the_path.append((i, j))
            #    n_moves += 1
            #    k-=1
            #  elif j > 0 and move_matrix[i][j - 1] == k-1:
            #    i, j = i, j-1
            #    the_path.append((i, j))
            #    n_moves += 1
            #   k-=1
            #  elif i < len(move_matrix) - 1 and move_matrix[i + 1][j] == k-1:
            #    i, j = i+1, j
            #    the_path.append((i, j))
            #    n_moves += 1
            #    k-=1
            #  elif j < len(move_matrix[i]) - 1 and move_matrix[i][j + 1] == k-1:
            #    i, j = i, j+1
            #    the_path.append((i, j))
            #    n_moves += 1
            #   k -= 1
            
            # Finally, return the minimum number of moves required in the
            # portal algorithm
            return m-1
            
        ## Now set up objects in the arena:
        
        # 1) BARRIERS
        self.barrier_dimension_matrix = [] # First clear existing matrix...
        barrier_grid_coords = [] # And grid matrix
        # In 5.a, 5.b (single), 6.a, and 6.b, there is at least one barrier
        # built somewhere in the "middle" of the arena (e.g., x location
        # between 2 and 5) and in any y location. First, the initial barrier
        # is built...
        if self.training_phase in ["5.a", "5.b", "5.c", "5.d", "5 TEST"]:
            barrier_grid_coords.append([randint(1, self.horizontal_moves_in_arena - 1),
                                        randint(0, self.vertical_moves_in_arena)])
            width_multiplier = 0.15 # This value very slightly shrinks the width of barriers to aesthetically fit 
        # Next, in 5.c and 5.d, there will be an additional barrier vertically
        # aligned with the first barrier. It is either above or below (but
        # the x-grid location) the first barrier. In the 5 TEST phase, there 
        # is a 50:50 chance of a second barrier being built.
        if self.training_phase in ["5.c", "5.d"] or (self.training_phase == "5 TEST" and choice([True, False])):
            y_locations = list(range(0, self.vertical_moves_in_arena + 1)) # All possible vertical locations
            y_locations.remove(barrier_grid_coords[0][1]) # Remove the vertical location of the existing barrier
            barrier_grid_coords.append([barrier_grid_coords[0][0],
                                       choice(y_locations)]) # Add new barrier to list
        elif self.training_phase == "6.c":
            xcord = randint(1, self.horizontal_moves_in_arena - 1)
            for ycord in list(range(0, self.vertical_moves_in_arena + 1)):
                barrier_grid_coords.append([xcord, ycord])    
        # Next, if the training phase is 7 TEST then the barrier should be completely
        # blocking access to the banana
        elif self.training_phase in ["7 TEST"]:
            width_multiplier = 0.15 # This value very slightly shrinks the width of barriers to aesthetically fit 
            if self.trial_number <= len(self.insight_trial_dictionaries)*2:
                object_location_dict = self.insight_trial_dictionaries[0]
                self.insight_trial_dictionaries.remove(object_location_dict)
                self.insight_trial_dictionaries.append(object_location_dict)
            else:
                object_location_dict = choice(self.insight_trial_dictionaries)
            
            self.insight_trial_type = object_location_dict["Trial Type"]
            
            barrier_grid_coords = object_location_dict["Barrier Grid Matrix"]
        
        elif self.training_phase in ["6"]:
            for r in list(range(0, self.vertical_moves_in_arena + 1)):
                for c in list(range(0, self.horizontal_moves_in_arena + 1)):
                    barrier_grid_coords.append([c, r])
            width_multiplier = 0.25 # This value very slightly widens the width of barriers to aesthetically fit
        
        ## 2) Portals
        self.portal_grid_locations = None # For phases w/o portals
        if self.training_phase in ["6.a", "6.b", "6.c", "6", "7 TEST"]:
            # First, we determine every border location that a portal could
            # potentially be built. We are only using the l/r/bottom borders
            # (because the pigeons could not reach the top of the screen), and
            # because our arena is 3 x 6 moves, we have a matrix of 12 possible
            # xy coordinates (3*2 + 6), as follows:
            #               [[-1,0],[-1,1], [-1,2],
            #         [0,3],[1,3], [2,3], [3,3], [4,3], [5,3],
            #                 [6,0],[6,1], [6,2]]
            # We can create this matrix by:
            possible_portal_location_matrix = []
            for y in list(range(0,self.vertical_moves_in_arena)):
                possible_portal_location_matrix.append([-1, y])
                possible_portal_location_matrix.append([self.horizontal_moves_in_arena +1,y])
            for x in list(range(0, self.horizontal_moves_in_arena)):
                if self.training_phase == "6.c":
                    if x != barrier_grid_coords[0][0]:
                        possible_portal_location_matrix.append([x, self.vertical_moves_in_arena + 1])
                elif self.training_phase == "6":
                    if x in [0, self.horizontal_moves_in_arena]:
                        possible_portal_location_matrix.append([x, self.vertical_moves_in_arena + 1])
                else:
                    possible_portal_location_matrix.append([x, self.vertical_moves_in_arena + 1])
            # After the list is created/trimmed, we can choose the locations
            # the two portals starting with the first:
            choice1 = choice(possible_portal_location_matrix) # First portal can be anywhere
            possible_portal_location_matrix.remove(choice1) # Remove from choices
            # Next up, we have to make sure that the portals fall on either 
            # side of the barriers (if there are barriers)
            second_portal_found = False
            # For 6.a, portals shouldn't be adjacent...
            if self.training_phase in ["6.a", "6.b"]: # No barriers
                if self.training_phase == "6.a":
                    min_portal_dist = 1
                elif self.training_phase == "6.b":
                    min_portal_dist = 2
                while not second_portal_found:
                    choice2 = choice(possible_portal_location_matrix) # First portal can be anywhere
                    if (choice2[0] > choice1[0] + min_portal_dist) or (choice2[0] < choice1[0] - min_portal_dist) or (choice2[1] > choice1[1] + min_portal_dist) or (choice2[1] < choice1[1] - min_portal_dist):
                        second_portal_found = True 
                self.portal_grid_locations = [choice1, choice2]# This should always be two elements long
                
            elif self.training_phase in ["6.c"]: # When barriers exist, should be on either side
                while not second_portal_found:
                    choice2 = choice(possible_portal_location_matrix)
                    if (choice1[0] < barrier_grid_coords[0][0] and choice2[0] > barrier_grid_coords[0][0]) or (choice1[0] > barrier_grid_coords[0][0] and choice2[0] < barrier_grid_coords[0][0]):
                        second_portal_found = True    
                        self.portal_grid_locations = [choice1, choice2]# This should always be two elements long
                
            
            elif self.training_phase == "6":
                while not second_portal_found:
                    choice2 = choice(possible_portal_location_matrix) # First portal can be anywhere
                    if choice2[0] != choice1[0]  and choice2[0] -1 != choice1[0] and choice2[0] +1 != choice1[0]:
                        second_portal_found = True 
                self.portal_grid_locations = [choice1, choice2]# This should always be two elements long
                
            elif self.training_phase == "7 TEST":
                self.portal_grid_locations = object_location_dict["Portal Grid Matrix"]
                
            
        ## 2) PACMAN
        if self.training_phase == "1.a":
            # If the training phase is 1.a, then the pacman should just be 
            # centered in the middle of the screen.
            pacman_grid_location = [2, 1]
        elif self.training_phase in ["2.a", "2.b"]:
            # If the training phase is 2.a or 2.b, the pacman is built in the
            # same location it was after moving in the prior trial. First trial
            # is in a random location. If it is not the first trial, it will
            # keep its previous value set in the "build_ovals" function
            if self.trial_number == 1:
                pacman_grid_location = rand_grid_location()
        # Next up are phases built in relation to barriers
        elif self.training_phase in ["5.a", "5.c"]: # Pacman is built LEFT of barrier(s)
            pacman_grid_location = [barrier_grid_coords[0][0] - 1,
                                    randint(0, self.vertical_moves_in_arena)]
        elif self.training_phase in ["5.b", "5.d"]: # Pacman is built RIGHT of barrier(s)
                pacman_grid_location = [barrier_grid_coords[0][0] + 1,
                                randint(0, self.vertical_moves_in_arena)]
        elif self.training_phase in ["5 TEST", "6.c"]:
            if choice([True, False]):
                pacman_LR = "Left" 
                pacman_grid_location = [randint(0, barrier_grid_coords[0][0]-1),
                                        randint(0, self.vertical_moves_in_arena)]
            else:
                pacman_LR = "Right" 
                pacman_grid_location = [randint(barrier_grid_coords[0][0]+1, self.horizontal_moves_in_arena),
                                        randint(0, self.vertical_moves_in_arena)]
        # For 6.a, the pacman should be in front of portal choice number one
        elif self.training_phase in ["6.a", "6"]:
            if self.portal_grid_locations[0][0] < 0: # Portal is on left barrier
                pacman_grid_location = [0, self.portal_grid_locations[0][1]]
                self.portal_direction = "west"
            elif self.portal_grid_locations[0][0] > self.horizontal_moves_in_arena: # Portal on right barrier
                pacman_grid_location = [self.horizontal_moves_in_arena,
                                        self.portal_grid_locations[0][1]]
                self.portal_direction = "east"
            elif self.portal_grid_locations[0][1] > self.vertical_moves_in_arena: # horizontal portal
                pacman_grid_location = [self.portal_grid_locations[0][0],
                        self.vertical_moves_in_arena]
                self.portal_direction = "south"
            if self.training_phase in ["6"]:
                barrier_grid_coords.remove(pacman_grid_location)
                barriers_to_remove = [[pacman_grid_location[0]+1, pacman_grid_location[1]],
                                      [pacman_grid_location[0]-1, pacman_grid_location[1]],
                                      [pacman_grid_location[0], pacman_grid_location[1]-1],
                                      [pacman_grid_location[0], pacman_grid_location[1]+1],
                                      [self.portal_grid_locations[1][0] +1, self.portal_grid_locations[1][1]],
                                      [self.portal_grid_locations[1][0] -1, self.portal_grid_locations[1][1]],
                                      [self.portal_grid_locations[1][0], self.portal_grid_locations[1][1] - 1],
                                      [self.portal_grid_locations[1][0], self.portal_grid_locations[1][1] + 1]
                                      ]
                possible_green_dot_grid_locations = []
                for b in barriers_to_remove:
                    if b in barrier_grid_coords:
                        barrier_grid_coords.remove(b)
                        possible_green_dot_grid_locations.append(b)
                
        elif self.training_phase == "7 TEST":
            pacman_grid_location = object_location_dict["Pacman Grid Location"]
       # These base coordinates are randomly determined (for 6.b)
        else: 
            pacman_grid_location = rand_grid_location()
            
        self.pacman_coords = self.convert_grid_to_coordinate(*pacman_grid_location)
         

        # 3) BANANA
        # Then, build the objects that aren't included in every training 
        # phase (e.g., the banana). That includes phases 3.a through 4.a (4-8).
        # This "if" statement asks if the banana is present in training. 
        if self.training_phase not in ["1.a", "1.b", "2.a", "2.b", "6.a", "6.b", "6.c"]:
            # For training phases without a barrier:
            if self.training_phase in ["1.a", "1.b", "2.a", "2.b",
                                       "3.a", "3.b", "3.c", "3.d", "4.a",
                                       "3.b TEST", "3.d TEST", "4.a TEST"]:
                # This function then determines the goal (banana) coordinates for
                # this trial and phase number
                banana_grid_location = banana_location_from_pacman()
            elif self.training_phase in ["4.b"]:
                # In 4.b, banana is in a random place (that is not the pacman)
                banana_loc_determined = False
                while not banana_loc_determined:
                    banana_grid_location = rand_grid_location()
                    self.goal_coords = self.convert_grid_to_coordinate(*banana_grid_location)
                    if self.goal_coords != self.pacman_coords:
                        banana_loc_determined = True
                
            # Next up are phases when the banana is built in relation to barriers
            elif self.training_phase in ["5.a", "5.c"]: # Banana is built RIGHT of barrier(s)
                banana_grid_location = [barrier_grid_coords[0][0] + 1,
                                        randint(0, self.vertical_moves_in_arena)]
            elif self.training_phase in ["5.b", "5.d"]: # Banana is built LEFT of barrier(s)
                    banana_grid_location = [barrier_grid_coords[0][0] - 1,
                                    randint(0, self.vertical_moves_in_arena)]
            elif self.training_phase in ["5 TEST"]: # Banana can be L or R, depending on pacman
                if pacman_LR == "Left": # Build banana right
                    banana_grid_location = [randint(barrier_grid_coords[0][0]+1, self.horizontal_moves_in_arena),
                        randint(0, self.vertical_moves_in_arena)]
                else: # Left
                    banana_grid_location = [randint(0, barrier_grid_coords[0][0]-1),
                        randint(0, self.vertical_moves_in_arena)]
             # Or if the banana should be in front of portal two       
            # elif self.training_phase in ["6.a"]:
            #     if self.portal_grid_locations[1][0] < 0: # Portal is on left barrier
            #         banana_grid_location = [0, self.portal_grid_locations[1][1]]
            #     elif self.portal_grid_locations[1][0] > self.horizontal_moves_in_arena: # Portal on right barrier
            #         banana_grid_location = [self.horizontal_moves_in_arena,
            #                                 self.portal_grid_locations[1][1]]
            #     elif self.portal_grid_locations[1][1] > self.vertical_moves_in_arena: # horizontal portal
            #         banana_grid_location = [self.portal_grid_locations[1][0],
            #                                 self.vertical_moves_in_arena]
            elif self.training_phase == "7 TEST":
                banana_grid_location = object_location_dict["Banana Grid Location"]
                    
        # 4) GREEN DOT
        if self.training_phase in ["6"]:       
            green_dot_grid_location = choice(possible_green_dot_grid_locations)
            
        # After all the functions within the "setup_trail()" function are 
        # declared, make sure canvas is cleaned and trial time is reset
        self.mastercanvas.delete("all") 
        print("*" * 75) # spacer
        self.local_trial_timer = datetime.now()
        
        
        ## Then, the "base" widgets on top of that canvas are created (including the 
        # background, pacman, banana, and any barriers/borders that are previously
        # stated). Note that the order in which widgets are created is correlated with
        # with the order (or "layer") that the object is created onscreen.
        
        # The background object is built first, and is tagged with a function
        # that records a X/Y peck data point to the cumuilative dataframe.
        self.background = self.mastercanvas.create_rectangle(0, 0,
                                                             self.mainscreen_width,
                                                             self.mainscreen_height,
                                      fill = "black",
                                      outline = "white",
                                      width = 10,
                                      tag = "background_tag")
        # This function ties the background_tag tag to the write_event_data func 
        self.mastercanvas.tag_bind("background_tag",
                      "<Button-1>",
                      lambda event,
                      event_type = "BackgroundPeck":
                      self.write_event_data(event_type,event.x,event.y))
            
        # Then the four borders are built on top of the background (North,
        # East, South, and West).
        for border_dim in self.border_dimensions_matrix:
            self.mastercanvas.create_rectangle(border_dim,
                                      fill = "white",
                                      outline = "white")

        # After the grid locations are determined, everything is converted to
        # coordinate units in order to be built. Here, we blow up the barrier 
        # size to 2x the size of the pacman or (more importantly) half the 
        # size of a move plus the pacman size. Additionally, we shrink the 
        # width (x values) very slightly to account for aesthetic overlap with
        # adjacent portals.
        for grid_coord in barrier_grid_coords:
            self.barrier_dimension_matrix.append(self.convert_grid_to_coordinate(*grid_coord))
        for barrier_dim in self.barrier_dimension_matrix:
            self.mastercanvas.create_rectangle([barrier_dim[0] - int(self.move_distance * width_multiplier),
                                                barrier_dim[1] - int(self.move_distance * 0.25),
                                                barrier_dim[2] + int(self.move_distance * width_multiplier),
                                                barrier_dim[3] + int(self.move_distance * 0.25)],
                                               fill = "white",
                                               outline = "white")
            
        if self.training_phase in ["6.a", "6.b", "6.c", "6", "7 TEST"]:
            # After the grid locations of both portals are determined, we
            # need to convert the grid units to pixel units to actually 
            # build the portals on the canvas.
            self.portal_dims = [] # This is the actual coordinates of the portals
            for grid_list in self.portal_grid_locations:
                self.portal_dims.append(self.portal_grid_to_coordinate(*grid_list)) # Fills in the portal_dims list
            # Finally, after we've determined the grid locations and calcualted the
            # onscreen coordinates, we build the two-part portals:
            for dim in self.portal_dims:
                # Black square tunnel
                self.mastercanvas.create_rectangle(dim[0],
                                                   fill = "black",
                                                   outline = "black") 
                # Oval at the end of the tunnel
                self.mastercanvas.create_oval(dim[1],
                                              outline = "green",
                                              tag = "portal",
                                              fill = "#03fceb")
        
        # The pacman background is just a blank square around the pacman to 
        # track pecks and act as a reference point for the pacman object.
        self.pacman_bkgrd = self.mastercanvas.create_rectangle(self.pacman_coords,
                                      fill = "black",
                                      outline = "black",
                                      tag = "pacman_tag")
        
        # This is the actual pacman
        self.pacman = self.mastercanvas.create_arc(self.pacman_coords,
                                 fill= self.pacman_color,
                                 outline = "white",
                                 style=PIESLICE,
                                 start=45,
                                 extent=270,
                                 tag = "pacman_tag")
        # Bind tag to pacman function
        self.mastercanvas.tag_bind("pacman_tag",
                      "<Button-1>",
                      self.pacman_pressed)
        
        # Banana
        if self.training_phase not in ["1.a", "1.b", "2.a", "2.b", "6.a", "6.b", "6.c", "6"]:     
            # After the banana grid location is set, we can calculate the actual 
            # coordinates needed to build the banana
            self.goal_coords = self.convert_grid_to_coordinate(*banana_grid_location)
            
            # After the goal coordinates are determined, we can then build the
            # banana object
            trial_banana_dims = calculate_banana_dims(*self.goal_coords[0:2],
                                                      self.base_banana_dimensions)
            trial_banana_brown_dims = calculate_banana_dims(*self.goal_coords[0:2],
                                                      self.base_banana_brown_dimensions)
            
            self.banana_goal = self.mastercanvas.create_rectangle(self.goal_coords,
                                          fill = "black",
                                          outline = "black")

            self.banana = self.mastercanvas.create_polygon(trial_banana_dims,
                                                 fill = "yellow",
                                                 outline = "white",
                                                 tag = "banana_func")
        
            self.banana_brown = self.mastercanvas.create_polygon(trial_banana_brown_dims,
                                                 fill = "brown",
                                                 outline = "black",
                                                 tag = "banana_func")

            self.mastercanvas.tag_bind("banana_func",
                          "<Button-1>",
                          lambda event,
                          event_type = "BananaPeck":
                          self.write_event_data(event_type,event.x,event.y))
                
                                
            # After the pacman and banana are built, we can find the number of 
            # moves required to get reach the banana goal, or what we're calling
            # the "par" for a trial. Note that this only applies to conditions
            # with a banana.
            self.trial_par = get_trial_par(pacman_grid_location,
                                           banana_grid_location,
                                           barrier_grid_coords,
                                           self.portal_grid_locations)
            
        elif self.training_phase in ["6"]:    
            self.green_dot_coords = self.convert_grid_to_coordinate(*green_dot_grid_location)
            gdot_pixel_shrink_factor = 15
            self.green_dot_bkgrd = self.mastercanvas.create_oval(self.green_dot_coords,
                                          fill = "black",
                                          outline = "black",
                                          tag = "green_dot_tag")
            self.green_dot = self.mastercanvas.create_oval([self.green_dot_coords[0] + gdot_pixel_shrink_factor,
                                                                 self.green_dot_coords[1] + gdot_pixel_shrink_factor,
                                                                 self.green_dot_coords[2] - gdot_pixel_shrink_factor,
                                                                 self.green_dot_coords[3] - gdot_pixel_shrink_factor],
                                          fill = "green",
                                          outline = "black",
                                          tag = "green_dot_tag")
            # Bind tag to pacman function
            self.mastercanvas.tag_bind("green_dot_tag",
                          "<Button-1>",
                          lambda event,
                          event_type = "GreenDotPeck":
                          self.write_event_data(event_type,event.x,event.y))
                
            
        
        
        # Lastly, we need to bring the pacman to the front (above the banana)
        self.mastercanvas.tag_raise(self.pacman)

    
# After the base widgets are initially created, the necessary functions are 
# declared below. Note that the order functions are created means nothing.

    def begin_reinforcement (self):
        # Begin_reinforcement is called only when behavior in a trial should
        # be reinforced: either a peck on the pacman in early training or when 
        # the dimensions of the pacman EXACTLY match the dimensions of the
        # banana goal. Note that, except in test session tyes where "incorrect" 
        # choices are punished, this function is always called at the very 
        # end of every trial.
        self.mastercanvas.delete("all") # Delete all objects
        self.write_event_data("reinforcement", None, None)
        self.reinforcers_provided += 1 # A reinforcer is provided
        if operant_box_version:
            self.Hopper.change_hopper_state("On")
        else:
            self.mastercanvas.create_text(350,300,
                                          fill="red",
                                          font="Times 20 italic bold",
                                          text = ("Reinforcer for %ss" % int(self.reinforcer_interval/1000)))
        self.root.after(self.reinforcer_interval, self.ITI)
    
    def ITI(self):
        # The ITI not only functions as an intertrial interval delay, but also 
        # is where the trial to trial variables are reset prior to the next trial
        # because it is ALWAYS called between trials, regardless of non/reinforced 
        # behavior  
        if operant_box_version:
            self.Hopper.change_hopper_state("Off")
        else:
            self.mastercanvas.delete("all") # Delete all objects
            self.mastercanvas.create_text(350,300,
                                     fill="red",
                                     font="Times 20 italic bold",
                                     text=f"Trial {self.trial_number}: ITI for {int(self.ITI_duration/1000)}s")
        self.trial_number += 1
        self.current_trial_moves = 0
        self.portal_accessed = False
        self.ovals_onscreen = False
        if self.reinforcers_provided >= self.max_reinforcers_per_session:
            # This exits the GUI screen and writes all the session data
            # that was collected to a final .csv document
            self.exit_program("event")

        else:
            self.write_data_csv(False) # Update .csv data file with that trial's data
            self.root.after(self.ITI_duration, self.set_up_trial)

    def TO_period(self):
        # The timeout contingency is called only within "test" phases 3.b (5), 
        # 3.d,(7), and 4.a (8) in which "wrong" moves are allowed. In 3.b, the 
        # pacman is only one step away from the banana, so if the pacman doesn't
        # match the banana coords after one move, they are punished with a TO. In 
        # 3.d and 4.a, they have two opportunitites to reach the banana (even if
        # then first is incorrect).
        self.mastercanvas.delete("all")
        self.write_event_data("TimeOutPeriod", None, None)
        if not operant_box_version:
            self.mastercanvas.create_text(350,300,
                             fill="red",
                             font="Times 20 italic bold",
                             text = ("INCORRECT CHOICE(S) \nTimeout for %ss") %
                             int(self.TO_duration/1000))
        self.root.after(self.TO_duration, self.ITI)
        
            
    def pacman_pressed(self,event):
        # This function is called whenever the pacman object is pecked. If 
        # an early training phase, it may immediately lead to reinforcement.
        # Else, if it at the beginning of a trial, the peck will cause oval
        # cursors to appear around the pacman. If ovals have already appeared
        # (tracked by the T/F self.ovals_onscreen variable), a peck on the 
        # pacman does nothing but write a datapoint on the df.
        self.write_event_data("PacmanPecked", event.x, event.y)
        if self.training_phase in ["1.a","1.b"]: # If pacman peck is reinforced
            self.begin_reinforcement()
        else: # Cursors are involved
            if not self.ovals_onscreen:
                self.ovals_onscreen = True
                self.build_oval()
            

    def build_oval (self):
        # Build_oval's main function is to build the respective ovals around
        # the pacman after it is pecked for the first time or after the pacman 
        # has moved. It calculates which ovals should be built around the
        # pacman in its current location (depending on proximity of barriers
        # or borders). The build_oval function also contains all the movement
        # and animation functions that are tied to each of the ovals.
        
        def get_oval_dim (oval_type, x1, y1, x2, y2):
            # This function returns relative dimensions of an oval based on the
            # passed dimensions (of the pacman). It should be passed the oval
            # type as a string and four coordinates of the pacman *[x1, y1, x2,
            # y2] and returns that respective oval's [x1,y1,x2,y2] dimensions.
            # Note that this will still work regardless of the location of the
            # pacman and size of pacman, and the ratio size of each oval can be 
            # manipulted via the oval_width variable.
            if oval_type == "south_oval_pacman":
                return [x1 + (x2 - x1)/2 - self.oval_width/2,
                         y2 + self.oval_pacman_gap,
                         x1 + (x2- x1)/2 + self.oval_width/2,
                         y2+self.oval_pacman_gap+self.oval_width]
            elif oval_type == "east_oval_pacman":
                return[x2 + self.oval_pacman_gap,
                        y1 + (y2 - y1)/2 - self.oval_width/2,
                        x2 + self.oval_pacman_gap + self.oval_width,
                        y1 + (y2-y1)/2 + self.oval_width/2]
            elif oval_type == "north_oval_pacman":
                return [x1 + (x2-x1)/2 - self.oval_width/2,
                         y1 - self.oval_pacman_gap - self.oval_width,
                         x1 + (x2-x1)/2 + self.oval_width/2,
                         y1 - self.oval_pacman_gap]
            elif oval_type == "west_oval_pacman":
                return [x1 - self.oval_pacman_gap - self.oval_width,
                        y1 + (y2-y1)/2 - self.oval_width/2,
                        x1 - self.oval_pacman_gap,
                        y1 + (y2 - y1)/2 + self.oval_width/2]
 
        def convert_pacman_to_x_y(tag):
            # This function converts the pacman tag string to the projected
            # x and y coordinate movement that each pacman oval will have.
            if tag == "north_oval_pacman":
                return 0, -self.move_distance
            elif tag == "east_oval_pacman":
                return self.move_distance, 0
            elif tag == "south_oval_pacman":
                return 0, self.move_distance
            elif tag == "west_oval_pacman":
                return -self.move_distance, 0
        
        def check_for_overlap(x1, y1, x2, y2, move_x, move_y):
            # The check_for_overlap function is passed six arguments:
            #       1-4) the current dimensions of the existing curosor object:
            #               x1, y1, x2, y2
            #       5-6) any movement to the existing x or y paramters
            # Then, the function creates a new set of "ghost" dimensions at the 
            # projected space, given the move alterations.
            x1 = int(x1 + move_x)
            x2 = int(x2 + move_x)
            y1 = int(y1 + move_y)
            y2 = int(y2 + move_y)
            # The overlap boolean (below) is a True/False value that tracks if
            # there will be ANY overlap between the projected curosr coordinates
            # and any barriers or borders, using the nested "FOR" loops below:
            overlap = False
            # First, before we look for overlap with walls or barriers, we
            # should check if the projected location is bordering a portal
            # for phases with portals
            if self.training_phase in ["6.a", "6.b", "6.c", "6", "7 TEST"]:
                for x in [x1, x2]:
                    for portal in self.portal_dims:
                        if x >= portal[0][0] and x <= portal[0][2]:
                            for y in [y1, y2]:
                                if y >= portal[0][1] and y <= portal[0][3]:
                                    return False #overlap w/ portal
            # "Combined matrix" combines any existing barrier coordinate lists with
            # the border dimensions (in order to treat borders the same way as 
            # barriers)
            combined_matrix  = []
            for dims in self.border_dimensions_matrix + self.barrier_dimension_matrix:
                combined_matrix.append(dims)
            # Next, this function checks for overlap between the curosr and borders/
            # barrier x coordinates and y coordintes
            for barrier_dimension_vector in combined_matrix:
                for x in [x1, x2]:
                    if x >= barrier_dimension_vector[0] and x <= barrier_dimension_vector[2]:
                        for y in [y1, y2]:
                            if y >= barrier_dimension_vector[1] and y <= barrier_dimension_vector[3]:
                                overlap = True 
                                break # If overlap exists, the for loop is broken
            return overlap # This returns "True" if there is overlap and "False" if not
        
        
        def animate_pacman(counter, location_x, location_y):
            # First things first, quickly "raise" all the portal outlines
            # just in case the pacman needs to pass through them
            self.mastercanvas.tag_raise("portal")
            # This function creates the animated movement of the pacman. The 
            # counter loop continues to loop while the distance between pacman
            # and the estimated distance of the movement (the counter) is
            # larger than 0. When it reaches zero, the location is reached and
            # the loop concludes.
            if counter > 0: 
                if location_x == 0: # move up/down
                    self.mastercanvas.move(self.pacman,
                                           0,
                                           self.movement_resolution * int(copysign(1, location_y)))
                    self.mastercanvas.move(self.pacman_bkgrd,
                                           0,
                                           self.movement_resolution * int(copysign(1, location_y)))
                elif location_y == 0: # move left/right
                    self.mastercanvas.move(self.pacman,
                                           self.movement_resolution * int(copysign(1, location_x)), 0)
                    self.mastercanvas.move(self.pacman_bkgrd,
                                           self.movement_resolution * int(copysign(1, location_x)), 0)
                counter -= 1 #As the pacman moves, the counter is reduced by one in each movement
                             # indicating that the pacman is getting near to the estimated position of the hole movement
                self.root.after(self.ms_per_pixel_speed,
                                lambda: animate_pacman(counter, location_x, location_y))
                
            else: # the moving pacman has arrived at its stopping location
                portal_exited = False
                # First up, we should check if the pacman moved into a portal 
                # (for portal phases)
                if not self.training_phase in ["6.a", "6.b", "6.c", "6", "7 TEST"]:
                    portal_exited = True # No portal to exit
                else: # Phases with a portal...
                    pac_coords = self.mastercanvas.coords(self.pacman)
                    overlapping_portal = None
                    for portal in self.portal_dims:
                        for x in [pac_coords[0], pac_coords[2]]:
                                if x >= portal[0][0] and x <= portal[0][2]:
                                    for y in [pac_coords[1], pac_coords[3]]:
                                        if y >= portal[0][1] and y <= portal[0][3]:
                                            overlapping_portal = portal[0]
                    # If the pacman is not inside a portal...
                    if overlapping_portal == None:
                        portal_exited = True
                    # Else if the pacman IS in a portal, then find the new portal
                    # grid location that the pacman should be transported to...
                    else:
                        # But first we should write it to the data sheet
                        self.write_event_data("PortalActivated", None, None)
                        new_portal_grid_location = None
                        self.portal_accessed = True
                        for grid_portal in self.portal_grid_locations:
                            if self.portal_grid_to_coordinate(*grid_portal)[0] != overlapping_portal:
                                new_portal_grid_location = grid_portal
                        # With the new grid location discovered, we can move the
                        # existing pacman to the new location inside the other portal
                        new_pacman_coords = self.convert_grid_to_coordinate(*new_portal_grid_location)
                        self.mastercanvas.coords(self.pacman, *new_pacman_coords)
                        self.mastercanvas.coords(self.pacman_bkgrd, *new_pacman_coords)
                        # Finally, once the pacman is moved to the other portal 
                        # location, it should be moved back into the arena. We
                        # need to find WHERE that is depending on the location
                        # of the portal...
                        if new_portal_grid_location[0] < 0: # Vertical portal on left moving right
                            x, y = convert_pacman_to_x_y("east_oval_pacman")
                        elif new_portal_grid_location[0] > self.horizontal_moves_in_arena:
                            x, y = convert_pacman_to_x_y("west_oval_pacman")
                        elif new_portal_grid_location[1] > self.vertical_moves_in_arena:
                            x, y = convert_pacman_to_x_y("north_oval_pacman")
                        # Once the new destination is determined, we again pass
                        # this info back to this same "animate pacman" function
                        animate_pacman(abs(x + y)/self.movement_resolution,
                           x,
                           y)
                # Finally, if the destination has been reached AND that
                # destination is not inside of a portal...   
                if portal_exited:                                  
                    self.build_oval() #By the end of the pacman's movement, the ovals are created again
                
        def move (event, passed_tag, passed_x, passed_y):
            # Once built, each of the ovals is bound to this move functions
            # with different tags and passed_x/y values. This is the function 
            # that is called when an oval is pressed.
            self.current_trial_moves += 1 # Add a move to the trial movement counter
            self.write_event_data(passed_tag, event.x, event.y)
            # First, delete all the ovals from the pacman (before moving)
            for t in self.oval_tags:
                self.mastercanvas.delete(t)
            # Then unbind the keys...
            for k in self.move_keys:
                self.root.unbind(k)
            # Next, move the pacman
            animate_pacman(abs(passed_x + passed_y)/self.movement_resolution,
                           passed_x,
                           passed_y)
                                        
    # After the functions are declared, then the code begins...
        # First, update the pacman_coords variable. If the pacman is deleted
        # off the screen between trials, the pacman_coords variable will
        # track the previous pacman's coordinates.
        self.pacman_coords = self.mastercanvas.coords(self.pacman)
        # Second, ALWAYS check if pacman has reached banana
        if self.mastercanvas.coords(self.pacman) ==  self.goal_coords:
            self.write_event_data("BananaReached", None, None)
            self.mastercanvas.delete("pacman_tag")
            self.mastercanvas.delete("banana_func")
            self.mastercanvas.create_oval(self.goal_coords,
                                     fill = self.pacman_color,
                                     outline= "white")
            self.root.after(750, self.begin_reinforcement)
        # Third, if the training phase is 2.a and 2.b (in which a peck on the
        # pacman followed by a peck on the cursor is reinforced), then the 
        # ovals are NOT built after the pacman is moved and reinforced .75s
        # after the pacman reaches its location
        elif self.training_phase in ["2.a", "2.b"] and self.current_trial_moves == 1:
            self.root.after(750, self.begin_reinforcement)
        # Fourth, check if the trial par has been reached for test session 
        # types 3.b, 3.d, and 4.a. If the two values are equal, then the 
        # trial ends and results in a timeout after a brief (1s) pause with
        # no ovals onscreen. self.pacman_coords is saved for the next session
        elif self.training_phase in ["3.b", "3.d", "4.a"] and self.current_trial_moves == self.trial_par:
            self.root.after(1000, self.TO_period)
        # Fifth, in phases where usage of the portal is reinforced, check to see
        # if portal was acessed
        elif self.training_phase in ["6.a", "6.b", "6.c"] and self.portal_accessed:
                self.root.after(750, self.begin_reinforcement)
        elif self.training_phase in ["6"] and self.pacman_coords == self.green_dot_coords:
                self.write_event_data("GreenDotReached", None, None)
                self.root.after(500, self.begin_reinforcement)
        # If neither of these are true, then we continue to build ovals 
        # around the pacman (e.g., start the next opportunity to move)
        else:
            #if not self.ovals_onscreen or rebuild:
            tags_of_ovals_to_build = []
            for tag in self.oval_tags:
                # First, gather the ovals that should be built (e.g., not
                # the ovals that overlap with the borders or barriers)
                current_pacman_coords = self.mastercanvas.coords(self.pacman)
                # And, get the projected pacman oval coordinates:
                projected_x, projected_y = convert_pacman_to_x_y(tag)
                # Second, check for potential overlap with that pacman oval:
                if not check_for_overlap(*current_pacman_coords,  projected_x, projected_y):
                    tags_of_ovals_to_build.append(tag)
                    
            if self.training_phase in ["2.a","3.a","3.c", "6.a"]:
                # For trials in which only one of these ovals should be built,
                # delete all the oval tags except the one pointing to the
                # banana (or the portal, for 6.a)
                correct_oval_tag_list = []
                if self.training_phase == "2.a": # random direction
                    correct_oval_tag_list.append(choice(tags_of_ovals_to_build))
                else: # If oval direction is dependent upon banana or portal...
                    if self.training_phase == "6.a":
                        correct_direction = self.portal_direction
                    else:
                        correct_direction = self.banana_direction
                    # Then select from the existing pool of four tags
                    for t in tags_of_ovals_to_build:
                        if correct_direction in t.split("_"):
                            correct_oval_tag_list.append(t)
                # Finally, reset the list of ovals to be built
                tags_of_ovals_to_build = correct_oval_tag_list
                
            for each_tag in tags_of_ovals_to_build:
                # Next, build either the non-overlapped ovals or the single
                # chosen oval for phases 3.a and 3.c
                oval_dims = get_oval_dim(each_tag, *current_pacman_coords)
                oval_outline_dims = [oval_dims[0]-(self.oval_pacman_gap - 6),
                       oval_dims[1]-(self.oval_pacman_gap -6),
                       oval_dims[2]+(self.oval_pacman_gap -6),
                       oval_dims[3]+(self.oval_pacman_gap -6)]
                oval_center_dims = [oval_dims[0]+(self.oval_width/2 - 4),
                       oval_dims[1]+(self.oval_width/2 - 4),
                       oval_dims[2]-(self.oval_width/2 - 4),
                       oval_dims[3]-(self.oval_width/2 - 4)]
                #Finally, create the pacman oval objects and tie the move function 
                # to each (but with a different input)
                self.mastercanvas.create_oval(oval_outline_dims,
                                         fill = "black",
                                         outline = "black",
                                         tag = each_tag)
                self.mastercanvas.create_oval(oval_dims,
                                         fill = "gray",
                                         outline = "gray",
                                         tag = each_tag)
                self.mastercanvas.create_oval(oval_center_dims,
                                         fill = "black",
                                         outline = "white",
                                         width = 2,
                                         tag = each_tag)  
                
                x, y = convert_pacman_to_x_y(each_tag)
                # CHANGE
                # we have to recreate variables here, as otherwise all ovals
                # will move like the last oval built
                self.mastercanvas.tag_bind(each_tag,
                                      "<Button-1>",
                                      lambda event,
                                      oval_tag = str(each_tag),
                                      proj_x = int(x),
                                      proj_y = int(y): 
                                          move(event, oval_tag, proj_x, proj_y))
                    
                self.root.bind(str(self.move_keys[self.oval_tags.index(each_tag)]),
                               lambda event,
                               oval_tag = str(each_tag),
                               proj_x = int(x),
                               proj_y = int(y):
                                   move(event, oval_tag, proj_x, proj_y))
                # self.mastercanvas.tag_lower(each_tag) # drop pacman to bottom
                
            self.ovals_onscreen = True
                
    ## These functions write session data

    def write_event_data (self, event_type, x, y):
        # The following function defines what type of data is suposed to be
        # writen in each cell of the previous empty matrix. Each time the 
        # function is called, a new list (or line in the final .csv) is added
        # to the matrix dataframe. All data entries should be identically
        # formatted via the variables below. This data format is created to be
        # compatible with R's "tidydata" format in order to make the data
        # pipeline from sessions --> R as seamless as possible. The first
        # series of equations calculate a transformed x and y values that
        # treat the center of the pacman as the center of the screen, such
        # that pecking variability around the pacman can consistent.
        try:
            local_pacman_center = [int(self.pacman_coords[2]-(self.pacman_size/2)),
                                   int(self.pacman_coords[3]-(self.pacman_size/2))]
        except AttributeError: # if pacman doesn't exist (before first trial)
            local_pacman_center = [None, None]
        if x != None:
            distance_from_center = [int(self.mainscreen_width/2 - local_pacman_center[0]),
                                    int(self.mainscreen_height/2 - local_pacman_center[1])]
            transformed_x = distance_from_center[0] + x 
            transformed_y = distance_from_center[1] + y
        else:
            x, y, transformed_x, transformed_y = "NA", "NA", "NA", "NA"
        time_stamp = str(datetime.now() - self.start_time) # time_stamp is the corresponding time when each event happens
        print(f"{event_type:>20} | x: {x: ^3} y: {y:^3} | {str(datetime.now() - self.start_time)}")
        ID = self.subject # Subject is the name of the pigeon
        self.session_data_matrix.append([time_stamp,
                                    event_type,
                                    x,
                                    y,
                                    transformed_x,
                                    transformed_y,
                                    local_pacman_center[0],
                                    local_pacman_center[1],
                                    self.trial_number,
                                    self.current_trial_moves,
                                    self.trial_par,
                                    datetime.now() - self.local_trial_timer, 
                                    ID,
                                    self.training_phase,
                                    date.today(),
                                    self.insight_trial_type])

    def write_data_csv(self, SessionEnded):
        if not self.record_data:
            return
        # The following function creates a .csv data document. It is either 
        # called after each trial during the ITI (SessionEnded ==False) or 
        # one the session finishes (SessionEnded). If the first time the 
        # function is called, it will produce a new .csv out of the
        # session_data_matrix variable, named after the subject, date, and
        # training phase. Consecutive iterations of the function will simply
        # write over the existing document.
        if SessionEnded:
            self.write_event_data("SessionEnds", None, None) # Writes end of session to df
        # Data recording is contingent on the RadioButton being selected...
        if self.record_data:
            try:
                myFile_loc = f"{self.data_folder_directory}/{self.subject}/P032a_data_{self.subject}_{self.start_time.strftime('%Y-%m-%d_%H.%M.%S')}_phase-{self.training_phase}.csv" # location of written .csv
                edit_MyFile = open(myFile_loc, 'w', newline = '')
            except FileNotFoundError:
                print("\nERROR: Data folder not found (during session.\n Data will be written to same folder as program instead\n")
                myFile_loc = f"{getcwd()}/P032a_data_{self.subject}_{self.start_time.strftime('%Y-%m-%d_%H.%M.%S')}_phase-{self.training_phase}.csv" # location of written .csv
                edit_MyFile = open(myFile_loc, 'w', newline = '')
            # Next, once the data file location is found and opened...
            with edit_MyFile as MyFile:
                w = writer(MyFile, quoting=QUOTE_MINIMAL)
                w.writerows(self.session_data_matrix) # Write all event/trial data        
        print("Data written")
        
    def exit_program(self, event):
        # This function is called either when the session ends naturally (e.g.,
        # session timer is reached or reinforcer timer is reached), or when
        # the keybound <escape> key is manually pressed. This should never be 
        # done, unless the session needs to be ended prematurely.
        if operant_box_version:
            if event != "event":
                print("Escape key pressed")
            self.Hopper.change_hopper_state("Off")
            if not self.cursor_visible:
            	self.change_cursor_state("event") # turn cursor back on, if applicable
        self.write_data_csv(True)
        self.root.after(10, self.root.destroy) # Give time for the .csv to be written
        print("\n You may now exit the terminal and operater windows now.")
        # Once the experimental sessions end, they should cycle over to the 
        # paint program for the remainder of the time the pigeons are in the
        # boxes.
        if operant_box_version:
            random_pigeon_paint.Paint(self.subject)

# %% Finally, this is the code that actually kick starts the whole process

cp = ExperimenterControlPanel()
