import sys,time,random,os,random

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def Intro():
    global bonnieai, chicaai, foxyai, freddyai
    slow_print_1("FNaF 1 in Python 3.4.3\n")
    slow_print_2("V1.0\n")
    time.sleep(0.5)
    slow_print_1("Adapted by Peakbasic\nOriginal Game by Scott Cawthon\n")
    time.sleep(2)
    move = input("Press enter to play, or 'edit ai' to edit ai values\n>>> ")
    if move.lower() == "edit ai":
        while True:
            try:
                bonnieai = int(input("Enter Bonnie's AI\n>>> "))
                chicaai = int(input("Enter Chica's AI\n>>> "))
                freddyai = int(input("Enter Freddy's's AI\n>>> "))
                foxyai = int(input("Enter Foxy's AI\n>>> "))
                break
            except ValueError:
                print("AI value must be an integer.\nAny integer above 20 will be set to 20\n")
    slow_print_2("\n - - - N I G H T   6 - - - ")
    GameState()

ldoor = False
rdoor = False
gotyou = False
alive = True
bonmercytimer = 0
chimercytimer = 0

# Night stuff
bonnieai = 15
chicaai = 17
foxyai = 7
freddyai = 9


night = 0
timer = 0
End_of_Night = False

#For freddy
fredinhall = False
action = ""
camera = ""
# List of cameras

ldoorpenalty = 50
rdoorpenalty = 50

cam_1a = ["Freddy", "Bonnie", "Chica"]
cam_1b = []
foxystage = 0 # Cam 1c - Pirates Cove
cam_2a = []
cam_2b = []
cam_3 = []
cam_4a = []
cam_4b = []
cam_5 = []
cam_6 = []
cam_7 = []
leftbspot = []
rightbspot = []

# Text stuff

def lb():
    print("\n")

def slow_print(text, speed):
    #Slightly slow speed.
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(float(speed))

def slow_print_1(text):
    #Slightly slow speed.
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

def slow_print_2(text):
    #Fast speed.
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)

def slow_print_3(text):
    #Slightly slow speed.
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)

def slow_print_4(text):
    #Fast speed.
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
        
# FNAF 1 uses a roll ai/20 to decide movement.

def AI(ai):
    roll = random.randint(1,20)
    return int(ai) > roll

# Bonnie's Movement Path:
# 1a, 1b, 5, 1c, 2a, 2b

# Anamatronic stuff
# Bonnie

def Bonnie_Cam_Mov():
    global leftbspot, ldoor, bonmercytimer
# Done in the opposite way to prevent bonnie
# skipping through the cameras in a single
# movement opportunity
    
    if "Bonnie" in leftbspot and not ldoor:
        global gotyou
        if bonmercytimer < 3:
            bonmercytimer += 1

        else:
            gotyou = True
            
    elif "Bonnie" in leftbspot and ldoor and not gotyou:      
        if random.randint(0,5) >= 2:
            leftbspot.remove("Bonnie")
            cam_1b.append("Bonnie")
            bonmercytimer = 0
            
        else:
            leftbspot.remove("Bonnie")
            cam_5.append("Bonnie")
            bonmercytimer = 0
            
    if "Bonnie" in cam_2b:
        cam_2b.remove("Bonnie")
        leftbspot.append("Bonnie")
        
    if "Bonnie" in cam_2a:
        cam_2a.remove("Bonnie")
        cam_2b.append("Bonnie")

    if "Bonnie" in cam_5:
        cam_5.remove("Bonnie")
        cam_1b.append("Bonnie")
        
    if "Bonnie" in cam_1b:
        # Split path
        if random.randint(0,1) == 1:
            cam_1b.remove("Bonnie")
            cam_2a.append("Bonnie")
            
        else:
            cam_1b.remove("Bonnie")
            cam_5.append("Bonnie")
        
    if "Bonnie" in cam_1a:
        cam_1a.remove("Bonnie")
        cam_1b.append("Bonnie")

# Anamatronics use AI to decide wether they move, if move is True, they move to the next camera

def Bonnie(level):
    move = AI(level)
    if move:
        Bonnie_Cam_Mov()

# Chica - Copies bonnie's code with new movement path

