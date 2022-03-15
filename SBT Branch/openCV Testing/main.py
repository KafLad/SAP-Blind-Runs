import cv2 as cv
from feed import Feed
from vision import Vision
from PIL import Image

screenView = Feed()
eyes = Vision()

while True:
    screen = screenView.LiveFeed()
    screenView.image = screen
    points = eyes.DetectImages(usingCVArr=True)
    
    if cv.waitKey(1) == ord('q'):
        break
