# TODO:
#   1) Make Each function into a different script w/ a class [easier to read that way]
#   2) Combine everything into a main.py function
#   3) Look for a linux alternative to the Win32 API for specific window capture bc that helps a LOT

from time import time
from tkinter import Image
import cv2 as cv
import numpy as np
import random as rand
import pyautogui as pag
from PIL import ImageGrab


def DetectImages(largeImage='SBT Branch/openCV Testing/Photos/SAPImg.png', detectingImage='SBT Branch/openCV Testing/Photos/lvl.png', thresh=0.8, debug=False, usingCVArr = False):
    """
        largeImage -> str\n
        detectingImage -> str\n
        thresh -> float\n
        debug -> bool\n
        Returns a list of points to click based off a theshold value given. By default, the threshold is set to 0.8.
        For display purposes, the image variables are set to a Super Auto Pets game example looking for the lvl 1 symbols.
        If debug is set to True, then it will also display the visual rectangles & points to be clicked within the larger image.
    """
    if not usingCVArr:
        # Import images
        screen = cv.imread(largeImage, cv.IMREAD_REDUCED_COLOR_2)
        level = cv.imread(detectingImage, cv.IMREAD_REDUCED_COLOR_2)
    else:
        level = cv.imread(detectingImage, cv.IMREAD_UNCHANGED)
    # Get width & height of searched image
    levelW = level.shape[1]
    levelH = level.shape[0]

    # Check where level is within screen
    result = cv.matchTemplate(screen, level, cv.TM_CCOEFF_NORMED)

    # Set up the confidence threshold
    threshold = thresh

    # Find where the most confident image replicas are located by looking @ whitest pixels in result image
    locations = np.where(result >= threshold)
    # Convert np matrix to an array of x,y coord tuples
    locations = list(zip(*locations[::-1])) 

    # Make a list of rectangle coords to be grouped together to avoid overlapping rectangles
    rectangles = []
    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), levelW, levelH]
        # Append each rectangle TWICE, bc otherwise any single-rectangles will be deleted when grouped together bc that's how it works
        rectangles.append(rect)
        rectangles.append(rect)

    # Change the rectangles array to be the grouped together array
    rectangles, weights = cv.groupRectangles(rectangles, 1, 0.5)

    # Create the array that will be returned
    points = []

    # Run through loop if there are rectangles found
    if locations:
        lineColor = (0,0,255)
        lineType = cv.LINE_4
        markerColor = (255,0,0)

        # Loop thru each rectangle location and draw it
        for (x,y,width,height) in rectangles:
            # Determine the location for the box
            top_left = (x,y)
            bottom_right = (x + width, y + height)
            # Draw
            cv.rectangle(screen, top_left, bottom_right,lineColor, lineType)

            # Get a position within the rectangle itself to click
                # TO DO: Make the position random, to avoid bot detection or something like that
            centerX = x + int(width/2)
            centerY = y + int(height/2)
            point = [centerX, centerY]
            points.append(point)
            cv.drawMarker(screen, (centerX, centerY), markerColor, markerType=0)

        if debug:
            cv.imshow('Matches', screen)
            cv.waitKey()
            cv.destroyAllWindows()

        return points
    else:
        print("No level 1 pets found")
        points.append(-1)
        return points

def LiveFeed(display = False):
    loopTime = time()
    while(True):
        # Take screenshot w/ PyAutoGUI and convert the color to be correct
        screenshot = ImageGrab.grab()
        screenshot = np.array(screenshot)
        screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)

        # Display the image
        if display:
            cv.imshow('Game', screenshot)
        print(f"FPS {(1 / (time() - loopTime))}")
        loopTime = time()

        # Press 'q' with the output window focused to exit
        # Waits 1 ms every loop to process key presses
        if cv.waitKey(1) == ord('q'):
            break
    

if __name__ == "__main__":
    points = DetectImages(debug=True)
    #LiveFeed()