def Chica_Cam_Mov(ai):
    global rightbspot, rdoor, gotyou, chimercytimer

    # Because Chica & Bonnie would straight kill you immediately
    if "Chica" in rightbspot and not rdoor:
        if chimercytimer < 3:
            chimercytimer += 1

        else:
            gotyou = True
            
        
    elif "Chica" in rightbspot and rdoor and not gotyou:
        rightbspot.remove("Chica")
        cam_1b.append("Chica")
        chimercytimer = 0

    if "Chica" in cam_4b:
        cam_4b.remove("Chica")
        rightbspot.append("Chica")
        
    if "Chica" in cam_4a:
        cam_4a.remove("Chica")
        cam_4b.append("Chica")
        
    if "Chica" in cam_6:
        cam_6.remove("Chica")
        cam_4a.append("Chica")
        
    if "Chica" in cam_7:
        cam_7.remove("Chica")
        cam_6.append("Chica")
        
    if "Chica" in cam_1b:
        cam_1b.remove("Chica")
        cam_7.append("Chica")
        
    if "Chica" in cam_1a:
        cam_1a.remove("Chica")
        cam_1b.append("Chica")

def Chica(level):
    move = AI(level)
    if move:
        Chica_Cam_Mov(level)

# Foxy

def Foxy(level, action):
    global alive, foxystage, power, ldoorpenalty
    
    move = AI(level)
    if move:
        foxystage += 1
        if action.lower() == "cams" or action.lower() == "cameras":
            foxystage -= 1
        
    if foxystage >= 6 and not ldoor:
        alive = False

    elif foxystage >= 5 and ldoor:
        foxystage = random.randint(0,2)
        ldoorpenalty = ldoorpenalty - 10
        print("You hear knocking on your left door...\nSomething is trying to break it down...")

#1a,1b,7,6,4a,4b
def Freddy_Cam_Mov(camera, action):
    global rdoor, fredinhall

    if "Freddy" in cam_4b and not rdoor:
        fredinhall = True

    if "Freddy" in cam_4a:
        cam_4a.remove("Freddy")
        cam_4b.append("Freddy")

    if "Freddy" in cam_6:
        cam_6.remove("Freddy")
        cam_4a.append("Freddy")

    if "Freddy" in cam_7:
        cam_7.remove("Freddy")
        cam_6.append("Freddy")
    
    if "Freddy" in cam_1b:
        cam_1b.remove("Freddy")
        cam_7.append("Freddy")

    if "Freddy" in cam_1a:
        cam_1a.remove("Freddy")
        cam_1b.append("Freddy")

def Freddy(level):
    move = AI(level)
    global fredinhall, rdoor, camera, gotyou
    if move:
        Freddy_Cam_Mov(camera, action)

    if fredinhall and not rdoor:
        if camera != "4b":
            gotyou = True

def CameraLogic():
    global camera
    # I would love to use a Switch Case statement... but it's introduced in python 3.10
    validcam = False
    while not validcam:
        camera = input("1a, 1b, 1c, 2a, 2b, 3, 4a, 4b, 5, 6, 7\n>>> ")
        
        if camera == "1a":
            print("Show Stage:" , *cam_1a)
            validcam = True
            
        elif camera == "1b":
            print("Dining Area:" , *cam_1b)
            validcam = True
            
        elif camera == "1c":
            print("Pirate Cove: Stage" , foxystage)
            validcam = True
            
        elif camera == "2a":
            print("West Hall:" , *cam_2a)
            validcam = True
            
        elif camera == "2b":
            print("West Hall Corner:" , *cam_2b)
            validcam = True
            
        elif camera == "3":
            print("Supply Closet:" , *cam_3)
            validcam = True
            
        elif camera == "4a":
            print("East Hall:" , *cam_4a)
            validcam = True
            
        elif camera == "4b":
            print("East Hall Corner:" , *cam_4b)
            validcam = True
            
        elif camera == "5":
            print("Backstage:" , *cam_5)
            validcam = True

        elif camera == "7":
            print("Restrooms:" , *cam_7)
            validcam = True
            
        elif camera == "6":
            print("Kitchen: AUDIO ONLY")
            validcam = True
            
            if "Chica" in cam_6:
                print("You hear the clanging of pots & pans...\n")

            elif "Freddy" in cam_6:
                print("A faint jingle can be heard...\n")

            # Pointless atmospheric thing for cam 6.
            else:
                cam6noise = random.randint(1,3)
                if cam6noise == 1:
                    print("There is a faint buzzing, probably just the refrigerator.")
                    lb()
                    
                elif cam6noise == 2:
                    print("The camera is... strangely silent...")
                    lb()
                    
                else:
                    easteregg = random.randint(1,1000)
                    
                    if easteregg < 990:
                        print("... The empty buzzing of the camera is very unsettling...")
                        lb()

                    else:
                        slow_print_3("IT'S ME!")
                        time.sleep(1)
                        slow_print_4(" IT'S ME! IT'S ME! IT'S ME! IT'S ME! IT'S ME! IT'S ME! IT'S ME! IT'S ME! IT'S ME! IT'S ME!")
                        for i in range(50):
                            print("IT'S ME! IT'S ME! IT'S ME! IT'S ME! IT'S ME! IT'S ME! IT'S ME! IT'S ME! IT'S ME! IT'S ME! IT'S ME! IT'S ME! IT'S ME! IT'S ME! IT'S ME! IT'S ME! IT'S ME! IT'S ME! IT'S ME! IT'S ME!")
                        1 / 0 # Ah, a classic /0 error

        else:
            print("That is not a valid camera")
            lb()



