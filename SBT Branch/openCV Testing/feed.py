from PIL import ImageGrab
import cv2 as cv
from time import time
import numpy as np

class Feed():
    def LiveFeed(display = False):
        loopTime = time()
        # Take screenshot w/ PyAutoGUI and convert the color to be correct
        screenshot = ImageGrab.grab()
        screenshot = np.array(screenshot)
        screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)

        print(f"FPS {(1 / (time() - loopTime))}")
        loopTime = time()
        return screenshot