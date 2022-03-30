import cv2 as cv
import time
from feed import WindowCapture
from vision import Vision


screenView = WindowCapture()
levelVision = Vision('SBT Branch\\openCV Testing\\lvl.png')
levelVision2 = Vision('SBT Branch\\openCV Testing\\lvl_test.png')

loopTime = time.time()
while(True):
    screenshot = screenView.GetStaticScreenshot()
    #points = levelVision.find(haystack_img=screenshot, debug_mode='rectangles')
    points = levelVision2.find(haystack_img=screenshot, debug_mode='rectangles')
    #print(f'FPS {2 / (time.time() - loopTime)}')
    loopTime = time.time()

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break