# Checks the camera to see if you're dead.
def AnamatronicCameraCheck():
    global gotyou
    
    # Camera Animatronics such as Bonnie killing you.
    if gotyou:
        global alive
        alive = False
    
    else:
        CameraLogic()
        
# Office State
def Office(action):
        global rdoor, ldoor, rdoorpenalty, ldoorpenalty
    
        if action.lower() == "debug:crash":
            raise Exception("An exception was raised due to a debug function.")

        if action.lower() == "debug:restart":
            print("Stopping program")
            time.sleep(2)
            print("Loading new instance\n")
            slow_print(". . . . . . . . . . . . ." , 0.2)
            slow_print_3("\nDone!")
            time.sleep(3)
            print("\nClearing screen\n")
            slow_print(". . . . . . . . . . ." , 0.3)
            cls()
            print(os.system("FNaF_1_Python_Redone.py"))
            exit()
            
        elif action.lower() == "cameras" or action.lower() == "cams":
            AnamatronicCameraCheck()

        elif action.lower() == "ldoor":
            print(leftbspot)
            if ldoor:
                print("The door is closed.")
            else:
                print("The door is open.")

        elif action.lower() == "rdoor":
            print(rightbspot)
            if rdoor:
                print("The door is closed.")
            else:
                print("The door is open.")

        elif action.lower() == "activate rdoor":
            if rdoor:
                rdoor = False
                print("right door open")
                rdoorpenalty = 50
                
            else:
                rdoor = True
                print("right door closed")

        elif action.lower() == "activate ldoor":
            if ldoor:
                ldoor = False
                print("left door open")
                ldoorpenalty = 50
                
            else:
                ldoor = True
                print("left door closed")

def DoorPenalty():
    global rdoorpenalty, ldoorpenalty, ldoor, rdoor
    if rdoor:
        rdoorpenalty = rdoorpenalty - 1
        if random.randint(1,50) > rdoorpenalty:
            rdoor = False
            print("The right door flies open...")
            rdoorpenalty = 50

    if ldoor:
        ldoorpenalty = ldoorpenalty - 1
        if random.randint(1,50) > ldoorpenalty:
            ldoor = False
            print("The left door flies open...")
            ldoorpenalty = 50

def GameState():
    global alive, camera, action, night, timer
    global bonnieai, chicaai, freddyai, foxyai
    while alive:
        lb()
        action = input("(Ldoor) (Rdoor) (Activate Rdoor) (Activate Ldoor) (Cameras)\n>>> ").lower()
        lb()
        # Player Action has priority
        Office(action)
        # Anamatronic movement
        Bonnie(bonnieai)
        Chica(chicaai)
        Foxy(foxyai, action)
        Freddy(freddyai)
        DoorPenalty()
    if alive == False:
        for i in range(15):
            lb()
            
        slow_print_2("You Died...")
        lb()        
Intro()          
