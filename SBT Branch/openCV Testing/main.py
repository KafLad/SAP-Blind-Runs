# Third-Party Library Imports
import cv2 as cv
import time
import os
import threading

# Personal Library Imports
from feed import WindowCapture
from vision import Vision
from logic import Logic


# Set up The base directory for each image folder
foodDir = 'SBT Branch\\photos\\Food'
petDir = 'SBT Branch\\photos\\Pet'
teamDir = 'SBT Branch\\photos\\Team'
uiDir = 'SBT Branch\\photos\\UI'

# Get all the images in each specific folder from earlier
foodFiles = os.listdir(foodDir)
petFiles = os.listdir(petDir)
uiFiles = os.listdir(uiDir)

# Create Arrays of Vision objects that look for the images in each folder
foodEyes = []
for food in foodFiles:
    path = foodDir + '\\' + food
    vision = Vision(path, text=food)
    foodEyes.append(vision)

petEyes = []
for pet in petFiles:
    path = petDir + '\\' + pet
    vision = Vision(path, text=pet)
    petEyes.append(vision)

uiEyes = []
for ui in uiFiles:
    path = uiDir + '\\' + ui
    vision = Vision(path, text=ui)
    uiEyes.append(vision)

# Set up the WindowCapture object to be able to capture the screen
screenView = WindowCapture()
# Set up the time object to be able to calculate the FPS of the screen capture
loopTime = time.time()

# Hard Code the 'End Turn' UI Button
path = uiDir[:-3] + '\\' + 'End.png'
endView = Vision(path)

# Set all the vars used above to None for garbage collection
path, petFiles, foodFiles, uiFiles = None, None, None, None

# FPS Debug Enabling
framesDebug = False

logic = Logic()



# Functions -- USED FOR MULTITHREADING
def petUpdate():
    # Scan image to see what pets are on the screen then highlight & label them
    for v in petEyes:
        name, coords = v.find(screenshot, threshold=0.8, debug_mode='rectangles', type='Pet')
        # If there are pets on the screen, decide where the pet goes
        if len(coords) >= 1:
            # If the pet is in the shop, throw into shop lists
            for i in range(len(coords)):
                if coords[i][1] > 300:
                    shopCoords.append(coords[i])
                    shopPets.append(name)
                else:
                    teamCoords.append(coords[i])
                    teamPets.append(name)

def foodUpdate():
    for v in foodEyes:
        name, coords = v.find(screenshot, threshold=0.8, debug_mode='rectangles', type='Food')
        shopFood.append(name)
        foodCoords.append(coords)

def uiUpdate():
    # Initialize temp list that is used to find empty spots in the team
    rockCoords = []

    # Scan image for any UI elements [if rocks found, throw into temp rock list]
    for v in uiEyes:
        name, coords = v.find(screenshot, threshold=0.8, debug_mode='rectangles', type='UI')
        if v.txt == 'Rock':
            rockCoords = coords

    # If rocks found, throw and empty team slots into team list so that way it can know where to click on empty slots
    if len(rockCoords) != 0:
        for r in rockCoords:
            if r[1] > 300:
                rockCoords.remove(r)
            else:
                teamCoords.append(r)
                teamPets.append('Rock')

# Thread Starting Info
threads = list()
funcs = [petUpdate, foodUpdate, uiUpdate]

# Main Loop
while(True):
    # First, take screenshot
    screenshot = screenView.GetStaticScreenshot()
    
    # Scan for the End Turn Icon
    turnName, turnCoords = endView.find(screenshot, threshold=0.8, debug_mode='rectangles', type='UI')
    
    # If the End Turn Icon is found, start scanning for everything else 
    if len(turnCoords) >= 1:
        # Initialize the main lists that will be passed to logic
        shopPets = []
        shopCoords = []
        teamPets = []
        teamCoords = []
        shopFood = []
        foodCoords = []

        # Initialize & Run threads -- These scan for items on the screen
        for i in range(3):
            x = threading.Thread(target=funcs[i])
            threads.append(x)
            x.start()
        
        for thread in (threads):
            thread.join()
    
    # If debug mode to show FPS is on, then print it & update calculation
    if framesDebug:
        print(f'FPS {2 / (time.time() - loopTime)}')
        loopTime = time.time()

    
    # Check to see if the 'q' key is pressed, if it is, close the window
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break