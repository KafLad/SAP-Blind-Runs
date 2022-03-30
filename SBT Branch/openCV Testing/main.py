import cv2 as cv
import time
import os
from feed import WindowCapture
from vision import Vision

# Set up The base directory for each image folder
foodDir = 'SBT Branch\\photos\\Food'
petDir = 'SBT Branch\\photos\\Pet'
teamDir = 'SBT Branch\\photos\\Team'
uiDir = 'SBT Branch\\photos\\UI'

# Get all the images in each specific folder from earlier
foodFiles = os.listdir(foodDir)
petFiles = os.listdir(petDir)
teamFiles = os.listdir(teamDir)
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

teamEyes = []
for team in teamFiles:
    path = teamDir + '\\' + team
    vision = Vision(path, text=team)
    teamEyes.append(vision)

uiEyes = []
for ui in uiFiles:
    path = uiDir + '\\' + ui
    vision = Vision(path, text=ui)
    uiEyes.append(vision)

# Set up the WindowCapture object to be able to capture the screen
screenView = WindowCapture()
# Set up the time object to be able to calculate the FPS of the screen capture
loopTime = time.time()
# Set starting state of the boolean to either scan for everything or just the UI
scanFull = True

# Hard Code the 'End Turn' UI Button
path = uiDir + '\\' + 'End.png'
endView = Vision(path)
###################
#   CHANGE TO TRUE TO RUN PROGRAM
#################
playGame = True
#################
# CHANGE TO TRUE TO RUN PROGRAM
#################

while(playGame):
    
    screenshot = screenView.GetStaticScreenshot()
    turnName, turnCoords = endView.find(screenshot, threshold=0.8, debug_mode='rectangles', type='UI')
    if len(turnCoords) >= 1:
        shopPets = []
        shopCoords = []
        teamPets = []
        teamCoords = []
        for v in petEyes:
            name, coords = v.find(screenshot, threshold=0.8, debug_mode='rectangles', type='Pet')
            if len(coords) >= 1:
                if coords[0][1] > 300:
                    shopPets.append(name)
                    shopCoords.append(coords)
                else:
                    teamPets.append(name)
                    teamCoords.append(coords)
        shopFood = []
        foodCoords = []
        for v in foodEyes:
            name, coords = v.find(screenshot, threshold=0.8, debug_mode='rectangles', type='Food')
            shopFood.append(name)
            foodCoords.append(coords)
    
    #print(f'FPS {2 / (time.time() - loopTime)}')
    loopTime = time.time()

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break