import cv2 as cv
import time
from feed import WindowCapture
from vision import Vision


screenView = WindowCapture()
levelVision = Vision('SBT Branch\\photos\\rock.png')
signVision = Vision('SBT Branch\\photos\\sign.png')
loopTime = time.time()
while(True):
    screenshot = screenView.GetStaticScreenshot()
    rockPoints = levelVision.find(haystack_img=screenshot, debug_mode='rectangles', type='Team')
    signPoints = signVision.find(screenshot, debug_mode='rectangles')
    #print(f'FPS {2 / (time.time() - loopTime)}')
    loopTime = time.time()

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break