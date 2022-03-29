import numpy as np
import win32ui, win32gui, win32con
import pyautogui as pag
import cv2 as cv


class WindowCapture:
    w = 0
    h = 0
    hwnd = None
    cropped_x = 0
    cropped_y = 0
    offset_x = 0
    offset_y = 0

    # Constructor for Window-Specific Capture
    def __init__(self, windowName=None):
        if windowName != None:
            # Find the window
            self.hwnd = win32gui.FindWindow(None, windowName)
            if not self.hwnd:
                raise Exception(f'Window not found: "{windowName}"')

            # Get the window size
            window_rect = win32gui.GetWindowRect(self.hwnd)
            self.w = window_rect[2] - window_rect[0]
            self.h = window_rect[3] - window_rect[1]

            # Account for window border
            borderPixels = 8
            titlebarPixels = 30
            self.w = self.w - (borderPixels * 2)
            self.h = self.h - titlebarPixels - borderPixels
            self.cropped_x = borderPixels
            self.cropped_y = titlebarPixels

            # Set the cropped coords offset to translate images into clickable coords
            self.offset_x = window_rect[0] + self.cropped_x
            self.offset_y = window_rect[1] + self.cropped_y
        else:
            self.w = 800
            self.h = 600

    def GetScreenShot(self):
        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt( (0,0), (self.w,self.h), dcObj, (self.cropped_x,self.cropped_y), win32con.SRCCOPY)
        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (self.h, self.w, 4)

        #Free Up Resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        img = img[...,:3]
        img = np.ascontiguousarray(img)

        return img

    def GetStaticScreenshot(self):
        screen = pag.screenshot()
        screenArr = np.array(screen)
        cropped = screenArr[:620, 1120:, :]
        img = cv.cvtColor(cropped, cv.COLOR_RGB2BGR)
        return img



    # WWARNING: WILL ONLY WORK IF YOU DON'T MOVE YOUR GAME WINDOW AFTER RUNNING SCRIPT
    def GetScreenPosition(self, pos):
        return (pos[0] + self.offset_x, pos[1] + self.offset_y)


if __name__ == "__main__":
    test = WindowCapture()
    test.GetStaticScreenshot()